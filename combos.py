from objects_fighters import *
from objects_pilots import *
from strings import linebreak,header
count = 0
document = open('500_points.txt','w')
for fighter in KIL_fighters:
    for pilot in pilotsKilrathi:
        cost = pilot.getCost() + fighter.getCost()
        if cost < 500:
            char_write = str(pilot.getName())+str(ship)+' in a '
            ship = "Fighter: "+fighter.name 
            space = 67-len(char_write)
            spaces = str(' '*space)
            document.write(str(pilot.getName())+' in a '+str(fighter.name)+spaces+"-"+str(cost)+"\n")
            count += 1

for fighter in CON_fighters:
    for pilot in pilotsConfed:
        cost = pilot.getCost() + fighter.getCost()
        if cost < 500:
            char_write = str(pilot.getName())+str(ship)+' in a '
            ship = "Fighter: "+fighter.name 
            space = 67-len(char_write)
            spaces = str(' '*space)
            document.write(str(pilot.getName())+' in a '+str(fighter.name)+spaces+"-"+str(cost)+"\n")
            count += 1
document.close()
print(count)

