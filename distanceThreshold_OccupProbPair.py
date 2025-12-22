# USAGE
#python3.8 distanceThreshold_OccupProbPair.py > out_distanceth_27032025.txt


# import the necessary packages
import face_recognition
import argparse
import pickle
import cv2
import numpy as np
import sqlite3
import csv
import time
import config

#Get minimum distance from the distance vector
def minDist(f_distances):
	#print("Face distances ",f_distances)
	DataSetLen = len(f_distances)
	#print("Length of data set is ", DataSetLen)
	Occupant_Count = DataSetLen/20 #Divided by 30 as the count of images for each occupant is 30 in comparison set
	#print("Occupant_Count ",Occupant_Count)
	split_face_distances = np.array_split(f_distances,Occupant_Count)#Split the distance vector into subvectors(sublist) corresponding to each face encodings in the comparison set
	#print("Split are",split_face_distances)
	min_sublist_facedist = [(i*20,min(split)) for (i,split) in enumerate(split_face_distances)]# Saving as [(index,min_dist)]
	#print("Minimum Distances are",min_sublist_facedist)
	list1_index,list2_dist = zip(*min_sublist_facedist) #Find the minimum distance from each sublist and the corresponding index at which the minimum distance occurred
	min_list2_dist = min(list2_dist)
	min_lis2_dist.append(min(list2_dist))
	#print("min_list2_dist is ",min_list2_dist)
	return list1_index,list2_dist,min_list2_dist


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


##Not Loading master encodings as comparison only with building specific visitor set

# initialize the list of names for each face detected
Occup_names = [] #Name of occupants in the event pool
#Distribution = []
nameTocsv = []
min_lis2_dist = [] #To get the minimum distance for each test image
face_distances = [] #Distance between test and data encodingsmaster_DataEncodings.picklemaster_DataEncodings.picklemmaster_DataEncodings.picklemaster_DataEncodings.picklemaster_DataEncodings.pickleaster_DataEncodings.pickle
Dist2Prob =[] #Distance converted to probability
Events = [] #Events generated from test encodings
eventKeyValue ={} # Dictionary with {occupantname:event probability}

