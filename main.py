from timeofday import Time
from locations import allLocations
from packages import allPackages
from truck import Truck

def set_hub():
	for location in allLocations:
		if(location.name == "Western Governors University"):
			return location
	return None

time = Time.of("08:00")
hub = set_hub()
truck1 = Truck(1, hub)
fleet = set()
fleet.add(truck1)

#-------------------------------------------------------------------------------------------#
#TESTING
#-------------------------------------------------------------------------------------------#
while(len(allPackages) > 0):
	for truck in fleet:
		if(truck.location == hub):
			while(truck1.load(allPackages.pop())):
				continue
			truck1.make_deliveries()
	time.step()