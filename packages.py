"""
Instantiates the set of all packages to be delivered by the C950 final assessment algorithm
"""
from address import Address
from timeofday import Time
from package import Package
from packagegroup import PackageGroup
import xml.etree.ElementTree as ET

#Create element tree from xml file and instantiate set for storing packages
tree = ET.parse("resources/packages.xml")
root = tree.getroot()

#Initialize data structures for storing and organizing packages
allPackages = dict()          				#all packages to be delivered today
hasGroup = set()              				#all packages which must be delivered with other specified packages
allGroups = set()             					#all distinct groups of packages
finalGroups = PackageGroup()  	#after groups merged to avoid intersections among groups

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
                p.deadline = None
            else:
                p.deadline = Time.of(child.text)
        elif(child.tag == "available"):
            if(child.text == "sod"):
                p.available = Time.of("08:00")
            else:
                p.available = Time.of(child.text)
        elif(child.tag == "note"):
            p.note = child.text
        elif(child.tag == "group"):
            text = child.text
            if(text != None):
                i = 0
                num = ""
                while(i < len(text)):
                    if(text[i] == ","):
                        p.group.add(int(num))
                        num = ""
                    else:
                        num += text[i]
                    i += 1
                p.group.add(int(num))
                hasGroup.add(p)
    allPackages[p.id] = p

#Assemble any package groups
for p in hasGroup:
    newGroup = PackageGroup()
    newGroup.insert(p)
    for id in p.group:
        newGroup.insert(allPackages[id])
    allGroups.add(newGroup)
    
#Merge any groups whose intersection is not the empty set
finalGroups  = PackageGroup()
for g in allGroups:
    finalGroups.insert_group(g)

g = 1
for group in finalGroups.group:
	print("Group #" + str(g))
	g += 1
	for p in group.group:
		print("Package #" + str(p.id))
	print("\n----------------------------------------------------")