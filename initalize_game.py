import random
import itertools


def create_character():  # DONE, invoke game_difficult, cannot unittest
    """
    Ask the player for the character's name and declare the initial state of the character.

    :postcondition: initialize character coordinates, knowledge, term, stress, name, hired, and difficulty
    :return: a dictionary contain character info
    """
    with open("./text/intro.txt") as file_object:
        text = file_object.read()
        print(text)
    character_name = input("Tell me, what is your name? ")
    print("So, your name is %s" % character_name)
    proceed = input("Is this correct? (Y/N) ").upper()
    # confirm if user has typed the correct name
    while proceed not in ['Y', 'YES']:
        proceed = input("Is this correct? (Y/N) ").upper()
    character = {"X-coordinate": 0, "Y-coordinate": 0, "Knowledge": 0, "Term": 1, "Stress": 0, "Name": character_name,
                 "Hired": False, "Difficulty": None}
    game_difficulty(character)
    return character


def game_difficulty(character):  # DONE, unittest DONE
    """
    Ask the player for the game difficulty.

    :param character: a dictionary contains character status
    :precondition: character must contain 'Difficulty' as keys
    :postcondition: the 'Difficulty' key in the 'character' dictionary will be updated based on the user's input
    :return: the updated character dictionary
    """
    while True:
        difficulty = input("Life is hard, how hard you want this adventure to be on a scale "
                           "from 1 (easy) to 3 (difficult)? ")
        try:
            float(difficulty)
        except ValueError:
            print("Oh, you can't even type numbers?!")  # if user input is not a number
        else:
            if float(difficulty) not in [1, 2, 3]:  # if user input is not an integer
                print("Oh, I hope you can enter an integer.")
                continue
            else:
                print("Great! I like your choice.")
                character["Difficulty"] = float(difficulty)
                break
    return character


def make_board(rows, columns):  # DONE, unittest done
    """
    Generate a game board with the desired size.

    :param rows: an integer describing the width of the game board
    :param columns: an integer describing the height of the game board
    :precondition: both rows and columns are integers greater than or equal to 2
    :postcondition: create a dictionary containing the coordinates as key and locations as value
    :return: a dictionary representing the game board
    """
    locations = ('📖study room', '📚library', '🏫classroom', '💻hackathon', '🚶street')
    board = {}

    for row, column in itertools.product(range(rows), range(columns)):
        if row == 0 and column == 0:
            board[row, column] = '🏠home'  # make the start location home (0, 0)
        elif row == rows - 1 and column == columns - 1:
            board[row, column] = '💼interview'  # the final 'boss' location is at bottom left corner
        else:
            board[row, column] = random.choice(locations)  # randomly create locations
    return board
