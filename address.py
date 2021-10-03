"""
Represents a physical location on the downtown Salt Lake City map and uses
a matrix to track the distance between other physical locations on the map
"""
class Address:
	def __init__(self, name):
		self.name = name
		self.street = ""
		self.city = ""
		self.state = "UT"
		self.zip = ""
		self.distances = dict()

	def of(street, city, state, zip):
		address = Address("")
		address.street = street
		address.city = city
		address.state = state
		address.zip = zip
		return address

	def __str__(self):
		str = ""
		if(len(self.name) > 0):
			str = self.name + "\n" + self.street + "\n" + self.city + ", " + self.state + " " + self.zip
		else:
			str = self.street + "\n" + self.city + ", " + self.state + " " + self.zip
		return str

	def __hash__(self):
		hash = 2729
		primeMultiplier = 83
		string = "" + self.street + self.city + self.state + self.zip
		for char in string:
			hash = hash * primeMultiplier + ord(char)
		return hash % 128
	
	def __eq__(self, other):
		if(type(self) != type(other)):
			return False
		if(self.zip != other.zip):
			return False
		if(self.state != other.state):
			return False
		if(self.city != other.city):
			return False
		if(self.street != other.street):
			return False
		return True