from class_pilot import *
import json
import test_control

# from class_pilot import pilot
# from class_pilot import faction

pilotsConfed = []
pilotsKilrathi = []
pilots_string = """
    {
        "pilot":
            {
                "name": "Seether",
                "faction": faction[2],
                "pilotskill":9,
                "gunneryskill":8,
                "Psych":9,
                "ability":pilot_abilities['seether'],
            }
        "pilot":
            {
                "name": "Alicia 'Fire Storm' Heinz",
                "faction": faction[1],
                "pilotskill":4,
                "gunneryskill":6,
                "Psych":6,
                "ability":pilot_abilities['firestorm'],
            }
            "pilot":
            {
                "name": "Bakhtosh 'Redclaw' nar Kilranka",
                "faction": faction[4],
                "pilotskill":9,
                "gunneryskill":5,
                "Psych":6,
                "ability":pilot_abilities['redclaw'],
            }
            "pilot":
            {
                "name": "Bhurak 'Starkiller' nar Caxki",
                "faction": faction[4],
                "pilotskill":7,
                "gunneryskill":8,
                "Psych":7,
                "ability":pilot_abilities['starkiller'],
            }
            "pilot":
            {
                "name": "Amanda 'Show stopper' Williams",
                "faction": faction[1],
                "pilotskill":4,
                "gunneryskill":3,
                "Psych":5,
                "ability":pilot_abilities['showstopper'],
            }
             "pilot":
            {
                "name": "James 'Wild Card' Peterson",
                "faction": faction[1],
                "pilotskill":7,
                "gunneryskill":6,
                "Psych":6,
                "ability":pilot_abilities['wildcard'],
            }
             "pilot":
            {
                "name": "Captain Todd 'Maniac' Marshall",
                "faction": faction[1],
                "pilotskill":7,
                "gunneryskill":7,
                "Psych":8,
                "ability":pilot_abilities['captain marshall'],
            }
             "pilot":
            {
                "name": "Jeannette 'Angel' Devereaux",
                "faction": faction[1],
                "pilotskill":8,
                "gunneryskill":7,
                "Psych":7,
                "ability":pilot_abilities['angel'],
            }
             "pilot":
            {
                "name": "Col. Christopher 'Maverick' Blair,
                "faction": faction[1],
                "pilotskill":9,
                "gunneryskill":7,
                "Psych":8,
                "ability":pilot_abilities['colblair'],
            }
             "pilot":
            {
                "name": "Col. Jacon 'Hawk' Manley",
                "faction": faction[1],
                "pilotskill":8,
                "gunneryskill":6,
                "Psych":8,
                "ability":pilot_abilities['colmanley'],
            }
            "pilot":
            {
                "name": "Col. James 'Paladin' Taggart",
                "faction": faction[5],
                "pilotskill":7,
                "gunneryskill":8,
                "Psych":8,
                "ability":pilot_abilities['coltaggart'],
            }
            "pilot":
            {
                "name": "Col. Tamara 'Panther' Farnsworth",
                "faction": faction[5],
                "pilotskill":8,
                "gunneryskill":7,
                "Psych":7,
                "ability":pilot_abilities['colfarnworth'],
            }
            "pilot":
            {
                "name": "Confed Lieutenant",
                "faction": faction[1],
                "pilotskill":5,
                "gunneryskill":5,
                "Psych":5,
                "ability":pilot_abilities['confedlt'],
            }
            "pilot":
            {
                "name": "Confed Rookie Pilot",
                "faction": faction[1],
                "pilotskill":3,
                "gunneryskill":2,
                "Psych":4,
                "ability":pilot_abilities['confedrookie'],
            }
            "pilot":
            {
                "name": "Confed Cadet Pilot",
                "faction": faction[1],
                "pilotskill":3,
                "gunneryskill":3,
                "Psych":4,
                "ability":pilot_abilities['confedcadet'],
            }
            "pilot":
            {
                "name": "Confederation Lieutenant Junior Grade",
                "faction": faction[1],
                "pilotskill":4,
                "gunneryskill":4,
                "Psych":6,
                "ability":pilot_abilities['confedltjg'],
            }
            "pilot":
            {
                "name": "Dakhath nar Caxki",
                "faction": faction[4],
                "pilotskill":7,
                "gunneryskill":8,
                "Psych":7,
                "ability":pilot_abilities['dakhath'],
            }
            "pilot":
            {
                "name": "Ge\'rall nar Kilranka",
                "faction": faction[4],
                "pilotskill":5,
                "gunneryskill":8,
                "Psych":7,
                "ability":pilot_abilities['ge'rall'],
            }
            "pilot":
            {
                "name": "Gwen 'Archer' Bowman",
                "faction": faction[1],
                "pilotskill":3,
                "gunneryskill":5,
                "Psych":7,
                "ability":pilot_abilities['bowman'],
            }
            "pilot":
            {
                "name": "Khajja nar Ja'targk",
                "faction": faction[4],
                "pilotskill":8,
                "gunneryskill":8,
                "Psych":5,
                "ability":pilot_abilities['khajja'],
            }
            "pilot":
            {
                "name": "Kilranka Blood sworn",
                "faction": faction[4],
                "pilotskill":7,
                "gunneryskill":7,
                "Psych":7,
                "ability":pilot_abilities['bloodsworn'],
            }
       }
    """
