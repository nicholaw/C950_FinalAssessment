"""
Represents a delivery truck which can hold and deliver packages.
"""

from packages import Package
from timeofday import Time
from address import Address
from locations import allLocations
from constants import MAX_PACKAGES, AVG_SPEED_MPM
import math

#Define the Truck class
class Truck:
	def __init__(self, id, startingLocation, controller):
		self.id = id
		self.totalDist = 0
		self.cargo = list()
		self.currentPackage = None
		self.location = startingLocation
		self.controller = controller
		self.status = "At hub"
		self.destination = None
		self.eta = None

	def load(self, p):
		if(len(self.cargo) >= MAX_PACKAGES):
			return False
		else:
			self.cargo.append(p)
			p.status = "Out for delivery"
			return True
	
	def deliver(self, package):
		self.currentPackage = package
		self.status = "Delivering package #" + str(package.id)
		self.destination = allLocations[package.dest]
		distToDest = self.location.distances[self.destination]
		self.totalDist += distToDest
		self.eta = Time.copy_time(self.controller.globalTime)
		self.eta.add_minutes(int(math.ceil(distToDest * (1 / AVG_SPEED_MPM))))
		self.location = None
    
	def return_to_hub(self):
		self.status = "Returning to hub"
		self.destination = self.controller.hub
		distToDest = self.location.distances[self.destination]
		self.totalDist += distToDest
		self.eta = Time.copy_time(self.controller.globalTime)
		self.eta.add_minutes(int(math.ceil(distToDest * (1 / AVG_SPEED_MPM))))
		self.location = None
	
	def check_status(self):
		if(type(self.eta) != type(None)):
			if(self.eta == self.controller.globalTime or self.eta.is_before(self.controller.globalTime)):
				if(self.status == "Returning to hub"):
					self.status = "At hub"
					self.location = self.destination
					self.eta = None
					self.destination = None
				else:
					self.currentPackage.status = "Delivered"
					self.currentPackage.timeDelivered = Time.copy_time(self.controller.globalTime)
					print(str(self.currentPackage))
					print("")
					self.controller.packagesDelivered += 1
					self.location = self.destination
					self.destination = None
					self.currentPackage = None
					self.eta = None
				self.make_deliveries()
		return self.status
	
	def make_deliveries(self):
		if(len(self.cargo) > 0):
			self.deliver(self.cargo.pop())
		elif(self.location != self.controller.hub):
			self.return_to_hub()
	
	def __str__(self):
		string = "Truck #" + str(self.id) + "\n"
		string += "Status: " + self.status
		return string