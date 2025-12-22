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


def toCSV(s_K_Matrix, occup_count, zone_count, zone_Dict, Event_Counter, eventTimeDict, nameidList, indx_Labl_Dict, zoneList, t, zoneOfOccr,staterelation_outpath,state_Estimated):
	print("Writing state relation foe event", Event_Counter)
	#staterelation_outpath = config.WHOLE_STATE_RELATION_ESTIMATED
	#state_Estimated = config.ESTIMATED_STATE
	with open(staterelation_outpath, 'a+', newline='') as f:
		time_part = t.split(" ")[1]
		for j in range (0,occup_count):
        #print("occup_count is  ",occup_count)
			for i in range (0,zone_count):
				f.write("%s,%s,%s,%f\n"%(time_part, indx_Labl_Dict[str(j)], zoneList[i], s_K_Matrix[i][j]))
	#----------------Save Estimated State ------------------------
	with open(state_Estimated, 'a+', newline='') as file2:
		for j in range (0,occup_count):
			#print("occup_count is  ",occup_count)
			for i in range (0,zone_count):
				file2.write("%f "%(s_K_Matrix[i][j]))
			file2.write("\n")
