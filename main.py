from timeofday import Time
from locations import allLocations
from packages import allPackages

time = Time.of("08:00")
endTime = Time.of("09:00")

for p in allPackages:
	print(str(p))
	print("")