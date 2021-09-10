"""
Represents a vertex on a graph (in this case, a destination on the downtown map);
Each vertex contains a list of adjacent verticies with their distances in miles.
"""

#Define the Vertex class
class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.adjacencies = {}

    def add_adjacency(adjacentVertex, distance):
        self.adjacencies[adjacentVertex] = distance

#Instantiate provided downtown destinations

#Define adjacencies

#Add vertecies to set to be used as the graph