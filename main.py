"""
Nicholas Warner
ID: 001447619
"""

from packages import packages, Package
from verticies import map
from truck import Truck
from bucket import Bucket, DeadlineComparator

list = list()
for p in packages:
	print(str(p.id))

"""
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
truck1 = Truck(1)
truck2 = Truck(2)
currTruck = truck1
sortedPackages = list()
for p in packages:
	insert_at_min_dist(sortedPackages, p, currTruck)
for p in sortedPackages:
	if(len(currTruck.packages) < 16):
		currTruck.load(p)
	else:
		currTruck.make_deliveries()
		currTruck = truck2
if(len(truck1.packages) > 0):
	truck1.make_deliveries()
if(len(truck2.packages) > 0):
	truck2.make_deliveries()
print("ALGORITHM II:")
print("Truck #1 time finished: " + str(truck1.internalTime))
print("Truck #2 time finished: " + str(truck2.internalTime))
print ("Total Distance: " + str(truck1.totalDist + truck2.totalDist))
print("")
"""