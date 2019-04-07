from class_pilot import pilot
from class_ship import ship

class WingMember:
    def __init__(self, designation, pilot, fighter):
        self.pilot = pilot
        self.fighter = fighter
        self.designation = designation
    #@property
    def card(self):
        description = str(self.pilot.getName())+' is piloting a '+self.fighter.getName()
        return description
    def shooting(self, target, dice):
        if dice.roll() <= self.pilot.GunnerySkill:
            print("shooting attack passed")
            attack = True
            self.dodging(target, dice)
        else:
            print("shooting attack failed")
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