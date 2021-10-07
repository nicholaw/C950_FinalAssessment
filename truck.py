"""
Represents a delivery truck which can hold and deliver packages.
"""

from packages import Package
from timeofday import Time
from address import Address
#from controller import Controller

#Define the Truck class
class Truck:
	#Constants
	MAX_PACKAGES = 16
	AVG_SPEED_MPH = 18
	AVG_SPEED_MPM = AVG_SPEED_MPH / 60
	
	def __init__(self, id, startingLocation, controller):
		self.id = id
		self.totalDist = 0
		self.cargo = list()
		self.location = startingLocation
		self.controller = controller
		self.status = "At hub"

	def load(self, p):
		if(len(self.cargo) >= MAX_PACKAGES):
			return False
		else:
			self.cargo.append(p)
			return True
	
	def deliver(self, package):
		self.status = "Delivering package #" + str(package.id)
    
	def return_to_hub(self):
		self.status = "Returning to hub"
	
	def check_status(self):
		return self.status
	
	def make_deliveries(self):
		while(len(self.cargo) > 0):
			deliver(self.cargo.pop())
		self.return_to_hub()
	
	def __str__(self):
		string = "Truck #" + str(self.id) + "\n"
		string += "Status: " + self.status
		return string