from timeofday import Time
from locations import allLocations

time = Time.of("08:00")
endTime = Time.of("09:00")

for location in allLocations:
	if(location.name == "Wheeler Historic Farm"):
		for item in location.distances:
			print(item.name)
			print(str(location.distances[item]))
			print("")