# import necessary libraries
#import xlrd
import argparse
import csv
import pandas as pd
import numpy as np
import sqlite3
import pickle
from datetime import datetime
from datetime import time
from csv import writer
from collections import defaultdict
from operator import add
from  modules import config
import os

def get_estimatedoccup(state_current, state_previous, nameList, namLablDict, Event_Counter,t, zoneOfOccr,outfile):
    result_list = [a - b for a, b in zip(state_current,state_previous)]
    maxindex_result_list = result_list.index(max(result_list))
    print("result_list",result_list)
    eventtrigr_occup = nameList[maxindex_result_list]
    eventtrigr_occup_id = namLablDict[eventtrigr_occup]
    print(eventtrigr_occup, Event_Counter,eventtrigr_occup_id)
    data_to_append =  [t, zoneOfOccr, eventtrigr_occup, eventtrigr_occup_id,state_current[maxindex_result_list]]
    # Append to CSV file
#    outfile = config.ESTIMATED_OCCUPANTS
    with open(outfile, mode='a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_to_append)
    return
