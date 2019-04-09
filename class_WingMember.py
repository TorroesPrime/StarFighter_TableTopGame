from class_pilot import pilot
from class_ship import ship
from test_control import test, print_test
from class_dice import diceObject
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
    def shooting(self, target, dice):
        gunnerycheck = dice.roll()
        if gunnerycheck <= self.pilot.GunnerySkill:
            if print_test:
                print("shooting attack passed")
            attack = True
            print(str(self.pilot.name)+" attacks "+str(target.pilot.name)+". He rolls a "+str(gunnerycheck)+" signalling that is on target with his shot.")
            #self.dodging(target, dice)
        else:
            if print_test:
                print("shooting attack failed")
            print(str(self.pilot.name)+" attacks "+str(target.pilot.name)+". He rolls a "+str(gunnerycheck)+" signalling that his shot has gone wide and will miss "+str(target.pilot.name)+"." )
            attack = False
        return attack

    def dodging(self, attacker, dice):
        if dice.roll() <= self.pilot.PilotSkill -2:
            print("Attack dodged")
        else:
            print("Dodge attempt failed")

    def damage(self, attacker):
        self.fighter.hullpoints = self.fighter.hullpoints - attacker.can_damage
        print(str(self.fighter.hullpoints))