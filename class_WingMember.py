class WingMember:
    def __init__(self, pilot, fighter):
        self.pilot = pilot
        self.fighter = fighter
    
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