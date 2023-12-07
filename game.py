"""
Charlie Ho
A01358146
"""
import json
import pathlib
from all_events import encounter_event, event, interview, home
from initalize_game import create_character, make_board
from load_game import load_progress
from move import validate_move, move_character
from end_game import end_of_game, end_game


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
    special_locations = {'🏠home': home, '💼interview': interview}
    if current_location in special_locations:
        special_events = special_locations.get(current_location)
        special_events(character)
    else:
        if encounter_event():
            event(character)
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
