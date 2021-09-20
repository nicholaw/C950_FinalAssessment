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
        self.internalTime = Time.of("08:00")
        self.id = id
        self.totalDist = 0
        self.location = HUB_VERTEX
        self.packages = list()

    def load(self, p):
        if(len(self.packages) >= MAX_PACKAGES):
            return False
        else:
            self.packages.append(p)
            print("Loading package " + str(p.id))
            return True

    def deliver_next(self):
        p = self.packages.pop(0)
        delivDest = map[p.dest]
        distToDest = delivDest.adjacencies[self.location.id]
        self.totalDist = int((self.totalDist + distToDest) * 10) / 10
        self.internalTime.add_minutes(int(distToDest // AVG_SPEED_MPM))
        self.location = delivDest
        p.timeDelivered = Time.of(str(self.internalTime))
        print("Delivered package " + str(p.id) + " at " + str(p.timeDelivered))
        print("Total distance driven(miles): " + str(self.totalDist))
    
    def return_to_hub(self):
        distToDest = HUB_VERTEX.adjacencies[self.location.id]
        self.totalDist = int((self.totalDist + distToDest) * 10) / 10
        self.internalTime.add_minutes(int(distToDest // AVG_SPEED_MPM))
        self.location = HUB_VERTEX
        print("Returning to hub...")
        print("Total distance driven(miles): " + str(self.totalDist))