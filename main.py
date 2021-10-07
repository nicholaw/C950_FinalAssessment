"""
Launches C950 parcel delivery algorithm
"""

from timeofday import Time
from controller import Controller

controller = Controller(2, Time.of("08:00"), "Western Governors University")
controller.start()
print("Deliveries: " + str(controller.packagesDelivered))
print("Time: " + str(controller.globalTime))