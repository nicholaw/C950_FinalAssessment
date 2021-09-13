"""
Represents a delivery truck which can hold and deliver packages.
"""

#Constants
MAX_PACKAGES = 16
AVG_SPEED = 18

#Define the Truck class
class Truck:
    def __init__(self, id):
        self.id = id
        self.packages = ""
        self.dist = 0
        self.location = ""
        self.packages = Queue()

    def load_package(self, package):
        if len(self.packages < MAX_PACKAGES):
            packages.append(package)
            return True
        else:
            return False

    def execute_route(self):

class Queue:
    def __init__(self):
        self.items = []

    def offer(self, item):
        self.items.append(item)

    def pop(self):