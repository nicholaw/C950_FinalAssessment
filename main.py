"""
Launches C950 parcel delivery algorithm
"""
"""
from timeofday import Time
from controller import Controller

controller = Controller(2, Time.of("08:00"), "Western Governors University")
controller.start()
"""
from packages import allPackages
from locations import allLocations
for p in allPackages:
	try:
		allLocations[p.dest]
	except KeyError:
		print(str(p))