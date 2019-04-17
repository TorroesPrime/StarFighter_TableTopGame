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
    def getName(self):
        return self.name
    def setCost(self, cost):
        self.__points = cost
    def getCost(self):
        return self.cost
    def card(self):
        cost1 = "| "+(" ")*int((10-len(str(self.cost))-1)/2)+str(self.cost)
        cost2 = " "*(10-len(cost1))+" |"
        cost = cost1+cost2
        burn = " "*int((13-len(str(self.burn)))/2)+str(self.burn)
        turn = "/"+str(self.turn)+str(" "*int((13-len(str(self.turn)))/2-2))+"|"
        name = "|"+int(((75-len(self.name))/2)-1)*" "+self.name+int(((75-len(self.name))/2)-1)*" "+"|"
        if len(str(self.shields)) == 2:
            shields = str(" "*4)+str(self.shields)+" "*5+"|"
        else:
            shields = str(" "*5)+str(self.shields)+" "*5+"|"
        #shields = str("-"*int(11-int(len(str(self.shields)))/2-1))+str(self.shields)+str("-"*int(11-int(len(str(self.shields)))/2-1))+"|"
        if len(str(self.hullpoints)) == 1:
            hullpoints = str(" "*7)+str(self.hullpoints)+str(" "*7)+"|"
        elif len(str(self.hullpoints)) == 2:
            hullpoints = str(" "*6)+str(self.shields)+str(" "*7)+"|"
        else:   
            hullpoints = str(" "*6)+str(self.shields)+str(" "*6)+" |"
        if self.EvadeType == 'Decoy':
            evadeType = "   Decoys:"
        else:
            evadeType = "   Flares:"
        if len(str(self.EvadeCount)) == 2:
            evadeCount =str(self.EvadeCount)+"        |"
        else:
            evadeCount =str(self.EvadeCount)+"         |"
        print("|"+(" "*30)+"Fighter model"+(" "*30)+"|")
        print(str(name))
        print("|---Cost---|--Burn/Turn--|--Shields--|--Hull Points--|--Evasive Meassures-|")
        print(f"{cost}{burn}{turn}{shields}{hullpoints}{evadeType}{evadeCount}")
        print("Fighter Ability: "+str(self.ability))
        print("Guns: "+str(self.guns_number)+"-"+str(self.canon.name)+"s")
        print("Loadout slots: "+str(self.LoadOut))
        print("="*75)