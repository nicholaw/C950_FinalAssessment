"""
Represents a package which can be loaded onto a truck and delivered to a location
"""

from address import Address
from timeofday import Time

class Package:
	def __init__(self, id):
		self.id = id
		self.dest = Address("NONE")
		self.available = Time.of("08:00")
		self.deadline = Time.of("23:59")
		self.timeDelivered = -1
		self.mass = 1
		self.note = ''
		self.truck = -1
		self.group = set()

	def __str__(self):
		string = "(" + str(self.id) + ")\n"
		string = string + str(self.dest)
		return string

	def __hash__(self):
		return ((self.id * 5867) % 128)

	def __eq__(self, other):
		if(type(self) != type(other)):
			return False
		if(self.id != other.id):
			return False
		return True