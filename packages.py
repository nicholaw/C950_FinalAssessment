"""
Instantiates the set of all packages to be delivered by the C950 final assessment algorithm
"""
from address import Address
from timeofday import Time
from package import Package
import xml.etree.ElementTree as ET

#Create element tree from xml file and instantiate set for storing packages
tree = ET.parse("resources/packages.xml")
root = tree.getroot()
allPackages = set()

#Populate set of all locations from element tree
#TODO: can we maybe not have three nested for loops, please
for item in root.findall(".//package"):
	p = Package(int(item.attrib["id"]))
	for child in item:
		if (child.tag == "destination"):
			street = ""
			city = ""
			zip = ""
			for grandchild in child:
				if(grandchild.tag == "street"):
					street = grandchild.text
				elif(grandchild.tag == "city"):
					city = grandchild.text
				elif(grandchild.tag == "zip"):
					zip = grandchild.text
			p.dest = Address.of(street, city, "UT", zip)
		elif(child.tag == "weight"):
			p.mass = int(child.attrib["weight"])
		elif(child.tag == "truck"):
			p.truck = int(child.attrib["truck"])
		elif(child.tag == "deadline"):
			if(child.text == "eod"):
				p.deadline = Time.of("23:59")
			else:
				p.deadline = Time.of(child.text)
		elif(child.tag == "available"):
			if(child.text == "sod"):
				p.available = Time.of("08:00")
			else:
				p.available = Time.of(child.text)
		elif(child.tag == "note"):
			p.note = child.text
		"""
		elif(child.tag == "group"):
			try:
				text = child.text
				i = 0
				num = ""
				while(i < len(text)):
					if(text[i] == ","):
						p.group.add(int(num))
						num = ""
					else:
						num += text[i]
				p.group.add(int(num))
			except TypeError:
				continue
		"""
	allPackages.add(p)

#Assemble any package groups