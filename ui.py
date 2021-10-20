"""
Class which allows user to query to program with the console for status of 
trucks and packages
"""

from timeofday import Time
from package import Package
from truck import Truck
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
		print("NOTE: times must be entered in 24-hour format and include a leading '0' for times before 10:00")
		print("")
		self.prompt_query()
	
	def display_full_report(self):
		print("TODO")
	
	def display_error(self):
		print("Command not recognized.")
		print("List of valid commands:")
		self.display_help()
	
	def display_package(self, id, time):
		try:
			p = self.allPackages[id]
			print(str(p))
			p.print_status(time)
		except:
			print("No match found for package id #" + str(id))
		finally:
			print("")
			self.prompt_query()
	
	def display_truck(self, id, time):
		try:
			t = self.allTrucks[id]
			print(str(t))
			t.display_status(time)
		except KeyError:
			print("No match found for truck id #" + str(id))
		finally:
			print("")
			self.prompt_query()
	
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
				self.display_package(UserInterface.parse_id(query), UserInterface.parse_time(query))
			elif(re.search("^p[0-9]+$", query)):
				self.display_package(UserInterface.parse_id(query), None)
			else:
				self.display_error()
		elif(re.search("^t[0-9]+", query)):
			if(re.search("t[0-9]+ [0-9]{2}:[0-9]{2}", query)):
				self.display_truck(UserInterface.parse_id(query), UserInterface.parse_time(query))
			elif(re.search("^t[0-9]+$", query)):
				self.display_truck(UserInterface.parse_id(query), None)
			else:
				self.display_error()
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
	
	#Returns a copy of the provided set
	def copy_set(set):
		newSet = dict()
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