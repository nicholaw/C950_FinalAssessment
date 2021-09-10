"""
Nicholas Warner
ID: 001447619
"""

from packages import Package,packages
from truck import Truck

for p in packages:
    id = p.id
    mass = p.mass
    note = p.note
    print(f"ID: {id}\tMASS: {mass}\tNOTE: {note}")