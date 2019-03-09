class cannons:
    def __init__(self,name,can_range,can_damage,can_shots,can_special,cost):
        self.name = name
        self.can_range = can_range
        self.can_damage = can_damage
        self.can_shots = can_shots
        self.can_special = can_special
        self.cost = cost
    def card(self):
        print("|     Name      | Range | Dmg | Shots | Special:                    |")
        print(f"| {self.name} |  {self.can_range}   | {self.can_damage}  |  {self.can_shots}  |{self.can_special}                    |")
        print("="*75)
    def get_cost(self):
        return self.cost
    def get_name(self):
        return self.name
    def get_range(self):
        return self.can_range