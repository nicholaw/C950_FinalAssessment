"""
Instantiates all possible delivery destinations by reading
data from xml file
"""

from address import Address
import xml.etree.ElementTree as ET

#Create element tree from xml file and instantiate set for storing destinations
tree = ET.parse("resources/destinations.xml")
root = tree.getroot()
allLocations = set()

#Populate set from element tree
for item in root.findall(".//destination"):
	destination = Address(item.attrib["name"])
	for child in item:
		if(child.tag == "street"):
			destination.street = child.text
		elif(child.tag == "city"):
			destination.city = child.text
		elif(child.tag == "zip"):
			destination.zip = child.text
	allLocations.add(destination)

#Define distances among locations
