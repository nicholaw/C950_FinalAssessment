"""
Class which allows user to query to program with the console for status of 
trucks and packages
"""

from timeofday import Time
from package import Package
from truck import Truck
import re

class UserInterface:
	def __init__(self, packages, trucks, controller):
		self.allPackages = UserInterface.copy_set(packages)
		self.allTrucks = UserInterface.copy_set(trucks)
		self.controller = controller
	
	def prompt_query(self):
		query = input(">>")
		self.parse_query(query)
	
	def display_help(self):
		print("p[id] [HH:mm]\tDisplay info for the package with the specified package id at the provided time.")
		print("\t\t   If time is omitted, displays info at EOD.")
		print("pall [HH:mm]\tDisplay info for all packages at the specified time.")
		print("\t\t   If time is omitted, displays info at EOD.")
		print("t[id] [HH:mm]\tDisplay info for the truck with the specified truck id at the provided time.")
		print("\t\t   If time is omitted, displays info at EOD.")
		print("tall [HH:mm]\tDisplay info for all truks at the specified time.")
		print("\t\t   If time is omitted, displays info at EOD.")
		print("fullreport\tDisplay info for all trucks and packages at end-of-day.")
		print("help\t\tDisplay a list of  valid commands.")
		print("exit\t\tTerminate the application.")
		print("NOTE: times must be entered in 24-hour format and include a leading '0' for times before 10:00")
	
	def display_full_report(self):
		self.controller.print_stats()
	
	def display_error(self):
		print("Command not recognized.")
		print("List of valid commands:")
		self.display_help()
	
	def display_package(self, id, time):
		try:
			self.allPackages[id].print_status(time)
		except KeyError:
			print("No match found for package id #" + str(id))
	
	def display_truck(self, id, time):
		try:
			self.allTrucks[id].print_status(time)
		except KeyError:
			print("No match found for truck id #" + str(id))
	
	def parse_query(self, query):
		query = query.lower()
		query = query.rstrip()
		if(query == "fullreport"):
			self.display_full_report()
		elif(query == "exit"):
			return
		elif(query ==  "help"):
			self.display_help()
		elif(re.search("^p[0-9]+", query)):
			if(re.search("p[0-9]+ [0-9]{2}:[0-9]{2}$", query)):
				self.display_package(UserInterface.parse_id(query), UserInterface.parse_time(query))
			elif(re.search("^p[0-9]+$", query)):
				self.display_package(UserInterface.parse_id(query), None)
			else:
				self.display_error()
		elif(re.search("^t[0-9]+", query)):
			if(re.search("t[0-9]+ [0-9]{2}:[0-9]{2}$", query)):
				self.display_truck(UserInterface.parse_id(query), UserInterface.parse_time(query))
			elif(re.search("^t[0-9]+$", query)):
				self.display_truck(UserInterface.parse_id(query), None)
			else:
				self.display_error()
		elif(re.search("^pall", query)):
			if(re.search("^pall$", query)):
				for pid in self.allPackages:
					self.display_package(pid, None)
					print("")
			elif(re.search("pall [0-9]{2}:[0-9]{2}$", query)):
				for pid in self.allPackages:
					self.display_package(pid, UserInterface.parse_time(query))
					print("")
			else:
				self.display_error
		elif(re.search("^tall", query)):
			if(re.search("^tall$", query)):
				for tid in self.allTrucks:
					self.display_truck(tid, None)
					print("")
			elif(re.search("tall [0-9]{2}:[0-9]{2}$", query)):
				for t in self.allTrucks:
					self.display_truck(self.allTrucks[t].id, UserInterface.parse_time(query))
					print("")
			else:
				self.display_error
		else:
			self.display_error()
		print("")
		self.prompt_query()
	
	def start(self):
		print("------------------------------------------------------------------------------")
		print("Welcome to the user interface!")
		print("Please enter one of the following commands...")
		print("------------------------------------------------------------------------------")
		self.display_help()
		print("")
		self.prompt_query()
	
	#Returns a copy of the provided set
	def copy_set(set):
		newSet = dict()
		if(type(set) == type(newSet)):
			for item in set:
				try:
					newSet[item] = set[item]
				except AttributeError:
					print("Unable to copy " + str(item) + " into UI dictionary")
		else:
			for item in set:
				try:
					newSet[item.id] = item
				except AttributeError:
					print("Unable to copy " + str(item) + " into UI dictionary")
		return newSet
	
	#Returns a time from the provided string assuming the last five characters of the string represent the time
	def parse_time(timeString):
		string = ""
		index = len(timeString) - 5
		while(index < len(timeString)):
			string += timeString[index]
			index += 1
		return Time.of(string)
	
	#Returns an integer id from the provided string assuming the id starts at the second character and is delimited by a whitespace
	def parse_id(idString):
		string = ""
		index = 1
		while(idString[index] != " "):
			string += idString[index]
			index += 1
			if(index >= len(idString)):
				break
		return int(string)