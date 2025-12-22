#Generate an index for each image in GT. This ensures that the image picked up for an event remains the same in CSTS and DSTS
# import the necessary packages
import pickle
import cv2
import numpy as np
import csv
import time
from collections import Counter
import random
import os
import config

#Get the number of images for each occupant
def getcount_testimage(string_list):
	string_counts = Counter(string_list)
	stringCounter_dict = {}
	for string, count in string_counts.items():
		print(f"{string}: {count}")
		stringCounter_dict.update({str(string):count})
	return stringCounter_dict


#Get index for the current images
def get_indexcurrent(gtnamekey_list, gtnamekey_dict, counteachimage_dict):
	for occup in gtnamekey_list:
		gtnamekey_dict[str(occup)] = []
		n_4rand = int(counteachimage_dict[str(occup)])
		#print("n_4rand is",n_4rand)
		while len(gtnamekey_dict[str(occup)]) <n_4rand:
			#print("len(gtnamekey_dict[str(occup)]) is", len(gtnamekey_dict[str(occup)]))
			random_number = random.randint(1, n_4rand)
			if random_number not in gtnamekey_dict[str(occup)]:
				gtnamekey_dict[str(occup)].append(random_number)
	return gtnamekey_dict

#Get the no. of images for each occupant in movement, each image corresponds to an event (if  13 images for an Ocup in movement, then 13 events will be there for that Occup in GT)
#We maintain unique images, so as to get unique events
gt_test_pickle = config.TEST_ENCODINGS  # Update with your actual file path

# Load the test image pickle file before accessing it
with open(gt_test_pickle, "rb") as file:
    gt_test_data = pickle.load(file)  # Now it's a dictionary

print("gt_test_pickle is", gt_test_data)
counteachimage_dict = getcount_testimage(gt_test_data["Cntralzd_GTNames"])
print("Count of each images is ", counteachimage_dict)
gtnamekey_list = list(set(gt_test_data["Cntralzd_GTNames"])) #Name of occuants in GT track, convert that into a list
gtnamekey_dict = {}
print("gtnamekey_dict  ",gtnamekey_list)
#Initialize a dictionary with key as GT track occupant names
for key in gtnamekey_list:
	gtnamekey_dict[str(key)] = []
index_currentimage_dict = get_indexcurrent(gtnamekey_list, gtnamekey_dict, counteachimage_dict)
print("index_currentimage_dict is ", index_currentimage_dict)

#data = {"b2_DataEncodings": knownEncodings, "b2_DataNames": knownNames}
output_path = config.OCCUPANT_INDEX_LIST_FOREACHBUILD
#index_pickle = 'random_indexperFullGT.pickle'
if os.path.exists(output_path):
    os.remove(output_path)
file_pickle = open(output_path, "wb")
file_pickle.write(pickle.dumps(index_currentimage_dict))
file_pickle.close()
indexPool = pickle.loads(open(output_path, "rb").read())
print("IndexPool is",indexPool)
#write this to a csv file
with open("output_index.csv", 'w', newline='') as f:
    for key in index_currentimage_dict.keys():
        f.write("%s,%s\n"%(key,index_currentimage_dict[key]))
