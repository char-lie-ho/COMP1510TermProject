"""
Charlie Ho
A01358146
"""
import json
import pathlib
from all_events import encounter_event, event, interview, home
from initalize_game import create_character, make_board
from load_game import load_progress


def describe_current_location(board, character):  # DONE, only unittest the return
    """
    Return the current location on the board.

    :param board: a dictionary contains the coordinates as key and description of that location as value
    :param character: a dictionary contains character coordinates and HP
    :precondition: board must contain the location coordinates as key and each value is a string description
    :precondition: character must contain "X-coordinate", "Y-coordinate" and "Current HP" as keys
    :postcondition: retrieve location information on board base on the character coordinate
    :return: a string describing the location of the board
    """
    x_coordinate = character.get("X-coordinate")
    y_coordinate = character.get("Y-coordinate")
    current_location = board[(x_coordinate, y_coordinate)]
    print('-' * 80)
    print(f"You are now at [%s] on location (%d, %d)" % (current_location, x_coordinate, y_coordinate))
    display_map(x_coordinate, y_coordinate, board)
    return current_location


def display_map(x_coordinate, y_coordinate, board):  # DONE, unittest done
    """
    Display a simple map.

    :param x_coordinate: x-coordinate of the character
    :param y_coordinate: y-coordinate of the character
    :param board: a dictionary contains the coordinates as key and description of that location as value
    :precondition: x_coordinate must be non-negative integer and less than 5
    :precondition: y_coordinate must be non-negative integer and less than 5
    :precondition: board must contain the location coordinates as key
    :postcondition: prints a map with borders and a character at the specified coordinates
    """
    width = max(coordinate[0] for coordinate in board.keys()) + 1
    height = max(coordinate[1] for coordinate in board.keys()) + 1

    for row in range(height * 2 + 1):
        top_board = ["\t", "┍", "⎯"] + (width - 1) * ["┬", "⎯"] + ["┑"]
        bottom_board = ["\t", "┕", "⎯"] + (width - 1) * ["┴", "⎯"] + ["┙"]
        center_lines = ["\t", "├", "⎯"] + (width - 1) * ["┼", "⎯"] + ["┤"]
        center_space = ["\t", "|", " "] + (width - 1) * ['|', " "] + ['|']
        if row == 0:
            line_to_print = top_board
        elif row == 2 * height:
            line_to_print = bottom_board
        elif row % 2 != 0:
            if y_coordinate * 2 + 1 == row:
                center_space[x_coordinate * 2 + 2] = 'x'
            line_to_print = center_space
        else:
            line_to_print = center_lines
        print(" ".join(line_to_print))
    return


def get_user_choice(character):  # DONE, finish unittest, test input only (return)
    """
    Obtain the user's choice of direction (North, East, South, or West) or quit game.

    :postcondition: ensures that the user's choice is valid (N, E, S, or W)
    :return: a string with the user's chosen direction
    """
    decision = None
    while decision not in ['N', 'S', 'E', 'W']:
        decision = input('Please enter a direction you want to go (N: North| E: East| S: South| W: West)'
                         '\n or (QUIT: save and end game): ').upper()
        if decision == 'QUIT':
            with open('game_save.json', 'w') as output:
                json.dump(character, output)
            print("Progress has been saved. Good bye!")
            quit()
    return decision


def character_advance(character):  # DONE, unittest done
    """
    Determine if character's knowledge is enough to advance to the next term.

    :param character: a dictionary describing the character
    :precondition: character must contain "Term", "Knowledge" as keys
    :postcondition: calculates whether the character has enough knowledge to advance to the next term
    :return: a boolean value of whether character advances

    >>> character1 = {"Knowledge": 0, "Term": 1}
    >>> character_advance(character1)
    False
    >>> character2 = {"Knowledge": 6, "Term": 1}
    >>> character_advance(character2)
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


def advance(character):  # DONE, finish unittest
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


def end_of_game(character):  # DONE, finish unittest
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


def determine_location(character, board):  # DONE, no doctest, no unittest
    """
    Obtain character's location to determine the trigger event.

    :param character: a dictionary describing the character
    :param board: a dictionary describing the board
    :precondition: character must contain "X-coordinate",and "Y-coordinate" as keys
    :precondition: board must contain the location coordinates as key and each value is a string description
    :postcondition: execute different functions based on coordinates of the character and board
    """
    x_coordinate = character.get("X-coordinate")
    y_coordinate = character.get("Y-coordinate")
    current_location = board[(x_coordinate, y_coordinate)]
    special_locations = {'🏠home': home, '💼interview': interview}  # home, interview are functions
    if current_location in special_locations:
        special_events = special_locations.get(current_location)
        special_events(character)
    else:
        if encounter_event():
            event(character)
    return


def end_game(character):  # no need to unittest, print only
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
        with open('./text/game_end1.txt') as file_object:
            text = file_object.read()
            print(text)
    elif character["Stress"] >= stress_capacity:  # bad end
        with open('./text/game_end2.txt') as file_object:
            text = file_object.read()
            print(text)
    return


def game():
    """
    Start the game.
    """
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    save_path = pathlib.Path('/game_save.json')
    if save_path.exists():
        print('You have a saved progress.')
        character = create_character()
    else:
        character = load_progress()
    while not end_of_game(character):
        describe_current_location(board, character)
        direction = get_user_choice(character)
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            determine_location(character, board)
            if character_advance(character):
                advance(character)
        else:
            print("Ouch! You hit a wall! 🧱")
    end_game(character)


def main():
    """
    Execute the game function.
    """
    game()


if __name__ == '__main__':
    main()
