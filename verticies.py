"""
Represents a vertex on a graph (in this case, a destination on the downtown map);
This file also contains a matrix which stores the distances between each vertex to
complete the route graph.
"""

import xml.etree.ElementTree as ET

#Define the Vertex class
class Vertex:
    def __init__(self, id):
        self.id = id
        self.name = "N/A"
        self.address = "N/A"
        self.isHub = False

#Define Address class for use in vertex
class Address:
    def __init__(self, zip):
        self.street = ""
        self.city = ""
        self.state = "UT"
        self.zip = zip

    def __str__(self):
        str = self.street + "\n" + self.city + ", " + self.state + " " + self.zip
        return str

#Instantiate an empty set to store vertecies
routeGraph = {}

#Read in all possible delivery destinations from xml file
tree = ET.parse("resources/destinations.xml")
root = tree.getroot()

#Populate the set of verticies with information from xml file
for item in root.findall(".channel/item"):
    v = Vertex(item.attrib["id"])
    
    for child in item:
        if(child.tag == "name"):
            print(child.text)
            v.name = child.text
        elif(tag == "address"):
            a = Address(child.attrib["zip"])
            for grandchild in child:
                if(grandchild.tag == "street"):
                    a.street = grandchild.text
                elif(grandchild.tag == "city"):
                    a.city = grandchild.text
            v.address = a
    routeGraph.add(v)