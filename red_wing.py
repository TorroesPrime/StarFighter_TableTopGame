from objects_pilots import pilotsKilrathi
from objects_pilots import *
from class_WingMember import WingMember
import objects_canons
import d10
import class_WingMember
from test_control import test, print_test
from objects_fighters import *
redWing = []
#class WingMember:
#    def __init__(self, pilot, fighter):
#wing =  WingMember(pilotsKilrathi["Prince Thrakath nar Kilranka"])

red_1 = WingMember('red 1',K007,KRF07C)
red_2 = WingMember('red 2',K006,KB600B)
red_3 = WingMember('red 3',K006,KB600B)
redWing.append(red_1)
redWing.append(red_2)
redWing.append(red_3)

for member in redWing:
    member.card()
