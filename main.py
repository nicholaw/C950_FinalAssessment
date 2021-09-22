"""
Nicholas Warner
ID: 001447619
"""

from packages import packages, Package
from verticies import map
from truck import Truck
from bucket import Bucket, DeadlineComparator

#Instantiate delivery trucks
truck1 = Truck(1)
#truck2 = Truck(2)
b = Bucket(DeadlineComparator())

for p in packages:
	b.add(p)
for p in b.items:
	print(str(p.id) + "\t" + str(hash(p)) + "\t" + str(p.deadline))