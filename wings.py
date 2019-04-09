from objects_pilots import pilotsKilrathi
from objects_pilots import *
from class_WingMember import WingMember
import objects_canons
from d10 import *
import class_WingMember
from test_control import test, print_test
from objects_fighters import *
redWing = []
blueWing = []
#class WingMember:
#    def __init__(self, pilot, fighter):
#wing =  WingMember(pilotsKilrathi["Prince Thrakath nar Kilranka"])

red_1 = WingMember('red 1',K007,KRF07C)
red_2 = WingMember('red 2',K006,KB600B)
red_3 = WingMember('red 3',K006,KB600B)
blue_1 = WingMember('blue 1',C002,TB76A)
blue_2 = WingMember('blue 2',C003,TB76A)
blue_3 = WingMember('blue 3',C004,TB76A)
redWing.append(red_1)
redWing.append(red_2)
redWing.append(red_3)
blueWing.append(blue_1)
blueWing.append(blue_2)
blueWing.append(blue_3)

for member in redWing:
    member.card()

for kilrathi in redWing:
    for Confed in blueWing:
        kilrathi.shooting(Confed, d10)