#!/usr/bin/python
import psutil
import os
import time
import json
import task3_config

class Myclass:
	"""Class param"""
	#Counter
	def __init__(self):
		self.counter = 0	

	def params(self):
		self.ram = str(psutil.virtual_memory().percent)
		self.us = str(psutil.virtual_memory().used)
		self.percent = str(psutil.cpu_percent())
		self.io = str(psutil.disk_io_counters())
		self.net = str(psutil.net_io_counters())
		self.date = str(time.ctime())
	
	
	#Write data to txt file
	def write_txt(self):
	    """Write data to txt file"""
	    self.params()
	    self.counter += 1
	    f = open('testfile.txt', 'a')
	    f.write ("SNAPSHOT " + str(self.counter) + "\n")
	    f.write ("DATE: " + (time.ctime()) + "\n" + "\n")
	    f.write ("CPU_Load: " + self.percent + "\n")
	    f.write ("Memory usage: " + self.us+ "\n")
	    f.write ("Virtual memory usage: " + self.ram+ "\n")
	    f.write ("IO Information: " + self.io+ "\n")
	    f.write ("Network Information: " + self.net+ "\n" + "\n" + "\n" + "\n")
	    f.close()
	    print(str(self.counter) + " file create")


	#Write data to json file
	def write_json(self):
		"""Write data to json file"""
		self.params()
		self.counter += 1
		data = { 
		"SNAPSHOT" : str(self.counter),
		"DATE" : time.ctime(),
		'CPU_Load' : self.percent,
		'Memory usage' : self.us,
		'Virtual memory usage' : self.ram,
		'IO Information' : self.io,
		'Network Information:' : self.net,
		}
		with open("data.json", "a") as js:
			json.dump(data, js, indent = 4, ensure_ascii = False)
			js.write("\n")
			print(str(self.counter) + " json create")
		
	    
#evoke a class
c1=Myclass()


while True: 	
	if task3_config.exit == "txt":
		c1.write_txt()
	else: 
		c1.write_json()
	time.sleep(task3_config.value*60)


