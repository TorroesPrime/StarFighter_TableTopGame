from class_canons import *
import test_control
#(self,name,can_range,can_damage,can_shots,can_special,cost):
Tachyon = cannons("Tachyon Cannon",10,4,3,"none",15)
Massdriver = cannons("Mass Driver",10,6,1,"none",10)
Photon = cannons("Photon Canon",14,3,2,"none",14)
Particle = cannons("Particle Cannon",10,4,1,"none",7)
Ion = cannons("Ion Cannon",12,5,2,"none",20)
Reaper = cannons("Reaper Cannon",10,6,2,"none",20)
Neutron = cannons("Neutron Cannon",5,7,2,"none",12)
Fission = cannons("Fission Cannon",8,8,2,"none",21)
PlasmaG = cannons("Plasma Gun",8,10,1,"none",13)
PlasmaC = cannons("Plasma Cannon",12,30,1,"none",6)
PlasmaR = cannons("Plasma Reaper",12,8,4,"none",64)
Meson = cannons("Meson Gun",10,2,2,"none",32)
Laser = cannons("Laser Cannon",18,1,6,"none",6)

canons = []
canons.append(Tachyon)
canons.append(Massdriver)
canons.append(Photon)
canons.append(Particle)
canons.append(Ion)
canons.append(Reaper)
canons.append(Neutron)
canons.append(Fission)
canons.append(PlasmaG)
canons.append(PlasmaC)
canons.append(PlasmaR)
canons.append(Meson)
canons.append(Laser)
if test_control.test:
    for canon in canons:
        canon.card()