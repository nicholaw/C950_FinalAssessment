"""
Launches C950 parcel delivery algorithm
"""

from timeofday import Time
from controller import Controller

"""
controller = Controller(2, Time.of("08:00"), "Western Governors University")
controller.start()
controller.print_stats()
"""

from packages import allPackages
from locations import allLocations

package = None
id = 26
for p in allPackages:
	if(p.id == id):
		package = p
if(package == None):
	print("Package #" + str(id) + " not found.")
else:
	print(str(package))
	print("")
	for l in allLocations:
		try:
			print(str(l.distances[p.dest]))
		except:
			print("")
			print(str(l))
			print("")