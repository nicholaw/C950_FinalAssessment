"""
Represents a group of packages which must be on the same truck together at the same time
"""
class PackageGroup:
	def __init__(self):
		self.group = dict()
	
	def insert(self, package):
		if(self.contains(package):
			return False
		else:
			self.group[package] = package
	
	def remove(self, package):
		try:
			self.group.pop(package)
			return True
		except KeyError:
			return False
	
	def contains(self, package):
		try:
			self.group[package]
			return True
		except KeyError:
			return False
	
	def size(self):
		return len(self.group))
	
	def __str__(self):
		return str(self.group)
	
	def __eq__(self, other):
		if(type(self) != type(other)):
			return False
		return self.group == other.group
	
	def __hash__(self):
		sum = 0
		for item in self.group:
			sum += (hash(item) * 13)
		return (sum % 1024)