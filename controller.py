"""
Class which controls interactions among other classes
"""

from timeofday import Time
from locations import allLocations
from packages import allPackages, finalGroups, deadlineBuckets
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
        self.priorityPackages = None
        self.set_priority_packages()
    
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
        available = True
        while((len(truck.cargo) < MAX_PACKAGES) and (len(allPackages) > 0) and available):
            nextPackage = None
            minDist = 999
            for pid in allPackages:
                p = allPackages[pid]
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
                groupPresent = False
                for group in finalGroups.group:
                    if(group.contains(nextPackage)):
                        self.load_group(group, nextPackage, truck)
                        groupPresent = True
                if(not groupPresent):
                    truck.load(nextPackage)
                    allPackages.pop(nextPackage.id)
            else:
                available = False
    
    def load_group(self, group, package, truck):
        #sort the group by nearest neighbor starting with provided package
        packages = Controller.sort_group(group, package)
        #ensure there is sufficient space on truck for entire group
        while(len(truck.cargo) + len(packages) > MAX_PACKAGES):
            p = truck.cargo.pop()
            allPackages[p.id] = p
        #load the group
        for p in packages:
            truck.load(p)
            allPackages.pop(p.id)
        finalGroups.remove_group(group)
    
    def sort_group(group, package):
        loadOrder = [package]
        group.remove(package)
        while(group.size() > 1):
            next = None
            minDist = 999
            for p in group.group:
                dist = Controller.find_distance(loadOrder[len(loadOrder) - 1].dest, p.dest)
                if(dist < minDist):
                    next = p
                    minDist = dist
            loadOrder.append(group.pop(next))
        loadOrder.append(group.pop_last())
        return loadOrder
    
    #finds the nearest neighbor to the provided location within the provided collection
    def nearest_neighbor(location, collection):
        next = None
        minDist = 999
        for item in collection:
            dist = Controller.find_distance(location, item.dest)
            if(dist < minDist):
                minDist = dist
                next = item
        return next
    
    def is_valid(self, package, truck):
        if(not(package.truck == 0 or package.truck == truck.id)):
            return False
        if(package.available.is_after(self.globalTime)):
            return False
        return True
    
    def find_distance(locationA, locationB):
        return allLocations[locationA].distances[locationB]
    
    def set_priority_packages(self):
        try:
            self.priorityPackages = deadlineBuckets[self.globalTime]
        except KeyError:
            return
    
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
            self.check_priority_packages()
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
        try:
            return allPackages[id]
        except KeyError:
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
        print("Total Distance: " + str(truncate_to_tenth(total)))