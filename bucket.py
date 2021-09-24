"""
Data structure which represents a 'bucket' into which packages are sorted for 
distribution onto trucks. Bucket sorts items with the provided comparator when 
items are added.
"""

from packages import Package

class Bucket:
	def __init__(self, comparator):
		self.items = list()
		self.comparator = comparator

	def contains(self, obj):
		for item in self.items:
			if(item == obj):
				return True
		return False

	def add(self, obj):
		if(len(self.items) == 0):
			self.items.append(obj)
			return True
		if(self.contains(obj)):
			return False
		i = 0
		while(i < len(self.items)):
			#if <= 0, place at i and shift right, else compare next
			if(self.comparator.compare(self.items[i], obj) > 0):
				Bucket.shift_array_right(self.items, i)
				self.items[i] = obj
				return True
			i += 1
		self.items.append(obj)
		return True

	def shift_array_right(arr, start):
		arr.append(arr[len(arr) - 1])
		i = len(arr) - 2
		while(i > start):
			arr[i] = arr[i - 1]
			i -= 1
	#end Bucket

"""
Comparator which compares delivery deadlines of two provided packages.
Returns 0 if the packages have the same deadline; returns 1 if the first deadline
is after the second deadline; returns -1 if the first deadline is after the second
deadline.
"""
class DeadlineComparator:
	def compare(self, obj1, obj2):
		if(obj1.deadline.is_after(obj2.deadline)):
			return 1
		if(obj1.deadline.is_before(obj2.deadline)):
			return -1
		return 0