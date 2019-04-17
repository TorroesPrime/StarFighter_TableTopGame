faction={1:"Confederation",
    2:"Black Lance",
    3:"Renegades",
    4:"Kilrathi",
    5:"Union of Boarder Worlds"}
Pilots_DB = []
pilot_abilities = {
    "firestorm": "Once per game, Fire Storm may execute a 'Canon Drill' attack. She may not make any turns or attempt to dodge enemy fire for that game turn, but she may make 2 shooting attacks that turn. she can still use evasive meassures.",
    "wildcard":"Each time a fighter is destroyed in Wild Card's forward arc, friendly or enemy, make an unmodified Psych test on Wild Card. If the test is passed, Wild Card operates as normal. If the test is failed, he has a break down and his pilot skill and Psych are both reduced to 4. However he may re-roll his first failed gunnery skill test each turn. In each subsequent turn, make a Psych test (using the modified value). if he passes, he returns to normal. If he rails, he remains in his 'break down' state. A friendly Confed pilot may attempt to talk him down by sacraficing all shooting and missile attacks for that turn, and making a taunt check against Wild Card. If Wild Card reists the taunt, he returns to normal.",
    "captain marshall":"Maniac is unaffected by abilities that affect his psych stat, both enemy and friendly. If an enemy fighter is in his forward arc, he must attempt to taunt them. If there is more then one enemy fighter in his forward arc, he will attempt to taunt the closest to him. Once per game, Maniac may make a special additional move immediately following a shooting attack. Treat this exactly like a normal move subject to the standard limitations",
    "colblair":"The First time a Wing Mate takes damage, Col. Blair gains a +2 bonus to his gunnery skill tests.",
    "bowman":"Archer is not especially aggressive as a pilot and would otherwise be a pacifist. Because of this she has a great deal of trouble taunting an enemy pilot. If she attempts to taunt an enemy pilot, treat her psych at 4 rather then 7. However, she is very clear minded. She may re-roll failed taunt resistance tests.",
    "khajja":"Khajja is exceptionally single minded in his tactics. When testing to resist a taunt, treat his ego stat as being 8 rather then 5",
    "bloodsworn":"Before the first game turn, select one enemy fighter. That fighter is now the target of the Blood Sworn's wraith and he must move to engage that figther at the first opportuity. For each turn that he does not have this fighter in his forward arc, or is not engaged in combat with it, he must pass a Psych test for gain 1 stress token. So long as he is engaged with that fighter, he may re-roll a single failed Gunnery Skill check per turn. He may re-roll a failed taunt resistance test if he is taunted by the selected fighter.",
    "spirit":"Once per game, Spirit may execute a strike attack. For that turn, she can any damage she taked from the first volley fired at her, and she gaines a +2 to her Gunnery Skill",
    "major blair":"Major Blair may re-roll 1 failed Gunnery Skill check per game turn",
    "seether":"When he makes a dodge test, Seether only ever suffers a -1 to his pilot skill. He may re-roll a failed taunt and any failed gunnery skill tests he is called on to make",
    "catscratch":"If Catscratch fails a Psych test, and the Wing leader/Commander is in his foward arc, he may re-roll the ego test but counts his Ego stat as being 5 rather then 4",
    "redclaw":"Redclaw may re-roll any failed gunnery skill tests he suffers.",
    "starkiller":"Bhurak dislikes using missiles, feeling that are beneath his skills. If he used a missile type weapon, and the attack is dodged, Bhurak must take a psych test. If he fails he gains 1 stress token.",
    "showstopper":"",
    "colangel":"",
    "colmanley":"",
    "coltaggart":"",
    "colfarnworth":"",
    "confedlt":"",
    "confedrookie":"",
    "confedcadet":"",
    "confedltjg":"",
    "dakhath":"",
    "ge'rall":"",
    "carnival":"",
    "vagabond":"If Winston Chang is the Wing Leader, all pilots in his wing may re-roll failed psych stat tests. If a friendly pilot with 1 or more stress tokens is with in his forward arc, Chang may attempt to calm them down. To do this he must sacrafice any attacks this turn and pass a psych test. If he succeds, the friendly pilot removes 1 stress token.",
    "majorangel":"",
    "wiseone":"",
    "se'aka":"",
    "sek'a":"",
    "Thrakath":"If Prince Thrakath is deployed, he is automatically the Wing Leader. If there is more then one wing, he automatically the Squadron Commander. His wing members do not test for stress if they are outnumbers at the begining of the game. Thrakath himself may re-roll any failed gunnery tests he suffers. he may re-roll a single failed dodge test per game turn.",
    "Primary Fang":"",
    "Ja'Trosh":"Ja'Trosh is a loner by nature and prefers to fight on his own. He is unaffected by abilities that modify his psych stat, both enemy and friendly. he can re-roll failed Pilot Skill tests. if he is alone (started with no wing mates) count his Psych as being a 7",
    "First Tooth":"",
}
class Pilot:
    def __init__(self, name, faction, PilotSkill,GunnerySkill,Psych,Ability):
        self.__points = int(10)
        self.name = str(name)
        self.faction = str(faction)
        self.PilotSkill = int(PilotSkill)
        self.GunnerySkill = int(GunnerySkill)
        self.Psych = int(Psych)
        self.__cost = int((Psych*self.__points)+(GunnerySkill*self.__points)+(PilotSkill*self.__points))
        self.Ability = Ability
    def get_Name(self):
        return self.name
    def set_Points(self, cost):
        self.__points = cost
    def set_Cost(self, cost):
        self.__cost = cost
    def get_Cost(self):
        return self.__cost
    def print_InfoCard(self):
        print("|"+" "*(30-(int(len(self.name)/2)))+self.name+" "*(30-(int(len(self.name)/2)))+"|")
        print("| Pilot Skill: "+str(self.PilotSkill)+" "*4+"| Gunnery Skill: "+str(self.GunnerySkill)+" "*4+"| Psych: "+str(self.Psych)+" "*10+"|")
        print("| Pilot cost: "+str(self.getCost()))
        print("| Pilot Ability: "+str(self.Ability))
        print("="*75)
    def psych_Test(self, dice):
        if dice.roll() <= self.Psych:
            print("Psych test passed")
        else:
            print("Psych test failed") 
