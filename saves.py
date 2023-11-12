import json
from settings import BEAT_LENGTH, SOUND_LIST


empty_save = []
    
for n in range((BEAT_LENGTH * len(SOUND_LIST))):
    empty_save.append(False)

saves = {
    "1" : empty_save,
    "2" : empty_save,
    "3" : empty_save,
    "4" : empty_save,
    "5" : empty_save,
    "6" : empty_save,
    "7" : empty_save,
    "8" : empty_save
}

bpms = {
    "1" : 120,
    "2" : 120,
    "3" : 120,
    "4" : 120,
    "5" : 120,
    "6" : 120,
    "7" : 120,
    "8" : 120
}

def save():
    with open("saves.json", "w") as file:
        json.dump((saves, bpms), file)

def load():
    global save_list
    global saves
    global bpms
    with open('saves.json', 'r') as file:
        save_list1 = json.load(file)
    saves = save_list1[0]
    bpms = save_list1[1]
    save_list = save_list1