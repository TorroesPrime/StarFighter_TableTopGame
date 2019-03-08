class ship():
    def __init__(self, name, faction, burn, turn, shields, hullpoints, evasive_meassures, ability, Guns_number, canon, LoadOut):
        self.name = name
        self.faction = faction
        self.burn = burn
        self.turn =turn
        self.shields = shields
        self.hullpoints = hullpoints
        self.EvadeType = evasive_meassures[0]
        self.EvadeCount = evasive_meassures[1]
        self.ability = ability
        self.guns_number = Guns_number
        self.LoadOut = LoadOut
        self.point = 10
        self.canon = canon
        self.cost = int(((self.burn+self.turn+self.shields+self.hullpoints)*self.point)+(5*self.guns_number)+(canon.cost*self.guns_number))
        
    def card(self):
        print("|"+(" "*24)+"Fighter model"+(" "*24)+"|")
        print("|"+" "*(int(31-len(self.name)/2))+self.name+" "*(int(30-len(self.name)/2))+"|")
        print("|-Cost-|-Burn/Turn-|-Shields-|-Hull Points-|-Evasive Massures-|")
        print(f"|  {self.cost} |    {self.burn}/{self.turn}    |    {self.shields}   |      {self.hullpoints}     |   {self.EvadeType}s: {self.EvadeCount}      |")
        print("Fighter Ability: "+str(self.ability))
        print("Guns: "+str(self.guns_number)+"-"+str(self.canon.name)+"s")
        print("Loadout slots: "+str(self.LoadOut))
        print("="*75)