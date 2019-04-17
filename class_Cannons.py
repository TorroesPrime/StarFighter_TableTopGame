class Cannons:
    def __init__(self,name,can_range,can_damage,can_shots,can_special,cost):
        self.name = name
        self.can_range = can_range
        self.can_damage = can_damage
        self.can_shots = can_shots
        self.can_special = can_special
        self.cost = cost
    def print_InfoCard(self):
        name = " "+self.name+" "*(17-len(self.name)+1)
        if len(str(self.can_range)) == 2:
            cannon_range = "  "+str(self.can_range)+"   "
        else:
            cannon_range = "   "+str(self.can_range)+"   "
        
        if len(str(self.can_damage)) == 2:
            cannon_damage = " "+str(self.can_damage)+"  "
        else:
            cannon_damage = "  "+str(self.can_damage)+"  "
        if (len(str(self.can_shots))) == 2:
            shots = " "+str(self.can_shots)+"   "
        else:
            shots = "   "+str(self.can_shots)+"   "
        
        print("|      Name         | Range | Dmg | Shots | Special:                      |")
        print(f"|{name}|{cannon_range}|{cannon_damage}|{shots}|{self.can_special}                           |")
        print("="*75)
    def get_Cost(self):
        return self.cost
    def get_Name(self):
        return self.name
    def get_range(self):
        return self.can_range
