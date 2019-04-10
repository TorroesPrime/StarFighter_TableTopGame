from class_pilot import pilot
from class_ship import ship
from test_control import test, print_test
from class_dice import diceObject
from strings import *
class WingMember:
    def __init__(self, designation, pilot, fighter):
        self.pilot = pilot
        self.fighter = fighter
        self.designation = designation
    def card(self):
        description = str(self.pilot.getName())+' is piloting a '+self.fighter.getName()
        if print_test:
            print(description)
        return description
    def shooting(self, target,dice):
        gunnerycheck = dice.roll()
        attacker =str(self.pilot.name)
        target = str(target.pilot.name) 
        if gunnerycheck <= self.pilot.GunnerySkill:
            if print_test:
                print(linebreak)
                print(hit)
            attack = True
            print(header)
            print(str(attacker)+" attacks "+str(target)+". He rolls a "+str(gunnerycheck)+" signalling that is on target with his shot.")
            print(linebreak)
           # target.dodging(dice)
        else:
            if print_test:
                print(header)
                print(miss)
            print(str(attacker)+" attacks "+str(target)+". He rolls a "+str(gunnerycheck)+" signalling that his shot has gone wide and will miss "+str(target)+"." )
            print(linebreak)
            attack = False
        return attack

    def dodging(self, dice):
        dodgecheck = dice.roll()
        if dodgecheck <= self.pilot.PilotSkill -2:
            print(self.pilot.name+"Attack dodged")
        else:
            print(self.pilot.name+"tried to dodge, but rolled "+str(dodgecheck)+" which is a failure.")

    def damage(self, attacker):
        self.fighter.hullpoints = self.fighter.hullpoints - attacker.can_damage
        print(str(self.fighter.hullpoints))
