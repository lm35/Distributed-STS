# USAGE
#python3.8 Cntralzd_occupProbPair.py --dataencodings 2k_masterCSTS_Encodings.pickle --keyUsrValEncod Cntralzd_keyUsrValEncod.pickle --gtencodingsCentr 2k_testCSTS_Encodings.pickle > OccupProb.txt



# import the necessary packages
import face_recognition
import argparse
import pickle
import cv2
import numpy as np
import sqlite3
import csv
import time
from modules import config
#print ("time.time(): %f " %  time.time())
#print (time.localtime( time.time() ))
#print (time.asctime( time.localtime(time.time()) ))
#start_time = time.time()

#Get minimum distance from the distance vector
#def minDist(f_distances):
#	print("Face distances ",f_distances)
#	DataSetLen = len(f_distances)
#	print("Length of data set is ", DataSetLen)
#	Occupant_Count = DataSetLen/20
#	split_face_distances = np.array_split(f_distances,Occupant_Count)
#	#print("Split are",split_face_distances)
#	min_sublist_facedist = [(i*20,min(split)) for (i,split) in enumerate(split_face_distances)]# Saving as [(index,min_dist)]
#	print("Minimum Distances are",min_sublist_facedist)
#	list1_index,list2_dist = zip(*min_sublist_facedist)
#	min_list2_dist = min(list2_dist)
#	min_list2_dist.append(min(list2_dist))
#	print("min_list2_dist is ",min_list2_dist)
#	return list1_index,list2_dist,min_list2_dist
def minDist(f_distances,min_list2_dist):
    #print("Face distances:", f_distances)
    DataSetLen = len(f_distances)
    #print("Length of data set is:", DataSetLen)
    Occupant_Count = DataSetLen // 20  # Ensure integer division
    split_face_distances = np.array_split(f_distances, Occupant_Count)
    min_sublist_facedist = [(i * 20, min(split)) for i, split in enumerate(split_face_distances)]
    #print("Minimum Distances:", min_sublist_facedist)
    list1_index, list2_dist = zip(*min_sublist_facedist)
    # Fix is here: create min_list2_dist as a new list and append the minimum value
    min_list2_dist.append(min(list2_dist))

    #print("list2_dist is:", list2_dist)
    return list1_index, list2_dist, min_list2_dist


#Convert distance into probability
def distProbConvlist(list2_dist):
	DistScorLen = len(list2_dist)
	Mean = np.sum(list2_dist)/ len(list2_dist)
	face_distancesMinsMean = [i - Mean for i in list2_dist]#(x_i - Mu)
	SqrFcDstMinMen = [i*i for i in face_distancesMinsMean] #(x_i - Mu)^2
	DistSquare = [i*i for i in list2_dist]
	SumSqrFcDstMinMen = np.sum(SqrFcDstMinMen) #Sigma(x_i - Mu)^2
	StdDevtn = np.sqrt(SumSqrFcDstMinMen/(DistScorLen-1)) # Standard Deviation
	Dist2ProbDinom = [np.exp((-i)/(2*StdDevtn*StdDevtn)) for i in DistSquare]
	SumDist2ProbDinom =  np.sum(Dist2ProbDinom)
	Dist2Prob = [round(np.exp((-(a)/(2*StdDevtn*StdDevtn)))/SumDist2ProbDinom,5) for a in DistSquare]
	return Dist2Prob


## construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-de", "--dataencodings", required=True,
#	help="name of serialized db of facial encodings")
#ap.add_argument("-ku", "--keyUsrValEncod",
#	help="name of serialized db of Event Probability Pair")
#ap.add_argument("-ge", "--gtencodingsCentr", required=True,
#	help="name of  serialized db of groundTruth (Occupants involved in event generation) encodings for b1/b2")
##ap.add_argument("-ev", "--event", required=True,
##	help="name of serialized db of Events")
#ap.add_argument("-d", "--detection-method", type=str, default="cnn",
#	help="face detection model to use: either `hog` or `cnn`")
#args = vars(ap.parse_args())


