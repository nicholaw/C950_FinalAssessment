"""
Represents a vertex on a graph (in this case, a destination on the downtown map);
This file also contains a matrix which stores the distances between each vertex to
complete the route graph.
"""

#Define the Vertex class
class Vertex:
    def __init__(self, id, name, zip):
        self.id = id
        self.name = name
        self.address = ""
        self.zip = zip
        self.adjacencies = {}
        self.isHub = False

    def hash_vertex(vertex):
        return 0

#Instantiate provided downtown destinations
v1 = Vertex(1, "Western Governors Uninversity", 84107)
v1.address = "4001 South 700 East"
v1.isHub = True

#Define adjacencies

#Add vertecies to set to be used as the graph
routeGraph = {}