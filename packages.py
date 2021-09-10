"""
File which contains each package to be delievered for the C950 final assessment
"""

#define Package class
class Package:
	def __init__(self, id):
		self.id = id
		self.dest = ''
		self.city = ''
		self.state = ''
		self.zip = ''
		self.available = 100
		self.deadline = 2359
		self.mass = 1
		self.note = ''
		self.truck = -1
		self.group = {}
        self.delivered = False
        self.time_delivered = ""
        
#instantiate the packages
p1 = Package(1)
p1.dest = '195 W Oakland Ave'
p1.city = 'Salt Lake City'
p1.state = 'UT'
p1.zip = 84115
p1.deadline = 1030
p1.mass = 21

p2 = Package(2)
p2.dest = '2530 S 500 E'
p2.city = 'Salt Lake City'
p2.state = 'UT'
p2.zip = 84106
p2.mass = 44

p3 = Package(3)
p3.dest = '233 Canyon Rd'
p3.city = 'Salt Lake City'
p3.state = 'UT'
p3.zip = 84103
p3.mass = 2
p3.note = 'Can only be on truck 2'
p3.truck = 2

p4 = Package(4)
p4.dest = '380 W 2880 S'
p4.city = 'Salt Lake City'
p4.state = 'UT'
p4.zip = 84115
p4.mass = 4

p5 = Package(5)
p5.dest = '410 S State St'
p5.city = 'Salt Lake City'
p5.state = 'UT'
p5.zip = 84111
p5.mass = 5

p6 = Package(6)
p6.dest = '3060 Lester St'
p6.city = 'West Valley City'
p6.state = 'UT'
p6.zip = 84119
p6.available = 905
p6.deadline = 1030
p6.mass = 88
p6.note = 'Delayed on flight---will not arrive to depot until 09:05'

p7 = Package(7)
p7.dest = '1330 2100 S'
p7.city = 'Salt Lake City'
p7.state = 'UT'
p7.zip = 84106
p7.mass = 8

p8 = Package(8)
p8.dest = '300 State Street'
p8.city = 'Salt Lake City'
p8.state = 'UT'
p8.zip = 84103
p8.mass = 9

p9 = Package(9)
p9.dest = '300 State Street'
p9.city = 'Salt Lake City'
p9.state = 'UT'
p9.zip = 84103
p9.mass = 2
p9.note = 'Wrong address listed'

p10 = Package(10)
p10.dest = '600 E 900 S'
p10.city = 'Salt Lake City'
p10.state = 'UT'
p10.zip = 84105
p10.mass = 1

p11 = Package(11)
p11.dest = '2600 Taylorsville Blvd'
p11.city = 'Salt Lake City'
p11.state = 'UT'
p11.zip = 84118
p11.mass = 1

p12 = Package(12)
p12.dest = '3575 W Valley Central Station'
p12.city = 'West Valley'
p12.state = 'UT'
p12.zip = 84119
p12.mass = 1

p13 = Package(13)
p13.dest = '2010 W 500 S'
p13.city = 'Salt Lake City'
p13.state = 'UT'
p13.zip = 84104
p13.deadline = 1030

p14 = Package(14)
p14.dest = '4300 S 1300 E'
p14.city = 'Millcreek'
p14.state = 'UT'
p14.zip = 84117
p14.deadline = 1030
p14.mass = 88
p14.note = 'Must be delivered with 15, 19'
p14.group = {14, 15, 19}

p15 = Package(15)
p15.dest = '4580 S 2300 E'
p15.city = 'Holladay'
p15.state = 'UT'
p15.zip = 84117
p15.deadline = 900
p15.mass = 4

p16 = Package(16)
p16.dest = '4580 S 2300 E'
p16.city = 'Holladay'
p16.state = 'UT'
p16.zip = 84117
p16.deadline = 1030
p16.mass = 88
p16.note = 'Must be delivered with 13, 19'
p16.group = {13, 16, 19}

p17 = Package(17)
p17.dest = '3148 S 1100 W'
p17.city = 'Salt Lake City'
p17.state = 'UT'
p17.zip = 84119
p17.mass = 2

p18 = Package(18)
p18.dest = '1488 4800 S'
p18.city = 'Salt Lake City'
p18.state = 'UT'
p18.zip = 84123
p18.mass = 6
p18.note = 'Can only be on truck 2'
p18.truck = 2

p19 = Package(19)
p19.dest = '177 W Price Ave'
p19.city = 'Salt Lake City'
p19.state = 'UT'
p19.zip = 84115
p19.mass = 37

p20 = Package(20)
p20.dest = '3595 Main St'
p20.city = 'Salt Lake City'
p20.state = 'UT'
p20.zip = 84115
p20.deadline = 1030
p20.mass = 37
p20.note = 'Must be delivered with 13, 15'
p20.group = {13, 15, 20}

