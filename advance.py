def check_advance(character):
    """
    Determine if character's knowledge is enough to advance to the next term.

    :param character: a dictionary describing the character
    :precondition: character must contain "Term", "Knowledge" as keys
    :postcondition: calculates whether the character has enough knowledge to advance to the next term
    :return: a boolean value of whether character advances

    >>> character1 = {"Knowledge": 0, "Term": 1}
    >>> check_advance(character1)
    False
    >>> character2 = {"Knowledge": 6, "Term": 1}
    >>> check_advance(character2)
    True
    """
    character_term = character["Term"]
    character_knowledge = character["Knowledge"]
    decision_of_advance = False

    max_term = 4
    knowledge_per_term = 5
    if character_term < max_term:
        decision_of_advance = character_knowledge / knowledge_per_term >= character_term
    return decision_of_advance


def advance(character):
    """
    Make the character to advance to next term.

    :param character: a dictionary describing the character
    :precondition: character must contain "Term" and "Stress" as keys
    :postcondition: updates the character's term, and reduces stress
    """
    character["Term"] += 1
    with open('./text/advance.txt') as file_object:
        text = file_object.read()
        print(text)
    print('You are now in Term %d' % character["Term"])
    character["Stress"] = max(character["Stress"] - 5, 0)
    print('After the term break, you are more refreshed! [Stress: %d]' % character["Stress"])
    return
