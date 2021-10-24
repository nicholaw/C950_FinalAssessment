"""
Represents a group of packages which must be on the same truck together at the same time
"""
class PackageGroup:
	def __init__(self):
		self.group = dict()
	
	def insert(self, package):
		if(self.contains(package)):
			return False
		else:
			self.group[package] = package
	
	def insert_group(self, item):
		if(type(item) != type(self)):
			return False
		for g in self.group:
			if(PackageGroup.intersect_groups(self.group[g], item).size() > 0):
				union = PackageGroup.union_groups(self.group[g], item)
				self.group[union] = union
				self.group.pop(g)
				return True
		self.group[item] = item
		return True
	
	def remove(self, package):
		try:
			self.group.pop(package)
			return True
		except KeyError:
			return False
	
	def remove_group(self, group):
		try:
			self.group.pop(grop)
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
		return len(self.group)
	
	def union_groups(groupA, groupB):
		union = PackageGroup()
		for p in groupA.group:
			union.insert(p)
		for p in groupB.group:
			union.insert(p)
		return union
	
	def intersect_groups(groupA, groupB):
		intersection = PackageGroup()
		for p in groupA.group:
			if(groupB.contains(p)):
				intersection.insert(p)
		return intersection
	
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