def event_gen(building_id,d_thresh, output_keyvalue_pickle_path, reg_encod_filepath, reg_nameidind_filepath, visit_encod_filepath, visit_nameidind_filepath, zoneid):
    # load the known faces and embeddings for centralized approach
    print("[INFO] loading data encodings...")
    '''
    gt_train_pickle = config.TEST_ENCODINGS  # Update with your actual file path

    # Load the pickle file before accessing it
    with open(gt_train_pickle, "rb") as file:
        data = pickle.load(file)  # Now it's a dictionary
    '''
    #Distribution
    # load the Ground Truth faces and embeddings for the centralized approach

    gt_test_pickle = config.TEST_ENCODINGS  # Update with your actual file path

    # Load the pickle file before accessing it
    print("[INFO] loading Ground Truth Test encodings...")
    with open(gt_test_pickle, "rb") as file:
        gt_eventset = pickle.load(file)  # Now it's a dictionary
    #print("Test Names are",gt_eventset["Cntralzd_GTNames"])
    #gt_eventset = pickle.loads(open(args["gtencodingsCentr"], "rb").read())
    #print("reg_encod_filepat is",reg_encod_filepath)
    data = pickle.loads(open(reg_encod_filepath, "rb").read())
	#visit_path = getattr(config, visit_encod)
    visitor = pickle.loads(open(visit_encod_filepath, "rb").read())

    #load the EventPool
    print("[INFO] loading EventPool...")
    ##ep = pickle.loads(open(args["event"], "rb").read())

    #evProbPair_b2 = pickle.loads(open(args["keyUsrValEncod"], "rb").read())
    #print("Event Pool is",evProbPair_b2)


    # initialize the list of names for each face detected
    Occup_names = [] #Name of occupants in the event pool
    #Distribution = []
    nameTocsv = []
    min_list2_dist = [] #To get the minimum distance for each test image
    min_list2_dist_v = []
    face_distances = [] #Distance between test and data encodingsmaster_DataEncodings.picklemaster_DataEncodings.picklemmaster_DataEncodings.picklemaster_DataEncodings.picklemaster_DataEncodings.pickleaster_DataEncodings.pickle
    Dist2Prob =[] #Distance converted to probability
    Events = [] #Events generated from test encodings
    j = 0 # A counter appended to test occupant names while
    x=0
    flag = 0 # To decide from which encoding db, name has to be fetched
    eventKeyValue ={} # Dictionary with {occupantname:event probability}
    encoding_counter = 0
    min_dist_b1 = []
    min_dist_m = []
    event_gt_encode_dict = {}
    recognized_event = []
    actual_event = []
    distance_list = []
    actual_List  = []
    predicted_List = []
    prediction_status = []
    #building_id = 3  # or whatever value you're working with
    reg_encodings_key = str(f"b{building_id}_DataEncodings")
    visit_encodings_key = str(f"b{building_id}_VisitorEncodings")
    reg_name_key = str(f"b{building_id}_DataNames")
    visit_name_key = str(f"b{building_id}_VisitorNames")

    #Get path to the file containing Name , ID, Index of registered occupants
    #occupID_path = config.OCCUPANT_IDS
    #occupID_path_init = config.OCCUPANT_IDS_INIT
    ##occupID_path = config.INTER_NAMEFILE
    ###Map occupants from each building to their corresponding IDs.
    ###"master_nameLabelMap.csv" has the name and Id's of occupants from all buildings
    with open(reg_nameidind_filepath, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        namLablDict = {}
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["Occupant Name"]} : {row["OccupID"]}')
			#print("Dictionary is", dict(row))
            namLablDict.update({row["Occupant Name"]:row["OccupID"]})
            line_count += 1
    encoding_counter = 0
    max_prob_values = []
    #Map visitors from b2 to their corresponding IDs from the visitor master csv file with all occupant IDs
    with open(visit_nameidind_filepath, mode='r') as csv_file:
    	csv_reader = csv.DictReader(csv_file)
    	line_count = 0
    	visitor_nameLabelMapDict = {}
    	for row in csv_reader:
    		if line_count == 0:
    			print(f'Column names are {", ".join(row)}')
    			line_count += 1
    		print(f'\t{row["Occupant Name"]} : {row["OccupID"]}')
    		#print("Dictionary is", dict(row))
    		visitor_nameLabelMapDict.update({row["Occupant Name"]:row["OccupID"]})
    		#OccupName.append(row["Occupant Name"])
    		#ID.append(row["OccupID"])
    		line_count += 1
    	#print(f'Processed {line_count} lines.')

    #Map master name, id  from building-specific files to their corresponding IDs from the visitor master csv file with all occupant IDs
    master_occupantID = config.OCCUPANT_IDS_INIT
    with open(master_occupantID, mode='r') as csv_file:
    	csv_reader = csv.DictReader(csv_file)
    	line_count = 0
    	master_nameLabelMapDict = {}
    	for row in csv_reader:
    		if line_count == 0:
    			print(f'Column names are {", ".join(row)}')
    			line_count += 1
    		print(f'\t{row["Occupant Name"]} : {row["OccupID"]}')
    		#print("Dictionary is", dict(row))
    		master_nameLabelMapDict.update({row["Occupant Name"]:row["OccupID"]})
    		#OccupName.append(row["Occupant Name"])
    		#ID.append(row["OccupID"])
    		line_count += 1
    	#print(f'Processed {line_count} lines.')


    #Random index for testimages in ground truth
    #Ensure different images are used for different events and as the index file is
    #Shared between centralized and distributed same events pick same images in CSTS and DSTS
    unique_index_eventoccup = config.OCCUPANT_INDEX_LIST_FOREACHBUILD
    unique_index_eventoccup_backup = config.OCCUPANT_INDEX_LIST_FOREACHBUILD_BACKUP
    with open(unique_index_eventoccup, "rb") as file:
        while True:
            try:
                indexPool = pickle.load(file)
                print(indexPool)
            except EOFError:  # Stop reading when end-of-file is reached
                break

    for i in gt_eventset["Cntralzd_GTEncodings"]:
        start_time = time.time()
        face_distances = face_recognition.face_distance(data[reg_encodings_key],i)
        current_encoding_occupname = gt_eventset["Cntralzd_GTNames"][encoding_counter]
        #print("current_encoding_occupname ",current_encoding_occupname)
        encoding_counter += 1
        list1_index,list2_dist,min_list2_dist = minDist(face_distances,min_list2_dist)
        #with open('distvector_time.csv', mode='a', newline='') as csv_file1:
        #	csv_file1.write("%s\n"%((time.time() - start_time)))
        #print("min_list2_dist and distane_threshold is", min_list2_dist, float(d_thresh))

        if float(min(list2_dist)) >= float(d_thresh):#If minimum distance upon comparison of event encodings with b2 Reg. Occup. is greater that d_thresh, then compare current face encodings with b2's visitor set
            flag = 1
            print("min distance greater than threshold")
            m_face_distances = face_recognition.face_distance(visitor[visit_encodings_key],i) #compare current face encodings with b2's visitor set and get minimum
            #print("Length of master distance score is",len(m_face_distances))
            list1_index_v,list2_dist_v,min_list2_dist_v = minDist(m_face_distances,min_list2_dist_v)
            min_dist_m.append(min(list2_dist_v))
            #with open('dist_time_visitor.csv', mode='a', newline='') as csv_file:
            #    csv_file.write("%s,%s\n"%((time.time() - start_time,time.time() - start_time_1)))
    	#print("Minimum Face distances with b2 is  ",list2_dist)
            Dist2Prob = distProbConvlist(list2_dist_v)

        if flag !=1:
            Dist2Prob = distProbConvlist(list2_dist)
        max_prob = np.amax(Dist2Prob)#Find the maximum Prob value from the array of Prob values
        max_prob_values.append(max_prob)
        index_maxProb = np.where(Dist2Prob == np.amax(Dist2Prob))#Get the index of the max Prob value
        index_maxProb_npary = [a for B in index_maxProb for a in B]#index-maxProb is a tuple, to get the Prob value first convert tuple into array
        #print("index_maxProb_npary is ", index_maxProb_npary)
        #Then take the first element of the array
        check = int(index_maxProb_npary[0])#Get the first element from the max Prob nparray
        #print("Check is", check)
        check_scalar = (np.asscalar(np.array([check])))*20#Convert check to a scalar value
	#print("Check_Scalar",check_scalar)
        if j == 0:
        	x = 1
        else:
        	if(i_occupName != current_encoding_occupname):
        		x = 1
        if flag == 0:
            index_new = indexPool[str(current_encoding_occupname)][x-1]
            name_higProb = data[reg_name_key][check_scalar]# Get name of individual corresponding to highest Prob
            eventKeyValue.update({namLablDict[name_higProb]+'_e'+str(index_new):Dist2Prob})
            #print("Occupant with  maximum probability is ",name_higProb)
        	#print("namLablDict[name_higProb]",namLablDict[name_higProb])
        	#print("--- %s seconds Flag = 0---" % (time.time() - start_time))
        	#with open('time.csv', mode='a', newline='') as csv_file2:
        	#	#csv_writer = csv.writer(csv_file)
        	#	csv_file2.write("%s,%s\n"%((time.time() - start_time),name_higProb))
        else:
            index_new = indexPool[str(current_encoding_occupname)][x-1]
            name_higProb = str(visitor[visit_name_key][check_scalar])
            print("Occupant with  maximum probability in not in b2 and is ",name_higProb)
