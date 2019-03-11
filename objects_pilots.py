from class_pilot import *
import json
#from class_pilot import pilot
#from class_pilot import faction


pilots_string ="""
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
with open('pilot_files.json','w') as output:
    json.dumps(pilots_string)
output.close()

