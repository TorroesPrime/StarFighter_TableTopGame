class pilot:
    def __init__(self, name, faction, PilotSkill,GunnerySkill,Psych,Ability):
        self.name = str(name)
        self.faction = str(faction)
        self.PilotSkill = int(PilotSkill)
        self.GunnerySkill = int(GunnerySkill)
        self.Psych = int(Psych)
        self.cost = int((Psych*10)+(GunnerySkill*10)+(PilotSkill*10))
        self.Ability = Ability
    def card(self):
        print("|"+" "*(30-(int(len(self.name)/2)))+self.name+" "*(30-(int(len(self.name)/2)))+"|")
        print("| Pilot Skill: "+str(self.PilotSkill)+" "*4+"| Gunnery Skill: "+str(self.GunnerySkill)+" "*4+"| Psych: "+str(self.Psych)+" "*10+"|")
        print("| Pilot Ability: "+str(self.Ability))
        print("="*75)
    def psych_test(self, dice):
        if dice.roll() <= self.Psych:
            print("Psych test passed")
        else:
            print("Psych test failed") 