def get_registered(file_path_reg):
#Map occupants from b1 to their corresponding IDs from the b1 csv file with all occupant IDs
	with open(file_path_reg, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 0
		reg_namLablDict = {}
		for row in csv_reader:
			if line_count == 0:
				#print(f'Column names are {", ".join(row)}')
				line_count += 1
			#print(f'\t{row["Occupant Name"]} : {row["OccupID"]}')
			#print("Dictionary is", dict(row))
			reg_namLablDict.update({row["Occupant Name"]:row["OccupID"]})
			#OccupName.append(row["Occupant Name"])
			#ID.append(row["OccupID"])
			line_count += 1
	return reg_namLablDict
		#print(f'Processed {line_count} lines.')

def get_visitor(file_path_visitor):
	#Map visitors from b1 to their corresponding IDs from the visitor master csv file with all occupant IDs
	with open(file_path_visitor, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 0
		visit_namLablDict = {}
		for row in csv_reader:
			if line_count == 0:
				#print(f'Column names are {", ".join(row)}')
				line_count += 1
			#print(f'\t{row["Occupant Name"]} : {row["OccupID"]}')
			#print("Dictionary is", dict(row))
			visit_namLablDict.update({row["Occupant Name"]:row["OccupID"]})
			#OccupName.append(row["Occupant Name"])
			#ID.append(row["OccupID"])
			line_count += 1
	return visit_namLablDict
		#print(f'Processed {line_count} lines.')

def get_master():
	master_nameidlist = config.OCCUPANT_IDS_INIT
	#Map master from b2 to their corresponding IDs from the visitor master csv file with all occupant IDs
	with open(master_nameidlist, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 0
		master_nameLabelMapDict = {}
		for row in csv_reader:
			if line_count == 0:
				#print(f'Column names are {", ".join(row)}')
				line_count += 1
			#print(f'\t{row["Occupant Name"]} : {row["OccupID"]}')
			#print("Dictionary is", dict(row))
			master_nameLabelMapDict.update({row["Occupant Name"]:row["OccupID"]})
			#OccupName.append(row["Occupant Name"])
			#ID.append(row["OccupID"])
		line_count += 1
	return master_nameLabelMapDict

		#print(f'Processed {line_count} lines.')


'''
#-------------------Get the Dict of events mapped to Zone of occurrence
with open(args["EventSeq1_Clockwise"], mode='r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	#line_count = 0 # To check if all rows are being read
	EventZoneOccrMapDict = {}
	eventTimeDict = {}
	event_gt_Dict = {}
	time_list = []
	zones = []
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		EventZoneOccrMapDict.update({row["Event"]:row["Zone"]})
		eventTimeDict.update({row["Event"]:row["Time"]})
		event_gt_Dict.update({row["Event"]:row["GT"]})
		time_list.append(row["Time"])
		zones.append(row["Zone"])
'''
#building_id,i,master_nameLabelMapDict,reg_encod_filepath, reg_nameidind_filepath, visit_encod_filepath, visit_nameidind_filepath
def get_distance(building_id,d_thresh,master_nameLabelMapDict,reg_encod_filepath, reg_nameidind_filepath, visit_encod_filepath, visit_nameidind_filepath):

	#reg_path = getattr(config, reg_encod)
	print("reg_encod_filepat is",reg_encod_filepath)
	data = pickle.loads(open(reg_encod_filepath, "rb").read())
	#visit_path = getattr(config, visit_encod)
	visitor = pickle.loads(open(visit_encod_filepath, "rb").read())
	#Distribution
	# load the Ground Truth faces and embeddings
	#print("[INFO] loading Ground Truth encodings...")
	gt_1 = pickle.loads(open('21rmvd_test_crop_Encodings.pickle', "rb").read())
	#print("Test Names are",gt_1["b1_mixed_OccupInGTNames"])
	# initialize the list of names for each face detected
	Occup_names = [] #Name of occupants in the event pool
	#Distribution = []
	nameTocsv = []
	min_lis2_dist = [] #To get the minimum distance for each test image
	face_distances = [] #Distance between test and data encodingsmaster_DataEncodings.picklemaster_DataEncodings.picklemmaster_DataEncodings.picklemaster_DataEncodings.picklemaster_DataEncodings.pickleaster_DataEncodings.pickle
	Dist2Prob =[] #Distance converted to probability
	Events = [] #Events generated from test encodings
	j = 0 # A counter appended to test occupant names while
	x = 0
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
	data_key = str(f"b{building_id}_DataEncodings")
	visitor_key = str(f"b{building_id}_VisitorEncodings")
	#print("data_key  is",data_key)
	#print("data[data_key] hard code is",data[data_key])
	#face_distances = face_recognition.face_distance(data[data_key], i)
# loop over the facial embeddings
	for i in gt_1["Cntralzd_GTEncodings"]:
		#print("master_nameLabelMapDict is",master_nameLabelMapDict)
		current_encoding_occupname = gt_1["Cntralzd_GTNames"][encoding_counter]
		#print("current_encoding_occupname ", current_encoding_occupname)
		encoding_counter += 1
		face_distances = face_recognition.face_distance(data[data_key],i)
		list1_index,list2_dist,min_list2_dist = minDist(face_distances)
		#print("Minimum Face distances with b1 is  ",list2_dist)
		min_dist_b1.append(min(list2_dist))
		distance_list.append(d_thresh)
		#print("id_current = master_nameLabelMapDict[current_encoding_occupname] is",master_nameLabelMapDict[current_encoding_occupname])
		actual_event.append(master_nameLabelMapDict[current_encoding_occupname]+'_e')
		id_current = master_nameLabelMapDict[current_encoding_occupname]
		if (str(id_current[0:3]) == "o_"+str(building_id)):
			actual_List.append("Registered")
			actual_to_Check = "Registered"
		else:
			actual_List.append("Visitor")
			actual_to_Check = "Visitor"
		#NOTE : Actual mindist value was '0.34'
	#print("Condition   ",min_list2_dist >= 0.34)
		if float(min_list2_dist) >= float(d_thresh):#If minimum distance upon comparison of event encodings with b1 Reg. Occup. is greater that d_b1, then compare current face encodings with b1's visitor set
			flag = 1
			#print("min distance greater than threshold")
			m_face_distances = face_recognition.face_distance(visitor[visitor_key],i) #compare current face encodings with b1's visitor set and get minimum
			#print("Length of master distance score is",len(m_face_distances))
			list1_index_v,list2_dist_v,min_list2_dist_v = minDist(m_face_distances)
			min_dist_m.append(min(list2_dist_v))
			Dist2Prob = distProbConvlist(list2_dist_v)
			predicted_List.append("Visitor")
			predicted_to_Check = "Visitor"
		if flag != 1:
			Dist2Prob = distProbConvlist(list2_dist)
			predicted_List.append("Registered")
			predicted_to_Check = "Registered"
		flag = 0
		if (str(actual_to_Check) == str(predicted_to_Check)):
			prediction_status.append("True")
		else:
			prediction_status.append("False")

	return(distance_list,actual_event,actual_List,predicted_List,prediction_status)
# Set the random seed for reproducibility
np.random.seed(42)

# Generate 100 random numbers between 0 and 1
random_numbers = np.random.uniform(low=0.0, high=1.0, size=100)

# Round to 4 decimal places
random_numbers = np.round(random_numbers, 4)

# Print or use the result
print(random_numbers)# Print the generated random numbers
registered_encodings = ['B1_REG_ENCODINGS', 'B2_REG_ENCODINGS', 'B3_REG_ENCODINGS', 'B4_REG_ENCODINGS', 'B5_REG_ENCODINGS', 'B6_REG_ENCODINGS', 'B7_REG_ENCODINGS', 'B8_REG_ENCODINGS', 'B9_REG_ENCODINGS', 'B10_REG_ENCODINGS', ]
reg_nameidlbl = ['B1_OCCUPANT_IDS_INIT','B2_OCCUPANT_IDS_INIT','B3_OCCUPANT_IDS_INIT','B4_OCCUPANT_IDS_INIT','B5_OCCUPANT_IDS_INIT','B6_OCCUPANT_IDS_INIT','B7_OCCUPANT_IDS_INIT','B8_OCCUPANT_IDS_INIT','B9_OCCUPANT_IDS_INIT','B10_OCCUPANT_IDS_INIT']
visitor_encodings = ['B1_VISIT_ENCODINGS', 'B2_VISIT_ENCODINGS', 'B3_VISIT_ENCODINGS', 'B4_VISIT_ENCODINGS', 'B5_VISIT_ENCODINGS', 'B6_VISIT_ENCODINGS', 'B7_VISIT_ENCODINGS', 'B8_VISIT_ENCODINGS', 'B9_VISIT_ENCODINGS', 'B10_VISIT_ENCODINGS' ]
visit_nameidlbl = ['B1_VISITOR_IDS_INIT','B2_VISITOR_IDS_INIT','B3_VISITOR_IDS_INIT','B4_VISITOR_IDS_INIT','B5_VISITOR_IDS_INIT','B6_VISITOR_IDS_INIT','B7_VISITOR_IDS_INIT','B8_VISITOR_IDS_INIT','B9_VISITOR_IDS_INIT','B10_VISITOR_IDS_INIT']

building_index = [1,2,3,4,5,6,7,8,9,10]
#for building_id in range(1,11):
for building_id,reg_encod, reg_name_file, visit_encode, visit_name_file in zip(building_index,registered_encodings,reg_nameidlbl, visitor_encodings,visit_nameidlbl):
#Initalize the list for each building
	distance_list_build_i = []
	actual_event_build_i = []
	actual_List_build_i = []
	predicted_List_build_i = []
	prediction_status_build_i = []
	for i in random_numbers:
		#master_nameLabelMapDict = get_master()
		#Get registered occupants encodings then Name,id ,index details
		reg_encod_filepath = getattr(config, reg_encod)
		reg_file_name = getattr(config,reg_name_file)
		reg_nameidind_filepath = get_registered(reg_file_name)
		#Get visitor occupants encodings then Name,id ,index details
		visit_encod_filepath = getattr(config,visit_encode)
		visit_file_name = getattr(config,visit_name_file)
		visit_nameidind_filepath = get_visitor(visit_file_name)
		distance_list, actual_event, actual_List, predicted_List,prediction_status = get_distance(building_id,i,master_nameLabelMapDict,reg_encod_filepath, reg_nameidind_filepath, visit_encod_filepath, visit_nameidind_filepath)
		#distance_list_build_i.append(distance_list)
		#actual_event_build_i.append(actual_event)
		#actual_List_build_i.append(actual_List)
		#predicted_List_build_i.append(predicted_List)
		#prediction_status_build_i.append(prediction_status)
		with open(f"b{building_id}_distanceThreshold.csv", mode='a+', newline='') as csv_file:
			#for i,j,k,l,m in zip(distance_list_build_i, actual_event_build_i, actual_List_build_i, predicted_List_build_i,prediction_status_build_i):
			for i,j,k,l,m in zip(distance_list, actual_event, actual_List, predicted_List,prediction_status):
				csv_file.write("%s,%s,%s,%s,%s\n"%(i,j,k,l,m))
	print(" Iteration for building is over",building_id)

	#print("distance_list is \n",distance_list)
	#print("Actual event is \n",actual_event)
	#print("actual_List is \n",actual_List)
	#print("predicted_List is \n",predicted_List)
