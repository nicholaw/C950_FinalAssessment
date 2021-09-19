"""
Represents a delivery truck which can hold and deliver packages.
"""

from packages import Package
from verticies import map, HUB_VERTEX
from timeofday import Time

#Constants
MAX_PACKAGES = 16
AVG_SPEED_MPH = 18
AVG_SPEED_MPM = 0.3

#Define the Truck class
class Truck:
    def __init__(self, id):
        self.id = id
        self.totalDist = 0
        self.location = HUB_VERTEX
        self.packages = list()
        self.internalTime = Time.of("08:00")

    def load(self, p):
        if(len(self.packages) >= MAX_PACKAGES):
            return False
        else:
            self.packages.append(p)
            print("Loading package " + str(p.id))
            return True

    def deliver_next(self):
        p = self.packages.pop(0)
        #p.status = EN_ROUTE
        delivDest = map[p.dest]
        distToDest = delivDest.adjacencies[self.location.id]
        self.totalDist = totalDist + distToDest
        self.internalTime.addMinutes(distToDest // AVG_SPEED_MPM)
        self.location = delivDest
        #p.status = DELIVERED
        p.timeDelivered = Time.of(str(self.timeOfDay))
        print("Delivered package " + p.id() + " at " + str(p.timeDelivered))
        print("Total distance driven(miles): " + self.totalDist)
    
    def return_to_hub(self):
        distToDest = HUB_VERTEX.adjacencies[self.location.id]
        self.totalDist = totalDist + distToDest
        self.internalTime.addMinutes(distToDest // AVG_SPEED_MPM)
        self.location = delivDest
        print("Returning to hub...")
        print("Total distance driven(miles): " + self.totalDist)