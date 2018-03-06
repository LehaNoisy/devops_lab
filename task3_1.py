#!/usr/bin/python
import psutil
import os
import time
import json

class Myclass(object):
	"""Class parametrs"""	
	def __init__(self):
		self.ram = psutil.virtual_memory().percent
		self.us = psutil.virtual_memory().used
		self.percent = psutil.cpu_percent() 
		self.io = psutil.disk_io_counters()
		self.net = psutil.net_io_counters() 
	
	#Write data to txt file
	def write_txt(self):
	    """Write data to txt file"""
	    f = open('testfile.txt', 'w')
	    f.write ("SNAPSHOT")
	    f.write ("CPU_Load: " + percent1 + "\n")
	    f.write ("Memory usage: " + us1+ "\n")
	    f.write ("Virtual memory usage: " + ram1+ "\n")
	    f.write ("IO Information: " + io1+ "\n")
	    f.write ("Network Information: " + net1+ "\n")
	    f.close()


	#Write data to json file
	def write_json(self):
	    """Write data to json file"""
	    data = {
	    'CPU_Load' : percent1,
	    'Memory usage' : us1,
	    'Virtual memory usage' : ram1,
	    'IO Information' : io1,
	    'Network Information:' : net1,
	    }
	    with open('data.json', 'w') as outfile:
	    	json.dump(data, outfile)
	    


ram1 = str(psutil.virtual_memory().percent)
us1 = str(psutil.virtual_memory().used)
percent1 = str(psutil.cpu_percent())
io1 = str(psutil.disk_io_counters())
net1 = str(psutil.net_io_counters())

#Add time
time1= time.strftime("%H:%M:%S")

#print("Current Time", time.strftime("%H:%M:%S"),)
print(time1)

#print lines
print("CPU Load:  ", percent1)
print("Memory usage:  ", us1 )
print("Virtual memory usage:  ", ram1 , "%" )
print("IO Information:  ", io1  )
print("Network Information:  ", net1)



c1=Myclass()
c1.write_txt();
c1.write_json()


