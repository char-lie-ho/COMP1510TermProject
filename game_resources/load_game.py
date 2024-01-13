import json
from game_resources import initalize_game


def load_progress():
    """
    Load the previous saved progress.

    :postcondition: read the json file to load the game progress or execute the create_character function
    :return: a dictionary containing the character status
    """
    with open('game_save.json') as file_object:
        character = json.load(file_object)
    decision = None
    while decision not in ["Y", "N"]:
        decision = input('%s is waiting. Do you want to load the progress? (Y/N) ' % character["Name"]).upper()
    if decision == "Y":
        print("Welcome back, %s!" % character["Name"])
    else:
        character = initalize_game.create_character()
    return character