p21 = Package(21)
p21.dest = '3595 Main St'
p21.city = 'Salt Lake City'
p21.state = 'UT'
p21.zip = 84115
p21.mass = 3

p22 = Package(22)
p22.dest = '6351 South 900 East'
p22.city = 'Murray'
p22.state = 'UT'
p22.zip = 84121
p22.mass = 2

p23 = Package(23)
p23.dest = '5100 South 2700 West'
p23.city = 'Salt Lake City'
p23.state = 'UT'
p23.zip = 84118
p23.mass = 5

p24 = Package(24)
p24.dest = '5025 State St'
p24.city = 'Murray'
p24.state = 'UT'
p24.zip = 84107
p24.mass = 7

p25 = Package(25)
p25.dest = '5383 South 900 East #104'
p25.city = 'Salt Lake City'
p25.state = 'UT'
p25.zip = 84117
p25.available = 905
p25.deadline = 1030
p25.mass = 7
p25.note = 'Delayed on flight---will not arrive to depot until 9:05'

p26 = Package(26)
p26.dest = '5383 South 900 East #104'
p26.city = 'Salt Lake City'
p26.state = 'UT'
p26.zip = 84117
p26.mass = 25

p27 = Package(27)
p27.dest = '1060 Dalton Ave S'
p27.city = 'Salt Lake City'
p27.state = 'UT'
p27.zip = 84104
p27.mass = 5

p28 = Package(28)
p28.dest = '2835 Main St'
p28.city = 'Salt Lake City'
p28.state = 'UT'
p28.zip = 84115
p28.available = 905
p28.mass = 7
p28.note = 'Delayed on flight---will not arrive to depot until 9:05'

p29 = Package(29)
p29.dest = '1330 2100 S'
p29.city = 'Salt Lake City'
p29.state = 'UT'
p29.zip = 84106
p29.deadline = 1030
p29.mass = 2

p30 = Package(30)
p30.dest = '300 State St'
p30.city = 'Salt Lake City'
p30.state = 'UT'
p30.zip = 84103
p30.deadline = 1030
p30.mass = 1

p31 = Package(31)
p31.dest = '3365 S 900 W'
p31.city = 'Salt Lake City'
p31.state = 'UT'
p31.zip = 84119
p31.deadline = 1030
p31.mass = 1

p32 = Package(32)
p32.dest = '3365 S 900 W'
p32.city = 'Salt Lake City'
p32.state = 'UT'
p32.zip = 84119
p32.available = 905
p32.mass = 1
p32.note = 'Delayed on flight---will not arrive to depot until 9:05'

p33 = Package(33)
p33.dest = '2530 S 500 E'
p33.city = 'Salt Lake City'
p33.state = 'UT'
p33.zip = 84106
p33.mass = 1

p34 = Package(34)
p34.dest = '4580 S 2300 E'
p34.city = 'Holladay'
p34.state = 'UT'
p34.zip = 84117
p34.deadline = 1030
p34.mass = 2

p35 = Package(35)
p35.dest = '1060 Dalton Ave S'
p35.city = 'Salt Lake City'
p35.state = 'UT'
p35.zip = 84104
p35.mass = 88

p36 = Package(36)
p36.dest = '2300 Parkway Blvd'
p36.city = 'West Valley City'
p36.state = 'UT'
p36.zip = 84119
p36.mass = 88
p36.note = 'Can only be on truck 2'
p36.truck = 2

p37 = Package(37)
p37.dest = '410 S State St'
p37.city = 'Salt Lake City'
p37.state = 'UT'
p37.zip = 84111
p37.deadline = 1030
p37.mass = 2

p38 = Package(38)
p38.dest = '410 S State St'
p38.city = 'Salt Lake City'
p38.state = 'UT'
p38.zip = 84111
p38.mass = 9
p38.note = 'Can only be on truck 2'
p38.truck = 2

p39 = Package(39)
p39.dest = '2010 W 500 S'
p39.city = 'Salt Lake City'
p39.state = 'UT'
p39.zip = 84104
p39.mass = 9

p40 = Package(40)
p40.dest = '380 W 2880 S'
p40.city = 'Salt Lake City'
p40.state = 'UT'
p40.zip = 84115
p40.deadline = 1030
p40.mass = 45

#add packages to a set
packages = {
p1,		p2,		p3,		p4,		p5,		p6,		p7,		p8,		p9,		p10,
p11,	p12,	p13,	p14,	p15,	p16,	p17,	p18,	p19,	p20,
p21,	p22,	p23,	p24,	p25,	p26,	p27,	p28,	p29,	p30,
p31,	p32,	p33,	p34,	p35,	p36,	p37,	p38,	p39,	p40}