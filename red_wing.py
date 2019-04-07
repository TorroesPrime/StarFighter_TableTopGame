from objects_pilots import pilotsKilrathi
from class_WingMember import WingMember
import objects_canons
import d10
import class_WingMember
import test_control
#class WingMember:
#    def __init__(self, pilot, fighter):
#wing =  WingMember(pilotsKilrathi["Prince Thrakath nar Kilranka"])
if test_control.test:
    for pilot in pilotsKilrathi:
        print(pilot.getName())


red_1 = WingMember('red 1',K007,KRF07C)
red_1.card()
