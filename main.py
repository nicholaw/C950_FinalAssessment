"""
Launches C950 parcel delivery algorithm
"""
"""
from timeofday import Time
from controller import Controller

controller = Controller(2, Time.of("08:00"), "Western Governors University")
controller.start()
"""
from packages import allPackages, finalGroups
from locations import allLocations
count = 1
for group in finalGroups.group:
	print("Group #" + str(count))
	count += 1
	for p in group.group:
		print(str(p))
	print("--------------------------------------------------")