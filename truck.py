"""
Represents a delivery truck which can hold and deliver packages.
"""

#Constants
MAX_PACKAGES = 16
AVG_SPEED = 18

#Define the Truck class
class Truck:
	def __init__(self, id):
		self.id = id
		self.packages = ""
		self.total_dist = 0
		self.location = ""
		self.packages = list()

	def load(self, p):
		if(len(self.packages) >= MAX_PACKAGES):
			return False
		else:
			packages.append(p)
			return True

	def deliver_next(self):
		p = packages.pop(0)
		self.location = p.dest