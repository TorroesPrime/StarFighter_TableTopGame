from class_ship import ship, EvasiveMessuresNames as EMN, abilities
from objects_canons import *
from test_control import test
from lists import faction as f,KIL_fighters,CON_fighters,UBW_fighters,BL_fighters,REN_fighters
import random

fighters = [ship("F-86C Hellcat V Assault Fighter",f[1],9,6,25,10,(EMN[1],4),abilities["F-86C"],2,Neutron,4),
            ship("KHFA-983A Darket",f[4],7,7,8,2,(EMN[1],3),abilities["KHFA-983A"],3,Laser,2),
            ship("KSF-119B Strakha",f[4],6,4,4,4,(EMN[1],1),abilities["KSF-119B"],4,Meson,8),
            ship("KHFB-1066C VokToth",f[4],7,5,25,13,(EMN[1],4),abilities["KHFB-1066C"],4,Meson,8),
            ship("HF-66A Thunderbolt",f[1],7,5,25,12,(EMN[1],5),abilities["HF-66A"],4,Photon,2),
            ship("FA-36A Hornet",f[1],9,4,3,3,(EMN[1],1),abilities["FA-36A"],2,Laser,2),
            ship("F-27C Arrow",f[1],4,6,16,10,(EMN[1],1),abilities["none"],2,Ion,2),
            ship("A-17 Broadsword",f[1],8,3,18,15,(EMN[1],6),abilities["none"],3,Massdriver,3),
            ship("A-14 Raptor",f[1],4,5,12,10,(EMN[1],8),abilities["none"],4,Massdriver,8),
            ship("F-104 Bearcat",f[1],9,9,28,15,(EMN[1],4),abilities["F-104a"],4,Tachyon,8),
            ship("F-64a Banshee",f[5],7,9,25,8,(EMN[1],4),abilities["F-64a"],4,Laser,4),
            ship("A-17A Broadsword",f[1],4,1,18,15,(EMN[1],4),abilities["A-17A"],2,Massdriver,8),
            ship("KRF-07C Bloodfang",f[4],9,8,10,33,(EMN[1],2),abilities["KRF-07C"],2,PlasmaR,2),
            ship("TB-80A Devastator Heavy Bomber",f[1],3,3,43,40,(EMN[1],12),abilities["TB-80A"],1,PlasmaC,16),
            ship("TB-76A Longbow Heavy Bomber",f[1],5,3,50,30,(EMN[1],8),abilities["none"],4,PlasmaG,2),
            ship("KF-09A Dralthi II",f[4],4,11,5,8,(EMN[1],2),abilities["none"],2,Laser,2),
            ship("KB-600B Paktahn Bomber",f[4],4,4,32,16,(EMN[1],3),abilities["none"],3,PlasmaG,9),
            ship("F-109B Vampire",f[1],6,13,29,32,(EMN[1],8),abilities["F-109B"],4,Tachyon,6),
            ship("F-107 Lance",f[1],9,7,50,30,(EMN[1],12),abilities["F-107"],4,PlasmaG,8),
            ship("F-103A Excalibur",f[1],7,9,25,11,(EMN[1],4),abilities["F-103A"],4,Tachyon,12),
            ship("F-57B Sabre",f[1],7,8,10,16,(EMN[1],8),abilities["sabre"],4,Particle,4),
            ship("KF-65B Dralthi IV",f[4],8,6,12,8,(EMN[1],6),"",3,Meson,4),
            ship("F-86C Hellcat V Assault Fighter",f[1],9,6,25,10,(EMN[1],4),abilities["F-86C"],2,Neutron,4),
            ship("UFB-115B Avenger Torpedoes Bomber",f[5],6,3,25,10,(EMN[1],12),abilities["UFB-115B"],2,Neutron,4),
            ship("UFB-74B Vindicator",f[5],6,3,25,10,(EMN[1],12),abilities["UFB-74B"],2,Tachyon,4)
            ]

for fighter in fighters:
    if fighter.faction == f[1]:
        CON_fighters.append(fighter)
    elif fighter.faction == f[2]:
        BL_fighters.append(fighter)
    elif fighter.faction == f[3]:
        REN_fighters.append(fighter)
    elif fighter.faction == f[4]:
        KIL_fighters.append(fighter)
    elif fighter.faction == f[5]:
        UBW_fighters.append(fighter)






