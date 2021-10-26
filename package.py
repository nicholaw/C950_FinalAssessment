"""
Represents a package which can be loaded onto a truck and delivered to a location
"""

from address import Address
from timeofday import Time

class Package:
	def __init__(self, id):
		self.id = id
		self.dest = None
		self.available = Time.of("08:00")
		self.deadline = None
		self.timeLoaded = None
		self.timeDelivered = None
		self.mass = 1
		self.note = ''
		self.truck = -1
		self.group = set()
	
	def print_status(self, timeOfReport):
		print("Package #" + str(self.id))
		#print the status of this package as of right now
		if(timeOfReport == None):
			print("Time: EOD")
			if(self.timeDelivered != None):
				print("Status: DELIVERED")
				print("Time of delivery: " + str(self.timeDelivered))
				print("Delivered by truck #" + str(self.truck))
			elif(self.timeLoaded != None):
				print("Status: EN ROUTE")
				print("Time of loading: " + str(self.timeLoaded))
				print("Loaded aboard truck #" + str(self.truck))
			else:
				print("Status: AT HUB")
		#print the status of this package as of the provided time
		else:
			print("Time: " + str(timeOfReport))
			if(timeOfReport.is_before(self.timeLoaded) or self.timeLoaded == None):
				print("Status: AT HUB")
			elif(timeOfReport.is_before(self.timeDelivered) or self.timeDelivered == None):
				print("Status: EN ROUTE")
				print("Time of loading: " + str(self.timeLoaded))
				print("Loaded aboard truck #" + str(self.truck))
			else:
				print("Status: DELIVERED")
				print("Time of delivery: " + str(self.timeDelivered))
				print("Delivered by truck #" + str(self.truck))

	def __str__(self):
		string = "Package #" + str(self.id) + "\n"
		string += (str(self.dest) + "\n")
		return string

	def __hash__(self):
		return ((self.id * 5867) % 128)

	def __eq__(self, other):
		if(type(self) != type(other)):
			return False
		return (self.id == other.id)