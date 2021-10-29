"""
Constants and shared methods for use in the application
"""

from timeofday import Time

SOD = Time.of("08:00")
MAX_PACKAGES = 16
AVG_SPEED_MPH = 18
AVG_SPEED_MPM = AVG_SPEED_MPH / 60

#Truncates the provided number to the tenths decimal place
def truncate_to_tenth(num):
		num = int(num * 10)
		return (num / 10.0)

#Reverses the provided list
def reverse_array(orig):
	reverse = list()
	while(len(orig) > 0):
		reverse.append(orig.pop())
	return reverse