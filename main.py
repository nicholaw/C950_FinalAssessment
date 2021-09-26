"""
Nicholas Warner
ID: 001447619
"""

from packages import packages, Package
from verticies import map
from truck import Truck, MAX_PACKAGES
from bucket import Bucket, DeadlineComparator

#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#	ALGORITHM I
#	Load packages onto trucks as they appear disregarding distance and special notes
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
truck1 = Truck(1)
truck2 = Truck(2)

currTruck = truck1
for p in packages:
	if(len(currTruck.packages) < 16):
		currTruck.load(p)
	else:
		currTruck.make_deliveries()
		currTruck = truck2
if(len(truck1.packages) > 0):
	truck1.make_deliveries()
if(len(truck2.packages) > 0):
	truck2.make_deliveries()
print("ALGORITHM I:")
print("Truck #1 time finished: " + str(truck1.internalTime))
print("Truck #2 time finished: " + str(truck2.internalTime))
print ("Total Distance: " + str(truck1.totalDist + truck2.totalDist))
print("")

#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#	ALGORITHM II
#	Sort packages by minimum geographical distance before loading trucks
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
"""
While len(packages) < MAX/2  -->  add shortest distance moving away
While len(packages) < MAX    -->  add shortest distance moving towards
"""
truck1 = Truck(1)
truck2 = Truck(2)
currTruck = truck1

#Moves packages from set of all packages to trucks for delivery
for p in packages:
    if(len(currTruck.packages) < (MAX_PACKAGES / 2)):
        
    elif(len(currTruck.packages) < MAX_PACKAGES):
    else:
        currTruck.make_deliveries()
        toggle_truck()

#Returns the closet package in packages to the given package
def find_shortest(pak, towardsHub):
    cloestPak = None
    shortestDist = 999
    for p in packages:
        dist = find_dist(p.dest, pak.dest)
        if(dist < shortestDist):
            shortestDist = dist
            closestPak = p

#Returns the distance between the given addresses
def find_dist(add1, add2):
    vert = None
    for v in map:
        if(v.address == add2):
            vert = v
            break
    return map[add1].adjacencies[vert.id]

#Returns the distance between the given address and the hub
def find_dist_from_hub(add1):
    return map[add1].adjacencies[0]

#Switches which truck is the current truck
def toggle_truck():
    if(currTruck == truck1):
        currTruck = truck2
    else:
        currTruck = truck1

print("ALGORITHM II:")
print("Truck #1 time finished: " + str(truck1.internalTime))
print("Truck #2 time finished: " + str(truck2.internalTime))
print ("Total Distance: " + str(truck1.totalDist + truck2.totalDist))
print("")