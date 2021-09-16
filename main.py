"""
Nicholas Warner
ID: 001447619
"""

from packages import packages
from verticies import map
from truck import Truck

#Instantiate delivery trucks
truck1 = Truck(1)
truck2 = Truck(2)

for p in packages:
	if(p.id == 1):
		print(str(p))