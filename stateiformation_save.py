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
import drawKeyZone



def precisionRecall(stateMatrix, gtMatrix,occup_count,zone_count,theta_i,zoneOfOccr_name,zoneOfOccr,gt, occupLabel, event_counter,eventTimeDict,master_nameidList,master_indx_Labl_Dict, zoneList,zone_Dict,t,Id_to_track,event):
	print("State Matrix is  ",stateMatrix )
	occup_id_Track = {} # To store the track of desired occupant ID passed as command-line argument
	key_listInTp = []
	zone_listInTp = []
	zone_Name = []
	time_listInTp = []
	new_zoneName = [] # Rename transit name to building corresponding transit name
	j=0
	sort_list = []
	dictMat = {}
	theta_zero_counter = 0
	OccupPresent_List = []
	for j in range (0,occup_count): # Take jth occupant
		#print("master_indx_Labl_Dict[str(10)]",master_indx_Labl_Dict[str(10)])
		for i in range (0,zone_count): #Find values for each zone
			#print("i is ",i)
			if(master_indx_Labl_Dict[str(j)][0:2] == 'o_1'):
				for k in range(0, 8):
					sort_list.append(stateMatrix[k][j])
				sort_list.sort()
				max_prob = sort_list[-1]
			elif(master_indx_Labl_Dict[str(j)][0:2] == 'o_2'):
				for k in range(9, 17):
					sort_list.append(stateMatrix[k][j])
				sort_list.sort()
				max_prob = sort_list[-1]
			elif(master_indx_Labl_Dict[str(j)][0:2] == 'o_3'):
				for k in range(18, 26):
					sort_list.append(stateMatrix[k][j])
				sort_list.sort()
				max_prob = sort_list[-1]
			else:
				flag_max_prob = 0
			sort_list.clear()
			if(stateMatrix[i][j]>= 0.9) and (stateMatrix[i][j] == max_prob)  and (gtMatrix[i][j]) == 1 :# True +ve :- Prob > theta & GT = 1
				if(zoneList[i][0:7]=='transit'):
					flag_tp = 0
				else:
					print("For occupant with tp is {} at j = {} and  zone i = {} stateMatrix = {} : gtMatrix = {} : theta_i = {} event_counter = {} and t ={} and zone is = {}".format(master_indx_Labl_Dict[str(j)],j,i, stateMatrix[i][j],gtMatrix[i][j],theta_i,event_counter,t,zoneList[i][0:6]))
					tp = tp+1  # Count of true positive for a particular state for varying theta(0 - 1)

				OccupPresent_List.append(master_indx_Labl_Dict[str(j)])
				key_listInTp.append(master_indx_Labl_Dict[str(j)])
				zone_listInTp.append(zoneList[i])
				time_listInTp.append(t)
				#Get location of the occupant to be tracked
				if master_indx_Labl_Dict[str(j)] == Id_to_track:
					flag_tp = 0
				if master_indx_Labl_Dict[str(j)] == Id_to_track and theta_i == 0.9 and i == int(zoneOfOccr) and (gtMatrix[i][j]) == 1:
					occup_id_Track[t] = zoneList[int(zoneOfOccr)]
			elif(stateMatrix[i][j]>= theta_i) and (stateMatrix[i][j] == max_prob) and (gtMatrix[i][j]) == 0 : # False +ve :- Prob > theta & GT = 0
				if(zoneList[i][0:7]=='transit'):
					flag_fp = 0
				else:
					print("Event is ",event)
					print("For false positive occupant identified as {} , j = {} and  zone i = {} stateMatrix = {} : gtMatrix = {} : theta_i = {} event_counter = {} and t ={} and zone is = {}".format(master_indx_Labl_Dict[str(j)],j,i, stateMatrix[i][j],gtMatrix[i][j],theta_i,event_counter,t,zoneList[i][0:6]))
				fp = fp+1  # Count of false positive for a particular state for varying theta(0 - 1)
				OccupPresent_List.append(master_indx_Labl_Dict[str(j)])
				if master_indx_Labl_Dict[str(j)] == Id_to_track and theta_i == 0.9 and i == int(zoneOfOccr) and (gtMatrix[i][j]) == 1:
					occup_id_Track[t] = zoneList[int(zoneOfOccr)]
			elif((stateMatrix[i][j]< theta_i) and (stateMatrix[i][j] == max_prob) and (gtMatrix[i][j]) == 1) or ((stateMatrix[i][j]< theta_i) and (gtMatrix[i][j]) == 1) : # False -ve :- Prob < theta & GT = 1
				if(zoneList[i][0:7]=='transit'):
					flag_fn = 0
				else:
					print("For false negative occupant j = {} and  zone i = {} stateMatrix = {} : gtMatrix = {} : theta_i = {} event_counter = {} and t ={} and zone is = {}".format(j,i, stateMatrix[i][j],gtMatrix[i][j],theta_i,event_counter,t,zoneList[i][0:6]))
					fn = fn+1  # Count of false negative for a particular state for varying theta(0 - 1)
			elif(stateMatrix[i][j]< theta_i) and (stateMatrix[i][j] == max_prob) and (gtMatrix[i][j]) == 0 :# True -ve :- Prob < theta & GT = 0
				print("For TRUE negative occupant j = {} and  zone i = {} stateMatrix = {} : gtMatrix = {} : theta_i = {} event_counter = {} and t ={} and zone is = {}".format(j,i, stateMatrix[i][j],gtMatrix[i][j],theta_i,event_counter,t,zoneList[i][0:6]))
				tn = tn+ 1 # Count of true negative for a particular state for varying theta(0 - 1)
			else:
				no_flaf = 0
	OccupPresent_List = list(dict.fromkeys(OccupPresent_List))
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
	with open('tpfpfntn.csv', 'a+', newline='') as file:
		writer = csv.DictWriter(file, fieldnames = headers)
		#writer.writeheader()
		writer.writerow(dictMat)
	#print("For theta = {} Precision: {} Recall: {}".format(theta,precision, recall))
	return precision, recall, specificity
