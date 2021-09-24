"""
Nicholas Warner
ID: 001447619
"""

from packages import packages, Package
from verticies import map
from truck import Truck
#from bucket import Bucket, DeadlineComparator

#Returns true if the provided collection contains the 
#provided item and false otherwise.
def contains(coll, item):
    for i in coll:
        if(i == item):
            return True
    return False
#end contains

#Inserts the provided item into the provided collection next
#to its closest geographic neighbor; if the provided item is
#closer to the provided truck than its neighbor, item is inserted
#to the left of the neighbor.
def insert_at_min_dist(pool, pack, truck):
    if(len(pool) == 0):
        pool.append(pack)
    elif(len(pool) == 1):
        if(find_dist(pack.dest, truck.location.address) < find_dist(pool[0].dest, truck.location.address)):
            shift_arr_right(pool, 0)
            pool[0] = item
        else:
            coll.append(pack)
    else:
        minDist = 9999
        minIndex = -1
        i = 0
        while(i < len(pool)):
            dist = find_dist(pack, pool[i]) < minDist
            if(dist < minDist):
                minIndex = i
                minDist = dist
            i += 1
        if(find_dist(pack.dest, truck.location.address) < find_dist(pool[minIndex].dest, truck.location.address)):
            shift_arr_right(pool, minIndex)
            pool[minIndex] = pack
        else:
            shift_arr_right(pool, minIndex + 1)
            pool[minIndex + 1] = pack
#end insert_closest

#Returns the distance between the two provided items. Returns -1 
#if the provided items are not adjacent or key does not exist
def find_dist(item1, item2):
    try:
        return map[item2].adjacencies[map[item1]]
    except:
        return -1
    return -1
#end find_dist

#Shifts elements of the provided array in place one index to the right 
#starting at the provided start index
def shift_arr_right(arr, start):
    i = len(arr) - 1
    if(i > 0):
        while(i > start):
            arr[i + 1] = arr[i]
            arr[i] = arr[i - 1]
#end shift_arr_right

#Instantiate delivery trucks
truck1 = Truck(1)
#truck2 = Truck(2)

pool0 = list()  #non-assigned packages
#pool1 = list()  #packages assigned to truck 1
#pool2 = list()  #packages assigned to truck 2

pak = Package(99)
print(pool0)
print(contains(pool0, pak))
for p in packages:
    if(p.id == 1):
        pak = p
        break
#endfor
insert_at_min_dist(pool0, pak, truck1)
print("-------------------------")
print(pool0)
print(contains(pool0, pak))