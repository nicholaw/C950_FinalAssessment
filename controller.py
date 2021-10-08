"""
Class which controls interactions among other classes
"""

from timeofday import Time
from locations import allLocations
from packages import allPackages
from truck import Truck
from constants import MAX_PACKAGES

class Controller:
	#Constructs this Controller object
	def __init__(self, numTrucks, startTime, hubName):
		self.globalTime = startTime
		self.hub = Controller.set_hub(hubName)
		self.fleet = set()
		self.populate_fleet(numTrucks)
		self.packagesDelivered = 0
	
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
		packageToLoad = None
		if(len(truck.cargo) == 0):
			packageToLoad = Controller.find_closest(self.hub, allPackages)
			truck.load(packageToLoad)
			allPackages.remove(packageToLoad)
			
		while((len(truck.cargo) < MAX_PACKAGES) and (len(allPackages) > 0)):
			if(len(truck.cargo) < (MAX_PACKAGES / 2)):
				packageToLoad = self.find_next_package(truck.cargo[len(truck.cargo) - 1], False)
			else:
				packageToLoad = self.find_next_package(truck.cargo[len(truck.cargo) - 1], True)
			truck.load(packageToLoad)
			allPackages.remove(packageToLoad)	
	
	def find_next_package(self, loadedPackage, towardsHub):
		closerToHub = set()
		fartherFromHub = set()
		for package in allPackages:
			if(Controller.find_distance(self.hub, package.dest) <= Controller.find_distance(self.hub, loadedPackage.dest)):
				closerToHub.add(package)
			else:
				fartherFromHub.add(package)
		if(towardsHub):
			if(len(closerToHub) == 0):
				return Controller.find_closest(loadedPackage.dest, fartherFromHub)
			else:
				return Controller.find_closest(loadedPackage.dest, closerToHub)
		else:
			if(len(fartherFromHub) == 0):
				return Controller.find_closest(loadedPackage.dest, closerToHub)
			else:
				return Controller.find_closest(loadedPackage.dest, fartherFromHub)
	
	def find_closest(locationA, collection):
		minDist = 999
		closestPackage = None
		for item in collection:
			try:
				dist = Controller.find_distance(locationA, item.dest)
				if(dist < minDist):
					minDist = dist
					closestPackage = item
			except:
				print("ERROR:")
				print(str(item))
				print("")
			finally:
				return closestPackage
	
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
	
	def unfinished_deliveries(self):
		unfinished = False
		for truck in self.fleet:
			if(len(truck.cargo) > 0):
				unfinished = True
			elif(truck.status == "Delivering package"):
				unfinished = True
		return unfinished
	
	def print_stats(self):
		print("Deliveries: " + str(self.packagesDelivered))
		print("Time: " + str(self.globalTime))
		print("Distance(mi):")
		total = 0
		for truck in self.fleet:
			num = Controller.truncate_to_tenth(truck.totalDist)
			total += num
			print("   " + str(num))
		print("Total Distance: " + str(total))
	
	def truncate_to_tenth(num):
		num = int(num * 10)
		return (num / 10.0)