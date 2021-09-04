"""
File which contains each package to be delievered for the C950 final assessment
"""

from package import Package

#instantiate the packages
p1 = Package(1)
p1.dest = '195 W Oakland Ave'
p1.city = 'Salt Lake City'
p1.state = 'UT'
p1.zip = 84115
p1.deadline = 1030
p1.mass = 21
p1.note = ''
p1.truck = -1

p2 = Package(2)
p2.dest = '2530 S 500 E'
p2.city = 'Salt Lake City'
p2.state = 'UT'
p2.zip = 84106
p2.deadline = 2359
p2.mass = 44
p2.note = ''
p2.truck = -1

p3 = Package(3)
p1.dest = '233 Canyon Rd'
p1.city = 'Salt Lake City'
p1.state = 'UT'
p1.zip = 84103
p1.deadline = 2359
p1.mass = 2
p1.note = 'Can only be on truck 2'
p1.truck = 2

p4 = Package(4)
p1.dest = '380 W 2880 S'
p1.city = 'Salt Lake City'
p1.state = 'UT'
p1.zip = 84115
p1.deadline = 2359
p1.mass = 4
p1.note = ''
p1.truck = -1

p5 = Package(5)
p1.dest = '410 S State St'
p1.city = 'Salt Lake City'
p1.state = 'UT'
p1.zip = 84111
p1.deadline = 2359
p1.mass = 5
p1.note = ''
p1.truck = -1

p6 = Package(6)
p1.dest = '3060 Lester St'
p1.city = 'West Valley City'
p1.state = 'UT'
p1.zip = 84119
p1.available = 0905
p1.deadline = 1030
p1.mass = 88
p1.note = 'Delayed on flight---will not arrive to depot until 09:05'
p1.truck = -1

p7 = Package(7)
p1.dest = '1330 2100 S'
p1.city = 'Salt Lake City'
p1.state = 'UT'
p1.zip = 84106
p1.deadline = 2359
p1.mass = 8
p1.note = ''
p1.truck = -1

p8 = Package(8)
p1.dest = '300 State Street'
p1.city = 'Salt Lake City'
p1.state = 'UT'
p1.zip = 84103
p1.deadline = 2359
p1.mass = 9
p1.note = ''
p1.truck = -1

p9 = Package(9)
p1.dest = '300 State Street'
p1.city = 'Salt Lake City'
p1.state = 'UT'
p1.zip = 84103
p1.deadline = 2359
p1.mass = 2
p1.note = 'Wrong address listed'
p1.truck = -1

p10 = Package(10)
p10.dest = '600 E 900 S'
p10.city = 'Salt Lake City'
p10.state = 'UT'
p10.zip = 84105
p10.deadline = 2359
p10.mass = 1
p10.note = ''
p10.truck = -1

p11 = Package(11)
p11.dest = '2600 Taylorsville Blvd'
p11.city = 'Salt Lake City'
p11.state = 'UT'
p11.zip = 84118
p11.deadline = 2359
p11.mass = 1
p11.note = ''
p11.truck = -1

p12 = Package(12)
p12.dest = '3575 W Valley Central Station'
p12.city = 'West Valley'
p12.state = 'UT'
p12.zip = 84119
p12.deadline = 2359
p12.mass = 1
p12.note = ''
p12.truck = -1

p13 = Package(13)
p13.dest = '2010 W 500 S'
p13.city = 'Salt Lake City'
p13.state = 'UT'
p13.zip = 84104
p13.deadline = 1030
p13.mass = 2
p13.note = ''
p13.truck = -1

p14 = Package(14)
p14.dest = '4300 S 1300 E'
p14.city = 'Millcreek'
p14.state = 'UT'
p14.zip = 84117
p14.deadline = 1030
p14.mass = 88
p14.note = 'Must be delivered with 15, 19'
p14.truck = -1
p14.group = {14, 15, 19}

p15 = Package(15)
p1.dest = '4580 S 2300 E'
p1.city = 'Holladay'
p1.state = 'UT'
p1.zip = 84117
p1.deadline = 0900
p1.mass = 4
p1.note = ''
p1.truck = -1

p16 = Package(16)
p1.dest = '4580 S 2300 E'
p1.city = 'Holladay'
p1.state = 'UT'
p1.zip = 84117
p1.deadline = 1030
p1.mass = 88
p1.note = 'Must be delivered with 13, 19'
p1.truck = -1
p16.group = {13, 16, 19}

p17 = Package(17)
p1.dest = '3148 S 1100 W'
p1.city = 'Salt Lake City'
p1.state = 'UT'
p1.zip = 84119
p1.deadline = 2359
p1.mass = 2
p1.note = ''
p1.truck = -1

p18 = Package(18)
p1.dest = '1488 4800 S'
p1.city = 'Salt Lake City'
p1.state = 'UT'
p1.zip = 84123
p1.deadline = 2359
p1.mass = 6
p1.note = 'Can only be on truck 2'
p1.truck = 2

p19 = Package(19)
p1.dest = '177 W Price Ave'
p1.city = 'Salt Lake City'
p1.state = 'UT'
p1.zip = 84115
p1.deadline = 2359
p1.mass = 37
p1.note = ''
p1.truck = -1

p20 = Package(20)
p20.dest = '3595 Main St'
p20.city = 'Salt Lake City'
p20.state = 'UT'
p20.zip = 84115
p20.deadline = 1030
p20.mass = 37
p20.note = 'Must be delivered with 13, 15'
p20.truck = -1
p20.group = {13, 15, 20}

p21 = Package(21)
p20.dest = '3595 Main St'
p20.city = 'Salt Lake City'
p20.state = 'UT'
p20.zip = 84115
p20.mass = 3

p22 = Package(22)
p20.dest = '6351 South 900 East'
p20.city = 'Murray'
p20.state = 'UT'
p20.zip = 84121
p20.mass = 2

p23 = Package(23)
p20.dest = '5100 South 2700 West'
p20.city = 'Salt Lake City'
p20.state = 'UT'
p20.zip = 84118
p20.mass = 5

p24 = Package(24)
p20.dest = '5025 State St'
p20.city = 'Murray'
p20.state = 'UT'
p20.zip = 84107
p20.mass = 7

p25 = Package(25)
p20.dest = '5383 South 900 East #104'
p20.city = 'Salt Lake City'
p20.state = 'UT'
p20.zip = 84117
p25.available = 0905
p25.deadline = 1030
p20.mass = 7
p25.note = 'Delayed on flight---will not arrive to depot until 9:05'

p26 = Package(26)
p27 = Package(27)
p28 = Package(28)
p29 = Package(29)
p30 = Package(30)
p31 = Package(31)
p32 = Package(32)
p33 = Package(33)
p34 = Package(34)
p35 = Package(35)
p36 = Package(36)
p37 = Package(37)
p38 = Package(38)
p39 = Package(39)
p40 = Package(40)

#add the packages to a set
packages = {
p1,		p2,		p3,		p4,		p5,		p6,		p7,		p8,		p9,		p10,
p11,	p12,	p13,	p14,	p15,	p16,	p17,	p18,	p19,	p20,
p21,	p22,	p23,	p24,	p25,	p26,	p27,	p28,	p29,	p30,
p31,	p32,	p33,	p34,	p35,	p36,	p37,	p38,	p39,	p40}