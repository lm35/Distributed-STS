# Standard library imports
#import xlrd
import argparse
import csv
import sqlite3
import pickle
import time

#Thirdparty library import
from csv import writer
import pandas as pd
#import xlwt
import numpy as np
from datetime import datetime
from datetime import time
from operator import add
from modules import config
#from xlwt import Workbook


def toCSV(gtmat, occup_count, zone_count, zone_Dict, Event_Counter, eventTimeDict, nameidList, indx_Labl_Dict, zoneList, t, zoneOfOccr,staterelation_GT_outpath, state_GT):
	#staterelation_GT_outpath = config.SR_GT_CSTS
	#state_GT = config.GROUNDTRUTH_STATE
	#--------------Write State Relation-----------
	with open(staterelation_GT_outpath, 'a+', newline='') as f:
		time_part = t.split(" ")[1]
		for j in range (0,occup_count):
        		#print("Ground Truth occup_count j is  ",j)
        		for i in range (0,zone_count):
        			#print("Ground Truth zone_count is  ",i)
        			f.write("%s,%s,%s,%f\n"%(time_part, indx_Labl_Dict[str(j)], zoneList[i], gtmat[i][j]))
	#----------------Save Ground Truth  State ------------------------
	with open(state_GT, 'a+', newline='') as file2:
		for j in range (0,occup_count):
        #print("occup_count is  ",occup_count)
			for i in range (0,zone_count):
				file2.write("%f "%(gtmat[i][j]))
			file2.write("\n")
