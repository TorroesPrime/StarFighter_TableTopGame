from objects_fighters import abilities
from class_ship import ship, EvasiveMessuresNames as EMN
from objects_canons import *
from test_control import test
#name, faction, burn, turn, shields, hullpoints, evasive_meassures, ability, Guns_number, canon, LoadOut
ship1 = ship("KHBA-983A Darket","Kitrathi",7,7,8,2,(EMN[3],1),abilities["KHFA-983A"],3,Laser,20)
ship1.setCost(170)
ship1.card()

print((EMN[1]))
