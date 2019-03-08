from class_pilot import *
import json
#from class_pilot import pilot
#from class_pilot import faction


pilots_string = '''
    {
        "pilot":[
            {
                "name": "Seether",
                "faction": "faction[2]",
                "pilotskill":9,
                "gunneryskill":8,
                "Psych":9,
                "ability":"pilot_abilities['seether']"
            }
            "pilot":[
            {
                "name": "Alicia 'Fire Storm' Heinz",
                "faction": "faction[1]",
                "pilotskill":4,
                "gunneryskill":6,
                "Psych":6,
                "ability":"pilot_abilities['firestorm']"
            }
            "pilot":[
            {
                "name": "Bakhtosh 'Redclaw' nar Kilranka",
                "faction": "faction[14]",
                "pilotskill":9,
                "gunneryskill":5,
                "Psych":6,
                "ability":"pilot_abilities['redclaw']"
            }
        ]
    }
    '''
with open('pilot_files.json','w') as output:
    json.dump(pilots_string, output)
output.close()

