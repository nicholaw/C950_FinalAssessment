"""
Nicholas Warner
ID: 001447619
"""

from packages import packages, Package
from verticies import map, Vertex, Address
from truck import Truck

#Instantiate delivery trucks
truck1 = Truck(1)
truck2 = Truck(2)

#Move packages from set to ordered, changable list
deliveries = list()
for p in packages:
    deliveries.append(p)

#Load and deliver packages until the list of deliveries is empty
print("Loading packages...")
while(len(deliveries) > 0):
    #Load truck with maximum allowable packages
    nextDelivery = deliveries.pop()
    if(truck1.load(nextDelivery) == False or len(deliveries) <= 0):
        deliveries.append(nextDelivery)
        #Deliver the loaded packages
        print("Delivering packages...")
        while(len(truck1.packages) > 0):
            truck1.deliver_next()
        truck1.return_to_hub()
        if(len(deliveries > 0)):
            print("Loading packages...")
"""
pTest = Package(100)
pTest.dest = Address.of("130 S 1300 E", "Salt Lake City", "UT", "84102")
vTest = Vertex(200)
vTest.address = Address.of("130 S 1300 E", "Salt Lake City", "UT", "84102")
print("PACKAGE:")
print(str(pTest.dest))
print(str(hash(pTest.dest)))
print(type(pTest.dest))
print()
print("VERTEX:")
print(str(vTest.address))
print(str(hash(vTest.address)))
print(type(vTest.address))
print()
print(pTest.dest == vTest.address)
"""