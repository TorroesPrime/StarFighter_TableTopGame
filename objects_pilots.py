from class_pilot import *
from class_pilot import faction
listpilots = []
pilot_seether = pilot("Seether",faction[2],9,8,9,pilot_abilities["Seether"])
listpilots.append(pilot_seether)
pilot_firestorm = pilot("Alicia 'Fire Storm' Heinz",faction[1],9,8,9,pilot_abilities["Firestorm"])
listpilots.append(pilot_firestorm)

for pilot in listpilots:
    pilot.card()
