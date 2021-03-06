"""
Represents a delivery truck which can hold and deliver packages.
"""

from packages import Package
from timeofday import Time
from address import Address
from locations import allLocations
from constants import SOD, MAX_PACKAGES, AVG_SPEED_MPM, truncate_to_tenth
import math

class Truck:
	#Constructs this object
	def __init__(self, id, startingLocation, controller):
		self.id = id
		self.totalDist = 0
		self.cargo = list()
		self.currentPackage = None
		self.location = startingLocation
		self.controller = controller
		self.status = "AT HUB"
		self.statusTracker = dict()
		self.destination = None
		self.eta = None
		self.start = Time.copy_time(SOD)

	#Loads the provided package onto this truck
	def load(self, p):
		if(p != None):
			if(len(self.cargo) >= MAX_PACKAGES):
				return False
			else:
				self.cargo.append(p)
				p.timeLoaded = Time.copy_time(self.controller.globalTime)
				p.truck = self.id
				return True
	
	#Delivers the provided package
	def deliver(self, package):
		self.currentPackage = package
		self.status = "MAKING DELIVERIES"
		self.destination = allLocations[package.dest]
		distToDest = self.location.distances[self.destination]
		self.totalDist += distToDest
		self.eta = Time.copy_time(self.controller.globalTime)
		self.eta.add_minutes(int(math.ceil(distToDest * (1 / AVG_SPEED_MPM))))
		self.location = None
	
	#Moves this truck to the hub from its current location
	def return_to_hub(self):
		self.destination = self.controller.hub
		distToDest = self.location.distances[self.destination]
		self.totalDist += distToDest
		self.eta = Time.copy_time(self.controller.globalTime)
		self.eta.add_minutes(int(math.ceil(distToDest * (1 / AVG_SPEED_MPM))))
		self.location = None
	
	#Checks the status of this truck and performs any status changes based on the time and its position
	def check_status(self):
		if(type(self.eta) != type(None)):
			if(self.eta == self.controller.globalTime or self.eta.is_before(self.controller.globalTime)):
				if(self.status == "RETURNING TO HUB"):
					self.status = "AT HUB"
					self.location = self.destination
					self.eta = None
					self.destination = None
				else:
					self.location = self.destination
					self.currentPackage.timeDelivered = Time.copy_time(self.controller.globalTime)
					self.controller.packagesDelivered += 1
					self.destination = None
					self.currentPackage = None
					self.eta = None
				self.make_deliveries()
			self.statusTracker[Time.copy_time(self.controller.globalTime)] = (self.totalDist, self.status)
		return self.status
	
	#Prints the status of this truck as of the provided time; if no time is provided, prints this trucks current status
	def print_status(self, timeOfReport):
		print("Truck #" + str(self.id))
		#Status as of right now
		if(timeOfReport == None):
			print("Time: EOD")
			if(self.location == self.controller.hub):
				print("Status: AT HUB")
			else:
				if(len(self.cargo) > 0):
					print("Status: MAKING DELIVERIES")
				else:
					print("Status: RETURNING TO HUB")
			print("Distance driven: " + str(truncate_to_tenth(self.totalDist)))
		#Status as of the provided report time
		else:
			print("Time: " + str(timeOfReport))
			closestTime = None
			for time in self.statusTracker:
				if(time.is_before(timeOfReport)):
					if(closestTime == None):
						closestTime = time
					else:
						if(time.is_after(closestTime)):
							closestTime = time
			if(closestTime != None):
				print("Status: " + self.statusTracker[closestTime][1])
				print("Distance driven: " + str(truncate_to_tenth(self.statusTracker[closestTime][0])))
			else:
				print("Status: AT HUB")
				print("Distance driven: 0.0")
	
	#Deliver all packages loaded on this truck in the order they are loaded
	def make_deliveries(self):
		if(len(self.cargo) > 0):
			self.status = "MAKING DELIVERIES"
			self.deliver(self.cargo.pop())
		elif(self.location != self.controller.hub):
			self.status = "RETURNING TO HUB"
			self.return_to_hub()
	
	#Returns the last package loaded onto this truck
	def last_package(self):
		if(len(self.cargo) > 0):
			return self.cargo[len(self.cargo) - 1]
		else:
			return None
	
	#Returns the hash value of this object
	def __hash__(self):
		return self.id % 1024
	
	#Returns a string representation of this object
	def __str__(self):
		string = "Truck #" + str(self.id) 
		return string