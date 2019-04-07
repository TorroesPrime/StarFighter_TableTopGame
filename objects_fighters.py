from class_ship import ship
from objects_canons import *
from test_control import test
abilities = {"sabre":"The F-57B Sabre mounts a computer controleld rear turret that covers its rear quadrant. \
This weapon fires independently of the main ship allowing it to target a different ship to the pilot themselves\
. The Turret has a Gunnery Skill of 4 and mounts 2 Neutron Guns.",
"F-103A": "The F-103A Excalibur conveys a +1 bonus to all gunnery skill checks the pilot is called on to make.\
You may re-roll the first 'miss' result you get each game turn.",
"F-107":"The Pilot of the Lance gains a +2 bonus to any gunnery skill tests they are called on to make. The \
Lance counts has having 1 more energy token in it's cannon slot then normal.",
"F-109B":"The Vampire poccesses exception maneuverability. When turning beyond its normal turn allowance, only \
only perform a pilot skill test for every 2 degrees of turn instead of the normal 1.",
"none":"",
"TB-80A":"The TB-80A Devastator mounts computer controlled Turrets that cover it's right, left, and rear quadrants\
. Each turret is independently controlled and can acquire and shoot at their own targets. Each of the Turrets are \
armed with a single laser canon and count has having a Gunnery skill of 5.",
"KRF-07C":"So long as the Bloodfang has 22 or more hit points remaining, you may re-roll damage checks you are\
 called on to make. The Bloodfang regenerates 1 more shield point per turn then it would normally so long as\
 it's shields have not been destroyed.",
 "A-17A":"The A-17A Broadsword mounts turrets that cover its right, left and rear quadrants. Each turret is\
independently controlled by either a computer system that counts has having a gunnery skill of 4, or can be\
manned by a pilot. each turret is armed with twin neutron guns. These turrets can aim at and fire at targets\
independent of the pilot of the Broadsword itself.",
"F-64a":"The Banshee mounts a redundant battery system tied directly to its shields. The Banshee can refenerate\
1 additional shield point per turn then it would normally be capable of, so long as it's shields have not been\
destroyed.",
"F-104a":"The F-104 Bearcat conveys a +2 gunnery skill bonus to any shooting attacks the pilot is calld on to\
 make. The pilot also gains 2 free re-rolls that may be used anywhere the player deems to use them during the\
 game."}

#(name, faction, burn, turn, shields, hullpoints, evasive_meassures, ability, Guns_number, canon, LoadOut):
evasiveMeassures = ('Decoy',2)
fighters = []
f86c = ship("F-86C Hellcat V Assault Fighter","Confed",9,6,25,10,evasiveMeassures,"",2,Neutron,4)
fighters.append(f86c)
evasiveMeassures = ('Decoy',6)
kf65B = ship("KF-65B Dralthi IV","Kilrathi",8,6,12,8,evasiveMeassures,"",3,Meson,4)
fighters.append(kf65B)
evasiveMeassures = ('Flares',8)
F57B = ship("F-57B Sabre","Confed",7,8,10,16,evasiveMeassures,abilities["sabre"],4,Particle,4)
fighters.append(F57B)
evasiveMeassures = ('Decoy',4)
F103A = ship("F-103A Excalibur","Confed",7,9,25,11,evasiveMeassures,abilities["F-103A"],4,Tachyon,12)
fighters.append(F103A)
evasiveMeassures = ('Decoy',12)
F107 = ship("F-107 Lance","Confed",9,7,50,30,evasiveMeassures,abilities["F-107"],4,PlasmaG,8)
fighters.append(F107)
evasiveMeassures = ('Decoy',8)
F109B = ship("F-109B Vampire","Confed",6,13,29,32,evasiveMeassures,abilities["F-109B"],4,Tachyon,6)
fighters.append(F109B)
evasiveMeassures = ('Decoy',3)
KB600B = ship("KB-600B Paktahn Bomber","Kilrathi",4,4,32,16,evasiveMeassures,abilities["none"],3,PlasmaG,9)
fighters.append(KB600B)
evasiveMeassures = ('Flares',2)
KF009A = ship("KF-09A Dralthi II","Kilrathi",4,11,5,8,evasiveMeassures,abilities["none"],2,Laser,2)
fighters.append(KF009A)
evasiveMeassures = ('Decoy',8)
TB76A = ship("TB-76A Longbow Heavy Bomber","Confed",5,3,50,30,evasiveMeassures,abilities["none"],4,PlasmaG,2)
fighters.append(TB76A)
evasiveMeassures = ('Decoy',12)
TB80A = ship("TB-80A Devastator Heavy Bomber","Confed",3,3,43,40,evasiveMeassures,abilities["TB-80A"],1,PlasmaC,16)
fighters.append(TB80A)
evasiveMeassures = ('Decoy',2)
KRF07C = ship("KRF-07C Bloodfang","Kilrathi",9,8,10,33,evasiveMeassures,abilities["KRF-07C"],2,PlasmaR,2)
fighters.append(KRF07C)
evasiveMeassures = ('Flares',4)
A17a = ship("A-17A Broadsword","Confed",4,1,18,15,evasiveMeassures,abilities["A-17A"],2,Massdriver,8)
fighters.append(A17a)
evasiveMeassures = ('Decoy',4)
F64a = ship("F-64a Banshee","UBW",7,9,25,8,evasiveMeassures,abilities["F-64a"],4,Laser,4)
fighters.append(F64a)
evasiveMeassures = ('Decoy',4)
F104 = ship("F-104 Bearcat","UBW",9,9,28,15,evasiveMeassures,abilities["F-104a"],4,Tachyon,8)
fighters.append(F104)
evasiveMeassures = ('Decoy',4)
F104 = ship("F-104 Bearcat","Confed",9,9,28,15,evasiveMeassures,abilities["F-104a"],4,Tachyon,8)
fighters.append(F104)
evasiveMeassures = ('Decoy',4)
X101 = ship("X-101 Test","Test",9,9,9,9,evasiveMeassures,abilities["none"],4,Tachyon,8)
fighters.append(X101)
evasiveMeassures = ('Flares',8)
A14 = ship("A-14 Raptor","Confed",4,5,12,10,evasiveMeassures,abilities["none"],4,Massdriver,8)
fighters.append(A14)
evasiveMeassures = ('Flares',6)
A17 = ship("A-17 Broadsword","Confed",8,3,18,15,evasiveMeassures,abilities["none"],3,Massdriver,3)
fighters.append(A17)
evasiveMeassures = ('Decoy',1)
F27C = ship("F-27C Arrow","Confed",4,6,16,10,evasiveMeassures,abilities["none"],2,Ion,2)
fighters.append(F27C)
evasiveMeassures = ('Decoy',1)
Y105A = ship("Y-105a","Confed",4,6,8,10,evasiveMeassures,abilities["none"],4,Photon,2)
fighters.append(Y105A)
if test_control.test:
    for fighter in fighters:
        fighter.card()
