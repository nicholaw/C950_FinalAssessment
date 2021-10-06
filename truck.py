"""
Represents a delivery truck which can hold and deliver packages.
"""

from packages import Package
from timeofday import Time
from address import Address

#Constants
MAX_PACKAGES = 16
AVG_SPEED_MPH = 18
AVG_SPEED_MPM = AVG_SPEED_MPH / 60

#Define the Truck class
class Truck:
	def __init__(self, id, startingLocation):
		self.id = id
		self.totalDist = 0
		self.cargo = list()
		self.location = startingLocation

	def load(self, p):
		if(len(self.cargo) >= MAX_PACKAGES):
			return False
		else:
			self.cargo.append(p)
			return True
	
	def deliver(self, package):
		#temp
    
	def return_to_hub(self):
		#temp
	
	def make_deliveries(self):
		while(len(self.cargo) > 0):
			deliver(self.cargo.pop())
		self.return_to_hub()