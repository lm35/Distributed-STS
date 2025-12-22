# Reading an excel file using Python
#import xlrd
import argparse
import csv
import pandas as pd
#import xlwt
import numpy as np
import sqlite3
import pickle
from datetime import datetime
from datetime import time
#from xlwt import Workbook
from csv import writer
from modules import drawKeyZone



def precisionRecall(stateMatrix, gtMatrix,occup_count,zone_count,theta_i,zoneOfOccr_name,zoneOfOccr,gt, occupLabel, event_counter,eventTimeDict,master_nameidList,master_indx_Labl_Dict, zoneList,zone_Dict,t,Id_to_track,event,track_id_toTrackDict):
	#print("State Matrix is  ",stateMatrix )
	tp=0
	fp=0
	fn=0
	tn = 0
	occup_id_Track = {} # To store the track of desired occupant ID passed as command-line argument
	key_listInTp = []
	zone_listInTp = []
	zone_Name = []
	time_listInTp = []
	new_zoneName = [] # Rename transit name to building corresponding transit name
	headers = ['Event','theta', 'tp', 'fp', 'fn', 'tn', 'Prec', 'Rec']
	j=0
	sort_list = []
	dictMat = {}
	theta_zero_counter = 0
	OccupPresent_List = []
	if(zoneOfOccr_name[0:7]!='transit'):
		if (theta_i == 0):
			for j in range (0,occup_count):
				for i in range (0,zone_count):
					if ((gtMatrix[i][j]) == 1):
						if(zoneList[i][0:7]=='transit'): #If the zone corresponding to index 'i' is a transition zone then neglect the high probability
							flag_theta_0 = 0
						else:
							tp = tp+1  # Count of true positive for a particular state for varying theta(0 - 1)
							fp = occup_count-tp # Gt is '0', but state prob >= theta
							fn = 0
			tn = 0
		else:
			for j in range (0,occup_count): # Take jth occupant
				#print("master_indx_Labl_Dict[str(10)]",master_indx_Labl_Dict[str(10)])
				for i in range (0,zone_count): #Find values for each zone
					#print("master_indx_Labl_Dict[str(j)][0:3] is   ",master_indx_Labl_Dict[str(j)][0:2])
					#if(master_indx_Labl_Dict[str(j)][0:3] == 'o_1'):
					for k in range(0, zone_count):
						sort_list.append(stateMatrix[k][j])
						sort_list.sort()
						max_prob = sort_list[-1]
					#elif(master_indx_Labl_Dict[str(j)][0:3] == 'o_2'):
					#	for k in range(9, 17):
					#		sort_list.append(stateMatrix[k][j])
					#	sort_list.sort()
					#	max_prob = sort_list[-1]
					#elif(master_indx_Labl_Dict[str(j)][0:3] == 'o_3'):
					#	for k in range(18, 26):
					#		sort_list.append(stateMatrix[k][j])
					#	sort_list.sort()
					#	max_prob = sort_list[-1]
					#else:
					#	flag_max_prob = 0
					#print("Max Prob is max prob, sort list [-1]",max_prob,sort_list[-1])
					#print("gtMatrix[{}][{}]) value is {}  ".format(i,j,gtMatrix[i][j]))
					sort_list.clear()
					#if (gtMatrix[i][j]) == 1 and (zoneList[i][0:7]=="transit") and (stateMatrix[i][j]>= theta_i):# inverse of  as (gtMatrix[i][j]) == 0 and (zoneList[i][0:7]!="transit") and (stateMatrix[i][j]< theta_i, will give you tn = tn+1 for all zones other than transition. To avoid adding up 1 to tn many times for a single occupant we consider the reverse scenario that occurs only once
					#	tn = tn+1
					#	print("For occupant j = {} and  zone i = {} stateMatrix = {} : gtMatrix = {} : theta_i = {} event_counter = {} and t ={} and zone is = {}".format(j,i, stateMatrix[i][j],gtMatrix[i][j],theta_i,event_counter,t,zoneList[i][0:6]))
					#	print("True Positivei -= ",tp)
					#	print("For occupant with TRUE Negative is {} at j = {} and  zone i = {} stateMatrix = {} : gtMatrix = {} : theta_i = {} event_counter = {} and t ={} and zone is = {}".format(master_indx_Labl_Dict[str(j)],j,i, stateMatrix[i][j],gtMatrix[i][j],theta_i,event_counter,t,zoneList[i][0:7]))

					if(gtMatrix[i][j]) == 1 and (zoneList[i][0:7]!="transit") and (stateMatrix[i][j]>= theta_i) and stateMatrix[i][j] == max_prob: # False +ve :- Prob > theta & GT = 0
						#if(stateMatrix[i][j]>= theta_i):
						tp = tp+1
						#print("For occupant with True positive is {} at j = {} and  zone i = {} stateMatrix = {} : gtMatrix = {} : theta_i = {} event_counter = {} and t ={} and zone is = {}".format(master_indx_Labl_Dict[str(j)],j,i, stateMatrix[i][j],gtMatrix[i][j],theta_i,event_counter,t,zoneList[i][0:7]))
						if master_indx_Labl_Dict[str(j)] == Id_to_track :
							track_id_toTrackDict.update({t:str(zoneList[i])})
					elif(gtMatrix[i][j]) == 1 and (zoneList[i][0:7]!="transit") and (stateMatrix[i][j] < theta_i):
						fn = fn+1
						#print("For occupant with False Negative is {} at j = {} and  zone i = {} stateMatrix = {} : gtMatrix = {} : theta_i = {} event_counter = {} and t ={} and zone is = {}".format(master_indx_Labl_Dict[str(j)],j,i, stateMatrix[i][j],gtMatrix[i][j],theta_i,event_counter,t,zoneList[i][0:7]))
					#	else:
					#		flag_not_Transitb = 1
					elif(gtMatrix[i][j]) == 0 and (zoneList[i][0:7]!="transit")  and (stateMatrix[i][j] >= theta_i):
						#if(stateMatrix[i][j] == max_prob and stateMatrix[i][j] >= theta_i):
						fp = fp+1
						#print("For occupant with False Positive is {} at j = {} and  zone i = {} stateMatrix = {} : gtMatrix = {} : theta_i = {} event_counter = {} and t ={} and zone is = {}".format(master_indx_Labl_Dict[str(j)],j,i, stateMatrix[i][j],gtMatrix[i][j],theta_i,event_counter,t,zoneList[i][0:7]))

					else:
						no_flag = 0
	else:
		print("Zone of occur is ",zoneOfOccr_name[0:7])
		tp = 0
		fp = 0
		fn = 0
		tn = 0
	#print("event--- {} ,theta==== {}, tp----- {}, fp--- {}, fn----- {}".format(event_counter,theta_i,tp, fp, fn))
	OccupPresent_List = list(dict.fromkeys(OccupPresent_List))
	#print("OccupPresent in bulding b1 are {} for theta {} at time {}".format(OccupPresent_List,theta,eventTimeDict['e'+str(event_counter)]))
	with open('Track_'+str(Id_to_track)+'_CSTS.csv', 'a+', newline='') as file:
		for key in occup_id_Track.keys():
			file.write("%s,%s\n"%(key,occup_id_Track[key]))
	print("Value of tp is {} fp {} fn {} tn {} for event {} ".format(tp,fp,fn,tn,event_counter))
	if (tp != 0):
		precision = tp/(tp+fp)
		recall = tp/(tp+fn)
		specificity = 0
	else:
		precision = 0
		recall = 0
		specificity = 0

	if (theta_i == 0.7) and event_counter == 87 :
		for zone in zone_listInTp:
			for key in zone_Dict.keys():
				#print("Keys in zone_Dict are",key)
				if(str(key) == zone):
					zone_Name.append(key)
		#print("key_listInTp,zone_listInTp",key_listInTp,zone_listInTp,zone_Name)
		#for i in range (0:len(zone_Name):
		for zone_i, occup_i in zip(zone_listInTp,key_listInTp):
			#print("occup_i[0:2]",occup_i[0:2], zone_i)
			if zone_i == 'transit_1' and occup_i[0:3]=='o_2':
				#print("occup_i[0:2]",occup_i[0:3])
				check_i = 'transit_2'
				new_zoneName.append(check_i )
			elif (zone_i == 'transit_1' and occup_i[0:3]=='o_3'):
				check_i = 'transit_3'
				new_zoneName.append(check_i )
			else:
				new_zoneName.append(zone_i)
		#print("key_listInTp,new_zoneName,",key_listInTp,new_zoneName,zone_Name)
		drawKeyZone.drawPlot(key_listInTp,new_zoneName,event_counter,t)
	dictMat.clear()
	dictMat['Event'] = event_counter
	dictMat['theta'] = theta_i
	dictMat['tp'] = tp
	dictMat['fp'] = fp
	dictMat['fn'] = fn
	dictMat['tn'] = tn
	dictMat['Prec'] = precision
	dictMat['Rec'] = recall
	with open('tpfpfntn_1802.csv', 'a+', newline='') as file:
		writer = csv.DictWriter(file, fieldnames = headers)
		#writer.writeheader()
		writer.writerow(dictMat)
	#print("For theta = {} Precision: {} Recall: {}".format(theta,precision, recall))
	return precision, recall, specificity,track_id_toTrackDict
