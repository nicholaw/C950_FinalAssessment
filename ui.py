"""
Class which allows user to query to program with the console for status of 
trucks and packages
"""

import re

class UserInterface:
	def __init__(self, packages, trucks):
		self.allPackages = UserInterface.copy_set(packages)
		self.allTrucks = UserInterface.copy_set(trucks)
	
	def prompt_query(self):
		query = input(">>")
		self.parse_query(query)
	
	def display_help(self):
		print("p[id] [HH:mm]\tDisplay info for the package with the provided package id at the provided time.")
		print("\t\t   If time is omitted, displays info at EOD.")
		print("t[id] [HH:mm]\tDisplay info for the truck with the provided truck id at the provided time.")
		print("\t\t   If time is omitted, displays info at EOD.")
		print("fullreport\tDisplay info for all trucks and packages at end-of-day.")
		print("help\t\tDisplay a list of  valid commands.")
		print("exit\t\tTerminate the application.")
		print("")
		self.prompt_query()
	
	def display_full_report(self):
		print("TODO")
	
	def display_error(self):
		print("Command not recognized.")
		print("List of valid commands:")
		self.display_help()
	
	def parse_query(self, query):
		query = query.lower()
		query = query.rstrip()
		if(query == "fullreport"):
			self.display_full_report()
		elif(query == "exit"):
			self.exit()
		elif(query ==  "help"):
			self.display_help()
		elif(re.search("^p[0-9]+", query)):
			if(re.search("p[0-9]+ [0-9]{2}:[0-9]{2}", query)):
				print("DISPLAY specific time")
				self.prompt_query()
			elif(re.search("^p[0-9]+$", query)):
				print("Display eod")
				self.prompt_query()
			else:
				self.display_error()
		elif(re.search("^t[0-9]+", query)):
			print("TRUCK!")
			self.prompt_query()
		else:
			self.display_error()
	
	def start(self):
		print("------------------------------------------------------------------------------")
		print("Welcome to the user interface!")
		print("Please enter one of the following commands...")
		print("------------------------------------------------------------------------------")
		self.display_help()
	
	def exit(self):
		return
	
	def copy_set(set):
		newSet = dict()
		for item in set:
			newSet[item] = item
		return newSet