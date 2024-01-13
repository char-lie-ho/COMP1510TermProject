def end_of_game(character):
    """
    Check if the character has reached the endgame conditions.

    :param character: a dictionary describing the character status
    :precondition: character must contain "Stress" and "Hired" as keys
    :postcondition: determines whether the character's stress is over 50 or 'Hired' status is True
    :return: a boolean value of whether game ends
    >>> character1 = {"Stress": 50, "Hired": False}
    >>> end_of_game(character1)
    True
    >>> character2 = {"Stress": 21, "Hired": True}
    >>> end_of_game(character2)
    True
    """
    if character["Stress"] >= 50 or character["Hired"]:
        return True
    else:
        return False


def end_game(character):
    """
    Print out the end game message.

    :param character: a dictionary describing the character
    :precondition: character must contain "Hired" and "Stress" as key
    :precondition: game_end1.txt must exist in the package
    :precondition: game_end2.txt must exist in the package
    :postcondition: reduce character 'Stress' by 3, and print out useful information
    """
    stress_capacity = 50
    if character["Hired"]:  # good end
        with open('../text/game_end1.txt') as file_object:
            text = file_object.read()
            print(text)
    elif character["Stress"] >= stress_capacity:  # bad end
        with open('../text/game_end2.txt') as file_object:
            text = file_object.read()
            print(text)
    return
