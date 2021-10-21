"""
Class which controls interactions among other classes
"""

from timeofday import Time
from locations import allLocations
from packages import allPackages
from truck import Truck
from constants import MAX_PACKAGES, truncate_to_tenth
from ui import UserInterface

class Controller:
	#Constructs this Controller object
	def __init__(self, numTrucks, startTime, hubName):
		self.globalTime = startTime
		self.hub = Controller.set_hub(hubName)
		self.fleet = set()
		self.populate_fleet(numTrucks)
		self.packagesDelivered = 0
		self.ui = UserInterface(allPackages, self.fleet, self)
	
	#Sets the hub location based on the provided location name
	def set_hub(hubName):
		for location in allLocations:
			if(location.name == hubName):
				return location
		return None
	
	#Instantiates the provided number of delivery trucks
	def populate_fleet(self, numTrucks):
		if(numTrucks <= 0):
			self.fleet.add(Truck(1, self.hub, self))
		else:
			i = 1
			while(len(self.fleet) < numTrucks):
				self.fleet.add(Truck(i, self.hub, self))
				i += 1
	
	#Loads a package onto a delivery truck;
	#If the truck is less than half full, loads a package which is farther from the hub than the last package loaded;
	#If the truck is more than half full, loads a package which is closer to the hub than the last package
	def load_truck(self, truck):
		while((len(truck.cargo) < MAX_PACKAGES) and (len(allPackages) > 0)):
			nextPackage = None
			minDist = 999
			for p in allPackages:
				if(self.is_valid(p, truck)):
					dist = 999
					if(len(truck.cargo) > 0):
						dist = Controller.find_distance(truck.cargo[len(truck.cargo) - 1].dest, p.dest)
					else:
						dist = Controller.find_distance(self.hub, p.dest)
					if(dist < minDist):
						minDist = dist
						nextPackage = p
			if(nextPackage != None):
				if(len(nextPackage.group) > 0):
					self.load_group(truck, nextPackage)
					print("Finished loading group")
				else:
					truck.load(nextPackage)
					allPackages.remove(nextPackage)
	
	def load_group(self, truck, basePackage):
		fullGroup = {basePackage}
		packagesToVisit = {basePackage}
		visitedPackages = dict()
		#Explore group memebers to find any other group memebers
		while(len(packagesToVisit) > 0):
			p = packagesToVisit.pop()
			visitedPackages[p] = p
			for g in p.group:
				g = Controller.get_package(g) #TODO: convert allPackages from set to dict so this operation isn't linear
				if(g != None):
					fullGroup.add(g)
					try:
						visitedPackages[g]
					except KeyError:
						packagesToVisit.add(g)
		#Make room for the entire group if there isn't enough room
		while(len(truck.cargo) + len(fullGroup) > MAX_PACKAGES): #Unloading the truck is terrible, but package groups are probably rare enough and small enough this isn't a big issue
			allPackages.add(truck.cargo.pop())
		#Sort the group by nearestNeighbor starting with basePackage
		deliveryOrder = [basePackage]
		fullGroup.remove(basePackage)
		while(len(fullGroup) > 1):
			next = Controller.nearest_neighbor(deliveryOrder[len(deliveryOrder) - 1], fullGroup)
			deliveryOrder.append(next)
			fullGroup.remove(next)
		next = fullGroup.pop()
		deliveryOrder.append(next)
		#Load the group of packages onto the truck
		for p in deliveryOrder:
			if(truck.load(p)):
				allPackages.remove(p)
	
	def is_valid(self, package, truck):
		if(not(package.truck == -1 or package.truck == truck.id)):
			return False
		if(package.available.is_after(self.globalTime)):
			return False
		return True
	
	#Returns the package from the provided collection whose delivery destination is closest to the destination of the provided package
	def nearest_neighbor(package, collection):
		nearestNeighbor = None
		minDist = 999
		for p in collection:
			dist = Controller.find_distance(package.dest, p.dest)
			if(dist < minDist):
				minDist = dist
				nearestNeighbor = p
		return nearestNeighbor
	
	def find_distance(locationA, locationB):
		return allLocations[locationA].distances[locationB]
	
	def start(self):
		while(len(allPackages) > 0):
			for truck in self.fleet:
				if(truck.location == self.hub):
					if(len(allPackages) > 0):
						self.load_truck(truck)
						truck.make_deliveries()
				else:
					truck.check_status()
			self.globalTime.step()
		self.finish()
	
	def finish(self):
		while(self.unfinished_deliveries()):
			for truck in self.fleet:
				truck.check_status()
			self.globalTime.step()
		self.ui.start()
	
	def unfinished_deliveries(self):
		unfinished = False
		for truck in self.fleet:
			if(len(truck.cargo) > 0):
				unfinished = True
			elif(truck.currentPackage != None):
				unfinished = True
		return unfinished
	
	def get_package(id):
		for p in allPackages:
			if(p.id == id):
				return p
		return None
	
	def print_stats(self):
		print("Deliveries: " + str(self.packagesDelivered))
		print("Time: " + str(self.globalTime))
		print("Distance(mi):")
		total = 0
		for truck in self.fleet:
			num = truncate_to_tenth(truck.totalDist)
			total += num
			print("   " + str(num))
		print("Total Distance: " + str(total))
		print("Length allPackages " + str(len(allPackages)))