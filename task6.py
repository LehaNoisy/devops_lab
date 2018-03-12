#!/usr/bin/python

import platform
import sys
import os
import site
import distutils.sysconfig
import json
import yaml
import pip


packages = sorted(["%s==%s" % (i.key, i.version) for i in pip.get_installed_distributions()])


class Myclass:
	"""Class param"""
	#Evoke params
	def params(self):
		self.version = str(platform.python_version())
		self.virtenv = str(sys.prefix)
		self.exect_loc = str(sys.executable)
		self.pip = str(pip.__path__)
		self.pythonpath = str(sys.path) 
		self.packages = str(packages)
		self.pack_loc = str(os.path.dirname(os.__file__) + '/site-packages')
	
	def getPipLocation(self):
		return site.getsitepackages()
	
	#Write data to json file
	def write_json(self):
		self.params()
		data = {
		"Version :" : str(self.version),
		"Virtual environment:" : str(self.virtenv),
		"Python executable location: " : str(self.exect_loc),
		"Pip location:" : str(self.pip),
		"PYTHONPATH:" : str(self.pythonpath),
		"Installed packages:" : str(self.packages),
		"Site-packages location:" : str(self.pack_loc),	
		}	
		with open("data.json", "a") as js:
			json.dump(data, js)
			js.write("\n")
		print("Congratulations!")
		print("json create")

	#Write data to yaml file
	def write_yuml(self):
		self.params()
		data = {
		"Version :" : str(self.version),
		"Virtual environment:" : str(self.virtenv),
		"Python executable location: " : str(self.exect_loc),
		"Pip location:" : str(self.pip),
		"PYTHONPATH:" : str(self.pythonpath),
		"Installed packages:" : str(self.packages),
		"Site-packages location:" : str(self.pack_loc),	
		}	
		with open('data.yaml', 'w', encoding='utf8') as outfile:
			yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)
		print("yuml create")
	


c1=Myclass()
c1.write_json()
c1.write_yuml()

