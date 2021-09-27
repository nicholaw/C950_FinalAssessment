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
list = list()
for p in packages:
    if(len(currTruck.packages) >= 16):
        currTruck.make_deliveries()
        if(currTruck == truck1):
            currTruck = truck2
        else:
            currTruck = truck1
    currTruck.load(p)
if(len(truck1.packages) > 0):
    truck1.make_deliveries()
if(len(truck2.packages) > 0):
    truck2.make_deliveries()
print("ALGORITHM I:")
print("Truck #1 time finished: " + str(truck1.internalTime))
print("Truck #2 time finished: " + str(truck2.internalTime))
print("Total Distance: " + str(truck1.totalDist + truck2.totalDist))
print("")

#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#	ALGORITHM II
#	Sort packages by minimum geographical distance before loading trucks
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
"""
While len(packages) < MAX/2  -->  add shortest distance moving away from hub
While len(packages) < MAX    -->  add shortest distance moving towards hub

Given:  package A is loaded on truck, package B is being analyzed...
        if(dist_from_hub(A) > dist_from_hub(B))...
        B is moving towards hub
"""

#Returns either the set of packages closesr to the hub than the provided package
#or farther from the hub than the provided package.
def divide_direction(pakA, towardsHub):
    closer = set()
    farther = set()
    for p in packages:
        if(find_dist_from_hub(pakA.dest) > find_dist_from_hub(p.dest)):
            closer.add(p)
        else:
            farther.add(p)
    if(towardsHub):
        if(len(closer) > 0):
            return closer
        else:
            return farther
    else:
        if(len(farther) > 0):
            return farther
        else:
            return closer

#Returns the distance between the given addresses
def find_dist(add1, add2):
    return map[add1].adjacencies[map[add2].id]

#Returns the distance between the given address and the hub
def find_dist_from_hub(add1):
    return map[add1].adjacencies[0]

truck1 = Truck(1)
truck2 = Truck(2)
currTruck = truck1

#Moves packages from set of all packages to trucks for delivery
while(len(packages) > 0):
    if(len(currTruck.packages) >= 16):
        currTruck.make_deliveries()
        if(currTruck == truck1):
            currTruck == truck2
        else:
            currTruck == truck1
    if(len(currTruck.packages) < (MAX_PACKAGES / 2)):
        nextPak = None
        minDist = 999
        if(len(currTruck.packages) == 0):
            for p in packages:
                tempDist = find_dist_from_hub(p.dest)
                if(tempDist < minDist):
                    nextPak = p
                    minDist = tempDist
            currTruck.load(nextPak)
            packages.remove(nextPak)
        else:
            nextPak = None
            minDist = 999
            for p in divide_direction(currTruck.packages[len(currTruck.packages) - 1], False):
                tempDist = find_dist(p.dest, currTruck.packages[len(currTruck.packages) - 1].dest)
                if(tempDist < minDist):
                    nextPak = p
                    minDist = tempDist
            currTruck.load(nextPak)
            packages.remove(nextPak)
    elif(len(currTruck.packages) < MAX_PACKAGES):
        nextPak = None
        minDist = 999
        for p in divide_direction(currTruck.packages[len(currTruck.packages) - 1], True):
            tempDist = find_dist(p.dest, currTruck.packages[len(currTruck.packages) - 1].dest)
            if(tempDist < minDist):
                    nextPak = p
                    minDist = tempDist
        currTruck.load(nextPak)
        packages.remove(nextPak)

print("ALGORITHM II:")
print("Truck #1 time finished: " + str(truck1.internalTime))
print("Truck #2 time finished: " + str(truck2.internalTime))
print ("Total Distance: " + str(truck1.totalDist + truck2.totalDist))
print("")