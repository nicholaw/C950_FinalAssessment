"""
Class which controls interactions between other classes
"""

from timeofday import Time
from locations import allLocations
from packages import allPackages
from truck import Truck

class Controller:
	def __init__(self, numTrucks, startTime, hubName):
		self.globalTime = startTime
		self.hub = Controller.set_hub(hubName)
		self.fleet = set()
		self.populate_fleet(numTrucks)
	
	def set_hub(hubName):
		for location in allLocations:
			if(location.name == hubName):
				return location
		return None
	
	def populate_fleet(self, numTrucks):
		if(numTrucks <= 0):
			self.fleet.add(Truck(1, self.hub, self))
		else:
			i = 1
			while(len(self.fleet) < numTrucks):
				self.fleet.add(Truck(i, self.hub, self))
				i += 1
	
	def load_truck(truck):
		while((len(truck.cargo) < Truck.MAX_PACKAGES) and (len(allPackages) > 0)):
			truck.load(allPackages.pop())
	
	def start(self):
		while(len(allPackages) > 0):
			for truck in fleet:
				if(truck.location == hub):
					load_truck(truck)
					truck.make_deliveries()
				else:
					truck.check_status()
		self.globalTime.step()