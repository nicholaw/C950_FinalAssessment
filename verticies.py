"""
Represents a vertex on a graph (in this case, a destination on the downtown map);
This file also populates destination information and contains a matrix which 
stores the distances between each vertex to complete the route graph.
"""

import xml.etree.ElementTree as ET

#Define the Vertex class
class Vertex:
	def __init__(self, id):
		self.id = id
		self.name = "N/A"
		self.address = "N/A"
		self.isHub = False
		self.adjacencies = list()

	def __str__(self):
		string = "(" + str(self.id) + ")" + self.name
		return string

	def __hash__(self):
		return self.address.__hash__()

#Define Address class for use in vertex
class Address:
    def __init__(self, zip):
        self.street = ""
        self.city = ""
        self.state = "UT"
        self.zip = zip

    def of(street, city, state, zip):
        address = Address(zip)
        address.street = street
        address.city = city
        address.state = state
        return address

    def __str__(self):
        str = self.street + "\n" + self.city + ", " + self.state + " " + self.zip
        return str

    def __hash__(self):
        hash = 2729
        primeMultiplier = 83
        string = "" + self.street + self.city + self.state + self.zip
        for char in string:
            hash = hash * primeMultiplier + ord(char)
        return hash % 128
    
    def __eq__(self, other):
        if(type(self) != type(other)):
            return False
        if(self.zip != other.zip):
            return False
        if(self.state != other.state):
            return False
        if(self.city != other.city):
            return False
        if(self.street != other.street):
            return False
        return True

#Instantiate an empty set to store vertecies
map = dict()
HUB_VERTEX = ""

#Read in all possible delivery destinations from xml file
tree = ET.parse("resources/destinations.xml")
root = tree.getroot()

#Populate the set of verticies with information from xml file
for item in root.findall(".//destination"):
    v = Vertex(int(item.attrib["id"]))
    if(v.id == 0):
        v.isHub = True
        HUB_VERTEX = v
    
    for child in item:
        if(child.tag == "name"):
            v.name = child.text
        elif(child.tag == "address"):
            a = Address(child.attrib["zip"])
            for grandchild in child:
                if(grandchild.tag == "street"):
                    a.street = grandchild.text
                elif(grandchild.tag == "city"):
                    a.city = grandchild.text
            v.address = a
        elif(child.tag == "distances"):
            text = "".join((child.text).split())
            distances = list()
            count = 0
            num = ""
            for char in text:
                if(char == "," or char == "]"):
                    distances.insert(count, float(num))
                    num = ""
                    count = count + 1
                elif(char == "["):
                    continue
                else:
                    num = num + char
            v.adjacencies = distances
    map[v.address] = v