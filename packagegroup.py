"""
Represents a group of packages which must be on the same truck together at the same time
"""

class PackageGroup:
	#Constructs this object
    def __init__(self):
        self.group = dict()
    
    #Inserts the provided package into this group
    def insert(self, package):
        if(self.contains(package)):
            return False
        else:
            self.group[package] = package
            return True

	#Inserts the provided group of packages into this group
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
    
    #Removes the provided package from this group
    def remove(self, package):
        try:
            self.group.pop(package)
            return True
        except KeyError:
            return False
    
    #Removes and returns provided item from this group
    def pop(self, item):
        try:
            return self.group.pop(item)
        except KeyError:
            return None
    
    #Removes and returns the last item from this group
    def pop_last(self):
        if(len(self.group) == 1):
            for item in self.group:
                return self.group.pop(item)
        else:
            return None
    
    #Remove the provided package group from this group
    def remove_group(self, group):
        try:
            self.group.pop(group)
            return True
        except KeyError:
            return False
	
	#Returns true if this group contains the provided package and false otherwise
    def contains(self, package):
        try:
            self.group[package]
            return True
        except KeyError:
            return False
    
    #Returns the number of items in this group
    def size(self):
        return len(self.group)
	
	#Returns the union of the two provided groups
    def union_groups(groupA, groupB):
        union = PackageGroup()
        for p in groupA.group:
            union.insert(p)
        for p in groupB.group:
            union.insert(p)
        return union
    
    #Returns the intersection of the two provided groups
    def intersect_groups(groupA, groupB):
        intersection = PackageGroup()
        for p in groupA.group:
            if(groupB.contains(p)):
                intersection.insert(p)
        return intersection
    
    #Returns a string representation of this object
    def __str__(self):
        return str(self.group)
    
    #Returns true if the provided object is equal to this object and false otherwise
    def __eq__(self, other):
        if(type(self) != type(other)):
            return False
        return self.group == other.group
    
    #Returns the hash value of this object
    def __hash__(self):
        sum = 0
        for item in self.group:
            sum += (hash(item) * 13)
        return (sum % 1024)