#    		print("b2_visitor_nameLabelMapDict[name_higProb]",b2_visitor_nameLabelMapDict[name_higProb])
#    		print("Occupant with  maximum probability  is in b2 from data encoding names is b2_namLablDict[current_encoding_occupname] is ",master_nameLabelMapDict[current_encoding_occupname])
            eventKeyValue.update({master_nameLabelMapDict[current_encoding_occupname]+'_e'+str(index_new):Dist2Prob})
    		#actual_event.append(master_nameLabelMapDict[current_encoding_occupname]+'_e'+str(index_new))
    		#with open('time_visitor.csv', mode='a', newline='') as csv_file:
    		#	csv_file.write("%s,%s\n"%((time.time() - start_time),name_higProb))
        flag = 0
        #If for a single occupant more than 10 events, use 'str(x)' else for many occupants with 10 or less than 10 events use j
        #eventKeyValue.update({namLablDict[current_encoding_occupname]+'_e'+str(index_new):Dist2Prob})#Since we experiment for a single occupant alone, all images in test db belongs to a single occupant hence we can append event counter which s same as value of x to event index instead of j
        #print("namLablDict[name_higProb]",{namLablDict[current_encoding_occupname]+'_e'+str(index_new):Dist2Prob})
        #print("Value of i is",x)
        #print("Name Dictionary",namLablDict[name_higProb])
        x = x+1
        j = x
	#-------------------------------
        Events.append(Dist2Prob)
        Occup_names.append(name_higProb)
        i_occupName = current_encoding_occupname
    print("Minimum distance list is ", min_list2_dist)
    print("Min in minmum Distance is ",min(min_list2_dist))
    print("Maximum Distance in minimum distance list is ",max(min_list2_dist))
    print("Total number of events",encoding_counter)
    print("Value of x is",x)
    print("Total number of events",encoding_counter)
    print("Event Key values are", eventKeyValue)
    print("Maximum Probabilities are ",max_prob_values)
	#f_kv = open(args["keyUsrValEncod"], "wb")
	#f_kv.write(pickle.dumps(eventKeyValue))
	#f_kv.close()

	# Use the file location from config.py to get the path to store events "key:value" pair
    #output_keyvalue_pickle_path = config.EVENT_KEYVALUE_CSTS

    # Write the eventKeyValue dictionary to the specified location
    with open(output_keyvalue_pickle_path, "wb") as f_kv:
        pickle.dump(eventKeyValue, f_kv)
    #print("Length of event probability pair is ",len(eventKeyValue))

    print(f"[INFO] Event key-value encodings saved to: {output_keyvalue_pickle_path}")
