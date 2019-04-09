from class_pilot import pilot
from class_ship import ship
from test_control import test, print_test
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
            print("shooting attack passed")
            attack = True
            result = str(self.pilot.name)+" attacks "+str(target.name)+". He rolls a "+gunnerycheck+" signalling that is on target with his shot." 
            self.dodging(target, dice)
        else:
            print("shooting attack failed")
            result = str(self.pilot.name)+" attacks "+str(target.name)+". He rolls a "+gunnerycheck+" signalling that is on target with his shot." 
            attack = False
            return attack, result

    def dodging(self, attacker, dice):
        if dice.roll() <= self.pilot.PilotSkill -2:
            print("Attack dodged")
        else:
            print("Dodge attempt failed")

    def damage(self, attacker):
        self.fighter.hullpoints = self.fighter.hullpoints - attacker.can_damage
        print(str(self.fighter.hullpoints))