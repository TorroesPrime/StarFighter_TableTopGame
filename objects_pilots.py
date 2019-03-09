from class_pilot import *
import json
#from class_pilot import pilot
#from class_pilot import faction


pilots_string = 
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
    }
    
with open('pilot_files.json','w') as output:
    json.dump(pilots_string)
output.close()

