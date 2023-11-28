"""
Charlie Ho
A01358146
"""
import random
import json


def create_character():  # DONE
    """
    Ask the player for the character's name and declare the initial state of the character.

    postcondition: initialize character coordinates, knowledge, term, stress, name, hired, and difficulty
    :return: a dictionary contain character info
    """
    with open("intro.txt") as file_object:
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


def game_difficulty(character):  # DONE
    """
    Ask the player for the game difficulty.

    :param character: a dictionary contains character status
    :precondition: character must contain 'Difficulty' as keys
    postcondition: the 'Difficulty' key in the 'character' dictionary will be updated based on the user's input
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


def make_board(rows, columns):  # DONE
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
    for row in range(rows):
        for column in range(columns):
            if row == 0 and column == 0:
                board[(row, column)] = '🏠home'  # make the start location home (0, 0)
            elif row == 4 and column == 4:
                board[(row, column)] = '💼interview'  # the final 'boss' location (4, 4)
            else:
                board[(row, column)] = random.choice(locations)  # randomly create locations
    print(board)
    return board


def describe_current_location(board, character):  # DONE
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
    print(f"You are now at [%s] on location (%d, %d)" % (current_location, x_coordinate, y_coordinate))
    display_map(x_coordinate, y_coordinate)
    return current_location


def display_map(x_coordinate, y_coordinate):  # DONE
    """
    Display a simple map.

    :param x_coordinate: x-coordinate of the character
    :param y_coordinate: y-coordinate of the character
    :precondition: x_coordinate must be non-negative integer and less than 5
    :precondition: y_coordinate must be non-negative integer and less than 5
    :postcondition: prints a map with borders and a character at the specified coordinates
    """
    for row in range(11):
        top_board = ["\t", "┍", "⎯", "┬", "⎯", "┬", "⎯", "┬", "⎯", "┬", "⎯", "┑"]
        bottom_board = ["\t", "┕", "⎯", "┴", "⎯", "┴", "⎯", "┴", "⎯", "┴", "⎯", "┙"]
        center_lines = ["\t", "├", "⎯", "┼", "⎯", "┼", "⎯", "┼", "⎯", "┼", "⎯", "┤"]
        center_space = ["\t", "|", " ", '|', " ", '|', " ", '|', " ", '|', " ", '|']
        if row == 0:
            line_to_print = top_board
        elif row == 10:
            line_to_print = bottom_board
        else:
            if row % 2 != 0:
                if y_coordinate * 2 + 1 == row:
                    center_space[x_coordinate * 2 + 2] = 'x'
                line_to_print = center_space
            else:
                line_to_print = center_lines
        print(" ".join(line_to_print))


def get_user_choice(character):  # DONE
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


def validate_move(board, character, direction):  # done
    """
    Receive the move direction and determine if the move is valid.

    :param board: a dictionary describing the board
    :param character: a dictionary describing the character
    :param direction: a string describing the desired direction
    :precondition: board must contain the location coordinates as key and each value is a string description
    :precondition: character must contain "X-coordinate", "Y-coordinate" and "Current HP" as keys
    :postcondition: validate moves based on character coordinates, width, and height of the board
    :return: boolean value

    >>> board1 = {(0, 0): '🏠home', (0, 1): '💻hackathon', (1, 0): '📚library', (1, 1): '🚶street'}
    >>> character1 = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> direction_N = 'N'
    >>> validate_move(board1, character1, direction_N)
    False
    >>> direction_S = 'S'
    >>> validate_move(board1, character1, direction_S)
    True
    """
    current_character_x_coordinate = character.get("X-coordinate")
    current_character_y_coordinate = character.get("Y-coordinate")
    max_x_location = max(coord[0] for coord in board.keys())
    max_y_location = max(coord[1] for coord in board.keys())
    if current_character_y_coordinate == 0 and direction == "N":
        return False
    elif current_character_x_coordinate == 0 and direction == "W":
        return False
    elif current_character_x_coordinate == max_x_location and direction == "E":
        return False
    elif current_character_y_coordinate == max_y_location and direction == "S":
        return False
    else:
        return True


def move_character(character, direction):
    """
    Move the character to a new location.

    :param character: a dictionary describing the character
    :param direction: a string representing the direction to move
    :precondition: character must contain "X-coordinate", "Y-coordinate" as keys
    :precondition: direction must be either "N", "S", "W", or "E"
    :postcondition: update character's coordinates

    >>> character1 = {'X-coordinate': 1, 'Y-coordinate': 1}
    >>> direction1 = 'N'
    >>> move_character(character1, direction1)
    {'X-coordinate': 1, 'Y-coordinate': 0}
    >>> character2 = {'X-coordinate': 1, 'Y-coordinate': 1}
    >>> direction2 = 'W'
    >>> move_character(character2, direction2)
    {'X-coordinate': 0, 'Y-coordinate': 1}
    """
    if direction == "N":
        character["Y-coordinate"] -= 1
    elif direction == "S":
        character["Y-coordinate"] += 1
    elif direction == "W":
        character["X-coordinate"] -= 1
    else:
        character["X-coordinate"] += 1


def encounter_event():
    """
    Determine if the player encounters an event.

    :postcondition: return a boolean value indicating whether the character encounters an event
    :return: a boolean value of character-event encounter
    """
    encounter = random.random()
    if encounter < 0.25:  # the chance of an event happens is 25%
        return True
    else:
        return False


def event(character):
    """
    Simulate a typing game where the player attempts to solve a Leetcode question.
    """
    difficulty = character["Difficulty"]
    progress = 0
    attempt_times = 0
    print('You discover an interesting Leetcode Question.🤔\n(Hint: You can type anything to try to solve.)')
    while progress < 100:
        attempt_text = input()
        # the player will make progress when the enter something
        if attempt_text:
            attempt_times += 1
            progress += random.randint(10, 50)
            progress = min(progress, 100)  # ensure progress doesn't exceed 100
            print('You have finished %d%%' % progress)
        else:
            print('Hint: You can type anything to try to solve.')
    character["Knowledge"] += (4 - difficulty) * 1  # higher difficulty will have less gained knowledge
    character["Stress"] += attempt_times
    print('Great job, %s! ' % character['Name'])
    print('You have learned from this. [Knowledge = %d]' % character["Knowledge"])
    print('However, you are more stressed now. [Stress = %d]' % character["Stress"])


def character_advance(character):
    """
    Determine if character's knowledge is enough to advance to the next term.

    :param character: a dictionary describing the character
    :precondition: character must contain "Term", "Knowledge" as keys
    :postcondition: calculates whether the character has enough knowledge to advance to the next term
    :return: a boolean value of whether character advances
    """
    character_term = character["Term"]
    character_knowledge = character["Knowledge"]
    decision_of_advance = False
    # Only 4 terms in this game
    if character_term < 4:
        # Each term requires 5 knowledge points
        decision_of_advance = character_knowledge / 5 >= character_term
    return decision_of_advance


def advance(character):
    """
    Make the character to advance to next term.

    :param character: a dictionary describing the character
    :precondition: character must contain "Term" and "Stress" as keys
    :postcondition: updates the character's term, and reduces stress
    """
    character["Term"] += 1
    print('Excellent!')
    print('You are now in Term %d' % character["Term"])
    character["Stress"] -= 5
    print('After the term break, you are more refreshed! [Stress: %d]' % character["Stress"])


def interview(character):
    """
    Simulate a job interview process and assess the character's suitability for the position.

    :param character: a dictionary describing the character
    :precondition: character must contain "Knowledge" and "Stress"as keys
    :postcondition: modify the character's info based on the game's outcome
    """
    # the character has to have 15 knowledge to have a chance to be hired
    print('You have arrive the interview room.')
    if character["Knowledge"] <= 15:
        character["Stress"] += 10
        character["Knowledge"] += 1
        print('Sorry, your skills and experience do not meet our current needs.')
        print('Please try to study more and come back.')
        print('You are exhausted from this interview. [Stress = %d]' % character["Stress"])
        print('However, you also learn from this. [Knowledge = %d]' % character["Knowledge"])
    else:
        actual_number = random.randint(1, 5)
        guess_number = input('People say interviewing is a numbers game, let\'s pick a number between 1 and 5. ')
        try:
            guess_number = int(guess_number)
        except ValueError:
            character["Stress"] += 5
            print("Oh, you can't even type numbers?!")
            print('Sorry, your skills and experience do not meet our current needs.')
            print('Your current stress is [Stress = %d]' % character["Stress"])
        else:
            if actual_number != guess_number:
                character["Stress"] += 5
                print('Sorry, your skills and experience do not meet our current needs.')
                print('[Stress +5], your current stress is [Stress = %d]' % character["Stress"])
            else:
                character["Hired"] = True


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


def determine_location(character, board):
    """
    Obtain character's location to determine the trigger event.
    """
    x_coordinate = character.get("X-coordinate")
    y_coordinate = character.get("Y-coordinate")
    current_location = board[(x_coordinate, y_coordinate)]
    if current_location == '🏠home':
        home(character)
    elif current_location == '💼interview':
        interview(character)
    else:
        if encounter_event():
            event(character)


def home(character):
    """
    Decrease character's stress when at home.
    """
    character["Stress"] = max(character["Stress"] - 3, 0)  # decrease stress by 3, but won't go below zero
    print("Your cat welcomes you home 🐈")
    print("You have lower your stress [Stress = %d]" % character["Stress"])


def load_progress():
    """
    Load the previous saved progress.
    """
    with open('game_save.json') as file_object:
        character = json.load(file_object)
    decision = None
    while decision not in ["Y", "N"]:
        decision = input('You have a saved progress, do you want to load the progress? (Y/N) ').upper()
    if decision == "Y":
        print("Welcome back, %s!" % character["Name"])
    else:
        character = create_character()
    return character


def game():
    """
    Start the game.
    """
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    try:
        open('game_save.json')  # not sure if i need to close this or use with open
    except FileNotFoundError:
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
    if character["Hired"]:  # good end
        print('-' * 80)
        print("We need you!")
        print("Congrats! You have landed your dream job!")
        print('-' * 80)

    elif character["Stress"] >= 50:  # bad end
        print('-' * 80)
        print("Sorry! You have passed out and when you wake up, you no longer want to go to school.")
        print('-' * 80)


def main():
    """
    Execute the game function.
    """
    game()


if __name__ == '__main__':
    main()
