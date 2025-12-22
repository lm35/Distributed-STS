
from numpy import *
from matplotlib.pyplot import *
import argparse 
import pickle
from matplotlib import rc,rcParams
#from past.builtins import xrange
#from google.colab import files
#matplotlib inline
#import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2

def drawPlot(key_listInTp,zone_listInTp,Event_Counter,t):
	y_values = key_listInTp
	text_values = zone_listInTp
	
	#x_values = np.arange(1, len(text_values) + 1, 1)
	plt2.rcParams["font.weight"] = "bold"
	plt2.rcParams["axes.labelweight"] = "bold"	
	plt2.rcParams.update({'font.size': 15})
	fig = plt2.figure(figsize = (10, 5))
 	
	# creating the bar plot
	plt2.scatter(text_values,y_values, c ="pink", 
            linewidths = 2, 
            marker ="s", 
            edgecolor ="blue", 
            s = 150)
	plt2.xticks(fontsize=12,rotation = 10)
	plt2.yticks(fontsize=12)
	plt2.ylabel("Occupant ID")
	plt2.xlabel("Zones")
	plt2.title("Occupant location for building $b_{1}$ and $b_{2}$ at time %s"%t)
	matplotlib.pyplot.savefig('StateforEvent.jpg',dpi=300, edgecolor='b',transparent=True)
	#plt2.show()
	
	#plt2.line(x_values, y_values, align='center')
	# Decide which ticks to replace.
	#new_ticks = ["word for " + str(y) if y != 0.3 else str(y) for y in y_values]
	#plt2.yticks(y_values, new_ticks)
	#plt2.xticks(x_values, text_values)
	#plt2.show()

	