with open('pilot_files.json', 'w') as output:
    json.dumps(pilots_string)
output.close()

# (self, name, faction, PilotSkill,GunnerySkill,Psych,Ability)
K001 = pilot("Kilranka Blood sworn", faction[4], 7, 7, 7, pilot_abilities['bloodsworn'])
Pilots_DB.append(K001)
K002 = pilot("Khajja nar Ja'targk", faction[4], 8, 8, 7, pilot_abilities['khajja'])
Pilots_DB.append(K002)
C001 = pilot("Gwen 'Archer' Bowman", faction[1], 3, 5, 7, pilot_abilities['bowman'])
Pilots_DB.append(C001)
K003 = pilot("Bakhtosh 'Redclaw' nar Kiranka", faction[4], 9, 5, 7, pilot_abilities['redclaw'])
Pilots_DB.append(K003)
K004 = pilot("Bhurak 'Starkiller' nar Caxki", faction[4], 8, 7, 7, pilot_abilities['starkiller'])
Pilots_DB.append(K004)
K005 = pilot("Dakhath nar Sihkag", faction[4], 7, 8, 7, pilot_abilities['dakhath'])
Pilots_DB.append(K005)
K006 = pilot("First Tooth pilot", faction[4], 3, 2, 4, pilot_abilities['First Tooth'])
Pilots_DB.append(K006)
K008 = pilot("Primary Fang pilot", faction[4], 4, 4, 5, pilot_abilities['Primary Fang'])
Pilots_DB.append(K008)
K007 = pilot("Prince Thrakath nar Kilranka", faction[4], 8, 9, 9, pilot_abilities['Thrakath'])
Pilots_DB.append(K007)
K009 = pilot("Ja'Trosh 'Lone Fang' nar Caxkal", faction[4], 4, 4, 5, pilot_abilities["Ja'Trosh"])
Pilots_DB.append(K009)
C002 = pilot("'Seether'", faction[1], 9, 8, 9, pilot_abilities['seether'])
Pilots_DB.append(C002)
C003 = pilot("Troy 'Cathscratch' Carter", faction[1], 4, 4, 4, pilot_abilities['catscratch'])
Pilots_DB.append(C003)
C004 = pilot("Winston 'Vagabond' Chang", faction[1], 5, 7, 7, pilot_abilities['vagabond'])
Pilots_DB.append(C004)
C005 = pilot("Confederation Lieutenant", faction[1], 5, 3, 3, pilot_abilities['confedlt'])
Pilots_DB.append(C005)
C006 = pilot("Confederation Rookie", faction[1], 3, 2, 4, pilot_abilities['confedrookie'])
Pilots_DB.append(C006)


for pilot in Pilots_DB:
    if pilot.faction == "Confederation":
        pilotsConfed.append(pilot)
    elif pilot.faction == "Kilrathi":
        pilotsKilrathi.append(pilot)

if test_control.test:
    print("pilots of the Confederation")
    for pilot in pilotsConfed:
        pilot.card()
if test_control.test:
    print("Kilrathi Pilots")
    for pilot in pilotsKilrathi:
        pilot.card()
