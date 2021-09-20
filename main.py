"""
Nicholas Warner
ID: 001447619
"""

from packages import packages, Package
from verticies import map
from truck import Truck
from timeofday import Time

#Instantiate delivery trucks
truck1 = Truck(1)
#truck2 = Truck(2)

for p in packages:
	if(not(truck1.load(p))):
		while(len(truck1.packages) >  0):
			truck1.deliver_next()
		truck1.return_to_hub()
while(len(truck1.packages) >  0):
	truck1.deliver_next()
truck1.return_to_hub()