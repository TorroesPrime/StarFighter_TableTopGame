from class_pilot import *
#from class_pilot import pilot
#from class_pilot import faction
listpilots = []
pilot_seether = pilot("Seether",faction[2],9,8,9,pilot_abilities["seether"])
listpilots.append(pilot_seether)
pilot_firestorm = pilot("Alicia 'Fire Storm' Heinz",faction[1],9,8,9,pilot_abilities["firestorm"])
listpilots.append(pilot_firestorm)
pilot_redclaw = pilot("Bakhtosh 'Redclaw' nar Kiranka",faction[4],9,5,6,pilot_abilities["redclaw"])
listpilots.append(pilot_redclaw)
pilot_dakhath = pilot("Dakhath 'Deathstroke' nar Caxki",faction[4],9,5,6,pilot_abilities["dakhath"])
listpilots.append(pilot_dakhath)
pilot_starkiller = pilot("Bhurak 'Starkkiller' nar Caxki",faction[4],7,8,7,pilot_abilities["starkiller"])
listpilots.append(pilot_starkiller)
pilot_khajja = pilot("Khajja 'The Fang' nar Ja'Targk",faction[4],8,8,5,pilot_abilities["khajja"])
listpilots.append(pilot_khajja)
for pilot in listpilots:
    pilot.card()
