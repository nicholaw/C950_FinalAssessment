"""
Nicholas Warner
ID: 001447619
"""

from packages import Package,packages
#from truck import Truck
from verticies import routeGraph

#t1 = Truck(1)
#t2 = Truck(2)

#Test all possible delivery address were read correctly from xml
print(str(len(routeGraph)))
for v in routeGraph:
    print(v.name)
    print(str(v.address))
    print("\n")