class Package:
	def __init__(self, id):
		self.id = id
		self.dest = ''
		self.city = ''
		self.state = ''
		self.zip = ''
		self.available = 0001
		self.deadline = 2359
		self.mass = 1
		self.note = ''
		self.truck = -1
		self.group = {}