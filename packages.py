"""
File which contains each package to be delievered for the C950 final assessment and definition
for Package class.
"""

from verticies import Address
from timeofday import Time

#define Package class
class Package:
	def __init__(self, id):
		self.id = id
		self.dest = ""
		self.available = Time.of("08:00")
		self.deadline = Time.of("23:59")
		self.mass = 1
		self.note = ''
		self.truck = -1
		self.group = set()
		self.delivered = False
		self.time_delivered = -1

	def __str__(self):
		string = "Package:/n"
		string = string + str(self.id) + "\n"
		string = string + "Destination: "
		string = string + str(self.dest)
		return string

#instantiate the packages
p1 = Package(1)
p1.dest = Address.of("195 W Oakland Ave", "Salt Lake City", "UT", "84115")
p1.deadline = Time.of("10:30")
p1.mass = 21

p2 = Package(2)
p2.dest = Address.of("2530 S 500 E", "Salt Lake City", "UT", "84106")
p2.mass = 44

p3 = Package(3)
p3.dest = Address.of("233 Canyon Rd", "Salt Lake City", "UT", "84103")
p3.mass = 2
p3.note = 'Can only be on truck 2'
p3.truck = 2

p4 = Package(4)
p4.dest = Address.of("380 W 2880 S", "Salt Lake City", "UT", "84115")
p4.mass = 4

p5 = Package(5)
p5.dest = Address.of("410 S State St", "Salt Lake City", "UT", "84111")
p5.mass = 5

p6 = Package(6)
p6.dest = Address.of("3060 Lester S", "West Valley City", "UT", "84119")
p6.available = Time.of("09:05")
p6.deadline = Time.of("10:30")
p6.mass = 88
p6.note = 'Delayed on flight---will not arrive to depot until 09:05'

p7 = Package(7)
p7.dest = Address.of("1330 2100 S", "Salt Lake City", "UT", "84106")
p7.mass = 8

p8 = Package(8)
p8.dest = Address.of("300 State Street", "Salt Lake City", "UT", "84103")
p8.mass = 9

p9 = Package(9)
p9.dest = Address.of("300 State Street", "Salt Lake City", "UT", "84103")
p9.mass = 2
p9.note = 'Wrong address listed'

p10 = Package(10)
p10.dest = Address.of("600 E 900 S", "Salt Lake City", "UT", "84105")
p10.mass = 1

p11 = Package(11)
p11.dest = Address.of("2600 Taylorsville Blvd", "Salt Lake City", "UT", "84118")
p11.mass = 1

p12 = Package(12)
p12.dest = Address.of("3575 W Valley Central Station", "West Valley", "UT", "84119")
p12.mass = 1

p13 = Package(13)
p13.dest = Address.of("2010 W 500 S", "Salt Lake City", "UT", "84104")
p13.deadline = Time.of("10:30")
p13.mass = 2

p14 = Package(14)
p14.dest = Address.of("4300 S 1300 E", "Millcreek", "UT", "84117")
p14.deadline = Time.of("10:30")
p14.mass = 88
p14.note = 'Must be delivered with 15, 19'
p14.group = {14, 15, 19}

p15 = Package(15)
p15.dest = Address.of("4580 S 2300 E", "Holladay", "UT", "84117")
p15.deadline = Time.of("09:00")
p15.mass = 4

p16 = Package(16)
p16.dest = Address.of("4580 S 2300 E", "Holladay", "UT", "84117")
p16.deadline = Time.of("10:30")
p16.mass = 88
p16.note = 'Must be delivered with 13, 19'
p16.group = {13, 16, 19}

p17 = Package(17)
p17.dest = Address.of("3148 S 1100 W", "Salt Lake City", "UT", "84119")
p17.mass = 2

p18 = Package(18)
p18.dest = Address.of("1488 4800 S", "Salt Lake City", "UT", "84123")
p18.mass = 6
p18.note = 'Can only be on truck 2'
p18.truck = 2

p19 = Package(19)
p19.dest = Address.of("177 W Price Ave", "Salt Lake City", "UT", "84115")
p19.mass = 37

