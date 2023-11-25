"""
Charlie Ho
A01358146
"""
import random
import json


def create_character():
    """
    Ask the player for the character's name and declare the initial state of the character.

    postcondition: initialize character coordinates, knowledge, term, stress, and name
    :return: a dictionary contain character info
    """
    character_name = input("Tell me, what is your name? ")
    print("So, your name is %s" % character_name)
    proceed = input("Is this correct? (Y/N) ").upper()
    # confirm if user has typed the correct name
    while proceed not in ['Y', 'YES']:
        proceed = input("Is this correct? (Y/N) ").upper()
    character = {"X-coordinate": 0, "Y-coordinate": 0, "Knowledge": 0, "Term": 1, "Stress": 0, "Name": character_name,
                 "Hired": False}
    return character


def game_difficulty():
    """
    Ask the player for the game difficulty.

    postcondition: initialize character coordinates, knowledge, term, stress, and name
    :return: representing the chosen difficulty level (1 for easy, 2 for medium, 3 for difficult)
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
                return float(difficulty)


def make_board(rows, columns):
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
    return board


def describe_current_location(board, character):
    """
    Return the current location on the board.

    :param board: a dictionary contains the coordinates as key and description of that location as value
    :param character: a dictionary contains character coordinates and HP
    :precondition: board must contain the location coordinates as key and each value is a string description
    :precondition: character must contain "X-coordinate", "Y-coordinate" and "Current HP" as keys
    :postcondition: retrieve location information on board base on the character coordinate
    :return: a string describing the location of the board

    >>> board1 = {(0, 0): 'library', (0, 1): 'classroom'}
    >>> character1 = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> describe_current_location(board1, character1)
    You are now at [library] on location (0, 0)
    'library'
    """
    x_coordinate = character.get("X-coordinate")
    y_coordinate = character.get("Y-coordinate")
    current_location = board[(x_coordinate, y_coordinate)]
    print(f"You are now at [%s] on location (%d, %d)" % (current_location, x_coordinate, y_coordinate))
    return current_location


def get_user_choice(character):
    """
    Obtain the user's choice of direction (North, East, South, or West) or quit game.

    :postcondition: ensures that the user's choice is valid (N, E, S, or W)
    :return: a string with the user's chosen direction
    """
    decision = input('Please enter a direction you want to go (N: North| E: East| S: South| W: West): ').upper()
    while decision not in ['N', 'S', 'E', 'W']:
        if decision == 'QUIT':
            with open('game_save.json', 'w') as output:
                json.dump(character, output)
            print("Progress has been saved. Good bye!")
            quit()
        decision = input('Not a valid option.\nPlease re-enter a direction you want to go '
                         '(N: North| E: East| S: South| W: West): ').upper()
    return decision


def validate_move(board, character, direction):
    """
    Receive the move direction and determine if the move is valid.

    :param board: a dictionary describing the board
    :param character: a dictionary describing the character
    :param direction: a string describing the desired direction
    :precondition: board must contain the location coordinates as key and each value is a string description
    :precondition: character must contain "X-coordinate", "Y-coordinate" and "Current HP" as keys
    :postcondition: validate moves based on character coordinates, width, and height of the board
    :return: boolean value
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
    :return: a dictionary containing character's updated location

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
    return character


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


def event(character, difficulty):
    """
    Simulate a typing game where the player attempts to solve a Leetcode question.
    """
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
    Determine if character's knowledge is enough to advance to next term.

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
    :return: a boolean value of whether the character is at interview location
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
        return character
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
        return character


def overwhelmed(character):
    """
    Check if character's stress reached 50.

    """
    if character["Stress"] >= 50:
        return True
    else:
        return False


def check_if_hired(character):  # should i keep this?
    """
       Check if the character has been hired.

       :param character: a dictionary representing the character, including "Hired" as key
       :postcondition: retrieve boolean value inside dictionary with the key "Hired"
       :return: the boolean vlue
        >>> check_if_hired({"Hired": False})
        False
       """
    if character["Hired"]:
        return True
    else:
        return False


def determine_location(character, board, difficulty):
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
            event(character, difficulty)


def home(character):
    """
    Decrease character's stress when at home.
    """
    character["Stress"] = max(character["Stress"] - 3, 0)  # decrease stress by 3, but won't go below zero
    print("Your cat welcomes you home 🐈")
    print("You have lower your stress [Stress = %d]" % character["Stress"])


def game():
    """
    Start the game.
    """
    rows = 5
    columns = 5
    character = create_character()
    difficulty = game_difficulty()
    board = make_board(rows, columns)
    got_hired = False
    while not overwhelmed(character) and not got_hired:
        describe_current_location(board, character)
        direction = get_user_choice(character)
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            determine_location(character, board, difficulty)
            if character_advance(character):
                advance(character)
            got_hired = check_if_hired(character)
        else:
            print("Ouch! You hit a wall! 🧱")
    if got_hired: # good end
        print('-'*80)
        print("We need you!")
        print("Congrats! You have landed your dream job!")
        print('-'*80)

    if overwhelmed(character):  # bad end
        print('-'*80)
        print("Sorry! You have passed out and when you wake up, you no longer want to go to school.")
        print('-'*80)


def main():
    """
    Execute the game function.
    """
    print('-' * 80)
    print("I am pleased to inform you that you have been accepted to Level 1 of the CST program. ")
    print("Congratulations and best wishes in your future studies.")
    print('-' * 80)
    print('\t \t \t \t Tips for playing')
    print('1. You are a student, which means you have to gain knowledge to advance to other terms.')
    print('2. Keep your stress level below 50, or you will pass out.')
    print('3. You goal is to get hired at Term 4, you can go to location (4,4) for job interview.')
    print('4. If your knowledge is <= 15, you will not be hired.')
    print('-' * 80)
    game()


if __name__ == '__main__':
    main()
