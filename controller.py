"""
Class which controls interactions among other classes
"""

from timeofday import Time
from locations import allLocations
from packages import allPackages, finalGroups
from truck import Truck
from constants import MAX_PACKAGES, truncate_to_tenth, reverse_array
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
	
	#Chooses the next package to be loaded onto the provided truck and loads the package
	def load_truck(self, truck):
		eligiblePackages = self.eligible_packages(truck)
		priorityPackages = self.check_for_prioity_packages(eligiblePackages)
		orig = len(priorityPackages)
		groupPackages = set()
		#Continue loading truck until it's full or there are no more eligiblePackages
		while(len(truck.cargo) < MAX_PACKAGES and len(eligiblePackages) > 0):
			#Truck is not empty
			if(len(truck.cargo) > 0):
				if(len(groupPackages) > 0):
					nextPackage = Controller.nearest_neighbor(truck.cargo[len(truck.cargo) -1].dest, groupPackages)
					groupPackages.remove(nextPackage)
				elif(len(priorityPackages) > int(orig - orig * (truck.id / len(self.fleet)))):
					nextPackage = Controller.nearest_neighbor(truck.cargo[len(truck.cargo) -1].dest, priorityPackages)
					priorityPackages.remove(nextPackage)
				else:
					nextPackage = Controller.nearest_neighbor(truck.cargo[len(truck.cargo) -1].dest, eligiblePackages)
			#Truck is empty
			else:
				if(len(priorityPackages) > int(orig - orig * (truck.id / len(self.fleet)))):
					nextPackage = Controller.nearest_neighbor(self.hub, priorityPackages)
					priorityPackages.remove(nextPackage)
				else:
					nextPackage = Controller.nearest_neighbor(self.hub, eligiblePackages)
			group = self.is_part_of_group(nextPackage)
			#Check if the package to load is part of a group
			if(group != None):
				Controller.add_packages(group.group, groupPackages, nextPackage)
				for p in groupPackages:
					try: 
						priorityPackages.remove(p)
					except KeyError:
						continue
				finalGroups.remove_group(group)
			#Load next package and remove from relevant sets
			eligiblePackages.remove(nextPackage)
			truck.load(allPackages.pop(nextPackage.id))
		truck.cargo = reverse_array(truck.cargo)
	
	#Returns the set of packages eligible to be loaded onto the provided truck
	def eligible_packages(self, truck):
		eligible = set()
		for id in allPackages:
			p = allPackages[id]
			if(Controller.is_valid(p, truck.id, self.globalTime)):
				eligible.add(p)
		return eligible
	
	#Retruns a set of packages from the provided collection with deadlines within two hours of the current time
	def check_for_prioity_packages(self, collection):
		priority = set()
		for item in collection:
			if(item.deadline != None):
				time = Time.copy_time(self.globalTime)
				time.add_minutes(150)
				if(item.deadline.is_before(time) or item.deadline == time):
					priority.add(item)
		return priority
	
	#Returns the group of which the provided package is a part if the provided package is part of a group
	def is_part_of_group(self, package):
		for group in finalGroups.group:
			if(group.contains(package)):
				return group
		return None
	
	#Adds all packages except the provided package from collection A to collectionB
	def add_packages(collectionA, collectionB, excludedPackage):
		for p in collectionA:
			if(p != excludedPackage):
				collectionB.add(p)
	
	#Finds the nearest neighbor to the provided location within the provided collection
	def nearest_neighbor(location, collection):
		next = None
		minDist = 999
		for item in collection:
			dist = Controller.find_distance(location, item.dest)
			if(dist < minDist):
				minDist = dist
				next = item
		return next
	
	#Returns true if the provided package is eligible to be loaded onto the provided truck at the current time
	def is_valid(package, truckId, time):
		if(not(package.truck == 0 or package.truck == truckId)):
			return False
		if(package.available.is_after(time)):
			return False
		return True
	
	#Returns the distacne between two provided locations
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
	
	#Continues algorithm until all packages loaded onto trucks have been delivered
	def finish(self):
		while(self.unfinished_deliveries()):
			for truck in self.fleet:
				truck.check_status()
			self.globalTime.step()
		self.ui.start()
	
	#Returns true if there are trucks making deliveries
	def unfinished_deliveries(self):
		unfinished = False
		for truck in self.fleet:
			if(len(truck.cargo) > 0):
				unfinished = True
			elif(truck.currentPackage != None):
				unfinished = True
		return unfinished
	
	#Returns the package matching the proveded package id
	def get_package(id):
		try:
			return allPackages[id]
		except KeyError:
			return None
	
	#Prints statistics for the current execution such as the time deliveries were completed and the total milage driven by the trucks
	def print_stats(self):
		print("Deliveries: " + str(self.packagesDelivered))
		print("Time: " + str(self.globalTime))
		print("Distance(mi):")
		total = 0
		for truck in self.fleet:
			num = truncate_to_tenth(truck.totalDist)
			total += num
			print("   " + str(num))
		print("Total Distance: " + str(truncate_to_tenth(total)))