p20 = Package(20)
p20.dest = Address.of("3595 Main St", "Salt Lake City", "UT", "84115")
p20.deadline = Time.of("10:30")
p20.mass = 37
p20.note = 'Must be delivered with 13, 15'
p20.group = {13, 15, 20}

p21 = Package(21)
p21.dest = Address.of("3595 Main St", "Salt Lake City", "UT", "84115")
p21.mass = 3

p22 = Package(22)
p22.dest = Address.of("6351 South 900 East", "Murray", "UT", "84121")
p22.mass = 2

p23 = Package(23)
p23.dest = Address.of("5100 South 2700 West", "Salt Lake City", "UT", "84118")
p23.mass = 5

p24 = Package(24)
p24.dest = Address.of("5025 State St", "Murray", "UT", "84107")
p24.mass = 7

p25 = Package(25)
p25.dest = Address.of("5383 South 900 East #104", "Salt Lake City", "UT", "84117")
p25.available = Time.of("09:05")
p25.deadline = Time.of("10:30")
p25.mass = 7
p25.note = 'Delayed on flight---will not arrive to depot until 9:05'

p26 = Package(26)
p26.dest = Address.of("5383 South 900 East #104", "Salt Lake City", "UT", "84117")
p26.mass = 25

p27 = Package(27)
p27.dest = Address.of("1060 Dalton Ave S", "Salt Lake City", "UT", "84104")
p27.mass = 5

p28 = Package(28)
p28.dest = Address.of("2835 Main St", "Salt Lake City", "UT", "84115")
p28.available = Time.of("09:05")
p28.mass = 7
p28.note = 'Delayed on flight---will not arrive to depot until 9:05'

p29 = Package(29)
p29.dest = Address.of("1330 2100 S", "Salt Lake City", "UT", "84106")
p29.deadline = Time.of("10:30")
p29.mass = 2

p30 = Package(30)
p30.dest = Address.of("300 State St", "Salt Lake City", "UT", "84103")
p30.deadline = Time.of("10:30")
p30.mass = 1

p31 = Package(31)
p31.dest = Address.of("3365 S 900 W", "Salt Lake City", "UT", "84119")
p31.deadline = Time.of("10:30")
p31.mass = 1

p32 = Package(32)
p32.dest = Address.of("3365 S 900 Wt", "Salt Lake City", "UT", "84119")
p32.available = Time.of("09:05")
p32.mass = 1
p32.note = 'Delayed on flight---will not arrive to depot until 9:05'

p33 = Package(33)
p33.dest = Address.of("2530 S 500 E", "Salt Lake City", "UT", "84106")
p33.mass = 1

p34 = Package(34)
p34.dest = Address.of("4580 S 2300 E", "Holladay", "UT", "84117")
p34.deadline = Time.of("10:30")
p34.mass = 2

p35 = Package(35)
p35.dest = Address.of("1060 Dalton Ave S", "Salt Lake City", "UT", "84104")
p35.mass = 88

p36 = Package(36)
p36.dest = Address.of("2300 Parkway Blvd", "West Valley City", "UT", "84119")
p36.mass = 88
p36.note = 'Can only be on truck 2'
p36.truck = 2

p37 = Package(37)
p37.dest = Address.of("410 S State St", "Salt Lake City", "UT", "84111")
p37.deadline = Time.of("10:30")
p37.mass = 2

p38 = Package(38)
p38.dest = Address.of("410 S State St", "Salt Lake City", "UT", "84111")
p38.mass = 9
p38.note = 'Can only be on truck 2'
p38.truck = 2

p39 = Package(39)
p39.dest = Address.of("2010 W 500 S", "Salt Lake City", "UT", "84104")
p39.mass = 9

p40 = Package(40)
p40.dest = Address.of("380 W 2880 S", "Salt Lake City", "UT", "84115")
p40.deadline = Time.of("10:30")
p40.mass = 45

#add packages to set for export
packages = {
p1,		p2,		p3,		p4,		p5,		p6,		p7,		p8,		p9,		p10,
p11,	p12,	p13,	p14,	p15,	p16,	p17,	p18,	p19,	p20,
p21,	p22,	p23,	p24,	p25,	p26,	p27,	p28,	p29,	p30,
p31,	p32,	p33,	p34,	p35,	p36,	p37,	p38,	p39,	p40}