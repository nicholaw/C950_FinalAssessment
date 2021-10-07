"""
Instantiates all possible delivery destinations by reading
data from xml file
"""

from address import Address
import xml.etree.ElementTree as ET

#Create element tree from xml file and instantiate set for storing destinations
tree = ET.parse("resources/destinations.xml")
root = tree.getroot()
allLocations = dict()

#Returns the location with the provided name from the set of all locations
def get_location(name):
	for item in allLocations:
		if(item.name == name):
			return item
	return None

#Populate set of all locations from element tree
for item in root.findall(".//destination"):
	destination = Address(item.attrib["name"])
	for child in item:
		if(child.tag == "street"):
			destination.street = child.text
		elif(child.tag == "city"):
			destination.city = child.text
		elif(child.tag == "zip"):
			destination.zip = child.text
	allLocations[destination] = destination

#Define distances among locations
for item in root.findall(".//destination"):
	locationA = get_location(item.attrib["name"])
	for child in item:
		if(child.tag == "distances"):
			for grandchild in child:
				locationB = get_location(grandchild.attrib["name"])
				distance = float(grandchild.attrib["dist"])
				locationA.distances[locationB] = distance
				locationB.distances[locationA] = distance