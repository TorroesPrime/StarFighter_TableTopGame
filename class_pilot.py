faction={1:"Confederation",
    2:"Black Lance",
    3:"Renegades",
    4:"Kilrathi",
    5:"Union of Boarder Worlds"}
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
    "seether":"Seether only recieves a -1 modifier to his pilot skill when he attempts to dodge enemy fire rather then the normal -2. If he piloting a figther with the 'Bomber' keyword or a F-107A Lance, once per game he may execute a 'Mine Jumper' manuever. This manuever is executed during the movement phase. In the manuever, he moves straight forward 7 inches while all figthers with in 6 inches of his starting location take a single damage 12 hit and must pass a pilot skill test or gain a stress token.",
    "catscratch":"If Catscratch fails a Psych test, and the Wing leader/Commander is in his foward arc, he may re-roll the ego test but counts his Ego stat as being 5 rather then 4",
    "redclaw":"",
    "starkiller":"",
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
    "vagabond":"",
    "majorangel":"",
    "wiseone":"",
    "se'aka":"",
    "sek'a":"",

}
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
