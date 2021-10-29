"""
Represents a physical location on the downtown Salt Lake City map and uses
a matrix to track the distance between other physical locations on the map
"""
class Address:
	#Constructs this address
	def __init__(self, name):
		self.name = name
		self.street = ""
		self.city = ""
		self.state = "UT"
		self.zip = ""
		self.distances = dict()

	#Returns an address with the provided attribute values
	def of(street, city, state, zip):
		address = Address("")
		address.street = street
		address.city = city
		address.state = state
		address.zip = zip
		return address

	#Returns a string representation of this object
	def __str__(self):
		str = ""
		if(len(self.name) > 0):
			str = self.name + "\n" + self.street + "\n" + self.city + ", " + self.state + " " + self.zip
		else:
			str = self.street + "\n" + self.city + ", " + self.state + " " + self.zip
		return str

	#Returns a hash value for this object
	def __hash__(self):
		hash = 2729
		primeMultiplier = 83
		string = "" + self.street + self.city + self.state + self.zip
		for char in string:
			hash = hash * primeMultiplier + ord(char)
		return hash % 128
	
	#Returns true if the provided object is equal to this object and false otherwise
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