from timeofday import Time
from locations import allLocations

time = Time.of("08:00")
endTime = Time.of("09:00")

for location in allLocations:
	print(str(location))
	print("")