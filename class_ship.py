EvasiveMessuresNames = {1:"Decoys",2:"Flares",3:"ECM Pod"}
class Ship():
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
    def get_Name(self):
        return self.name
    def set_Points(self, cost):
        self.point = cost
    def set_Cost(self, cost):
        self.cost = cost
    def get_Cost(self):
        return self.cost
    def print_InfoCard(self):
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
        if self.EvadeType == EvasiveMessuresNames[1]:
            evadeType = "   Decoys:"
        elif self.EvadeType == EvasiveMessuresNames[2]:
            evadeType = "   Flares:"
        else:
            evadeType = "   ECM Pod:"
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

        
abilities = {"sabre":"The F-57B Sabre mounts a computer controleld rear turret that covers its rear quadrant. \
This weapon fires independently of the main ship allowing it to target a different ship to the pilot themselves\
. The Turret has a Gunnery Skill of 4 and mounts 2 Neutron Guns.",
"F-103A": "The F-103A Excalibur conveys a +1 bonus to all gunnery skill checks the pilot is called on to make.\
You may re-roll the first 'miss' result you get each game turn.",
"F-107":"The Pilot of the Lance gains a +2 bonus to any gunnery skill tests they are called on to make. The \
Lance counts has having 1 more energy token in it's cannon slot then normal.",
"F-109B":"The Vampire poccesses exception maneuverability. When turning beyond its normal turn allowance, only \
only perform a pilot skill test for every 2 degrees of turn instead of the normal 1.",
"none":"",
"TB-80A":"The TB-80A Devastator mounts computer controlled Turrets that cover it's right, left, and rear quadrants\
. Each turret is independently controlled and can acquire and shoot at their own targets. Each of the Turrets are \
armed with a single laser canon and count has having a Gunnery skill of 5.",
"KRF-07C":"So long as the Bloodfang has 22 or more hit points remaining, you may re-roll damage checks you are\
 called on to make. The Bloodfang regenerates 1 more shield point per turn then it would normally so long as\
 it's shields have not been destroyed.",
"A-17A":"The A-17A Broadsword mounts turrets that cover its right, left and rear quadrants. Each turret is\
independently controlled by either a computer system that counts has having a gunnery skill of 4, or can be\
manned by a pilot. each turret is armed with twin neutron guns. These turrets can aim at and fire at targets\
independent of the pilot of the Broadsword itself.",
"F-64a":"The Banshee mounts a redundant battery system tied directly to its shields. The Banshee can refenerate\
1 additional shield point per turn then it would normally be capable of, so long as it's shields have not been\
destroyed.",
"F-104a":"The F-104 Bearcat conveys a +2 gunnery skill bonus to any shooting attacks the pilot is calld on to\
make. The pilot also gains 2 free re-rolls that may be used anywhere the player deems to use them during the\
game.",
"FA-36A":"The Hornet is exceptionally fast for a craft of its era. If converting 'turn' to 'burn' convert at\
a ration of 1 to 1 rather then the normal 2 to 1.",
"HF-66A":"The HF-66 Thunderbolt VII mounts a computer controlled rear turret that covers it's rear quadrant.\
This weapon fires independently of the main ship allow it to target a different ship to the pilot themselves.\
The turret has a gunnery skill of 4, and mounts a single mass Driver.",
 "KHFB-1066C":"The VokToth mounts a computer controlled rear turret that covers it's rear quadrant.\
This weapon fires independently of the main ship allow it to target a different ship to the pilot themselves.\
The turret has a gunnery skill of 4, and mounts 2 Meson Guns.",
 "KSF-119B":"The Strakha mounts one of the Kilrathi first production series cloaking devices, allowing the \
ship to vanish from sight and radar at a moments notice. When making a dodge test against guided missiles, \
treat the pilot skill of the Strakha's pilot as if it were +2 to it's normal value.",
 "KHFA-983A":"The Darket is an exceptionally nimble design, allowing to undertake shockingly adept manuevers\
in the hands of a skilled pilot. If the pilot of the Darket fails a dodge check, you may re-roll it.",
 "F-86C":"",
"UFB-115B":"The UFB-115B Avenger mounts a computer controlled rear turret that covers it's rear quadrant.\
This weapon fires independently of the main ship allow it to target a different ship to the pilot themselves.\
The turret has a gunnery skill of 4, and mounts 2 mass Drivers.",
"UFB-74B":"The UFB-74B Vindicator mounts a computer controlled rear turret that covers it's rear quadrant.\
This weapon fires independently of the main ship allow it to target a different ship to the pilot themselves.\
The turret has a gunnery skill of 4, and mounts 2 Laser Cannons."}
