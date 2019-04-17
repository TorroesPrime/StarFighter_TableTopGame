from objects_fighters import *
from objects_pilots import *
from strings import linebreak,header
count = 0
for fighter in KIL_fighters:
    for pilot in pilotsKilrathi:
        cost = pilot.getCost() + fighter.getCost()
        if cost < 500:
            print(linebreak)
            print(header)
            print("Pilot: "+pilot.getName())
            print("Fighter: "+fighter.name)
            print(cost)
            count += 1
print(count)
count = 0
for fighter in CON_fighters:
    for pilot in pilotsConfed:
        cost = pilot.getCost() + fighter.getCost()
        if cost < 500:
            print(linebreak)
            print(header)
            print("Pilot: "+pilot.getName())
            print("Fighter: "+fighter.name)
            print(cost)
            count += 1
print(count)