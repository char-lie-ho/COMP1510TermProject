"""
Charlie Ho
A01358146
"""
import random


def create_character():
    character_name = input("Tell me, what is your name? ")
    print("So, your name is %s" % character_name)
    proceed = input("Is this correct? (Y/N) ").upper()
    # confirm if user has typed the correct name
    while proceed != 'Y':
        proceed = input("Is this correct? (Y/N) ").upper()
    character = {"X-coordinate": 0, "Y-coordinate": 0, "Knowledge": 0, "Term": 1, "Stress": 0, "Name": character_name,
                 "Hired": False}
    return character


def game_difficulty():
    while True:
        difficulty = input("Life is hard, how hard you want this adventure to be on a scale "
                           "from 1 (easy) to 3 (difficult)? ")
        try:
            float(difficulty)
        except ValueError:
            print("Oh, you can't even type numbers?!")  # if user input is not a number
        else:
            if float(difficulty) not in [1, 2, 3]:  # if user input is not an integer
                print("Please enter an integer.")
                continue
            else:
                print("Great! I like your choice.")
                return int(difficulty)


def make_board():
    rows = 5
    columns = 5
    list_of_locations = ('study room', 'library', 'classroom')  # may add more locations
    board = {}
    for row in range(rows):
        for column in range(columns):
            if row == 0 and column == 0:
                board[(row, column)] = 'home'  # make the start location home (0, 0)
            elif row == 4 and column == 4:
                board[(row, column)] = 'interview'  # the final 'boss' location (4, 4)
            elif row == 0 or column == 0 or row == 4 or column == 4:
                board[(row, column)] = 'street'  # make the edge locations to street
            else:
                board[(row, column)] = random.choice(list_of_locations)  # randomly create locations
    return board


def describe_current_location(board, character):
    x_coordinate = character.get("X-coordinate")
    y_coordinate = character.get("Y-coordinate")
    current_location = board[(x_coordinate, y_coordinate)]
    print(f"You are now at %s on location (%d, %d)" % (current_location, x_coordinate, y_coordinate))
    return current_location


def get_user_choice():
    """
    Obtain the user's choice of direction (North, East, South, or West).

    :postcondition: ensures that the user's choice is valid (N, E, S, or W)
    :return: a string with the user's chosen direction
    """
    direction = input('Please enter a direction you want to go (N: North| E: East| S: South| W: West): ').upper()
    while direction not in ['N', 'S', 'E', 'W']:
        direction = input('Not a valid option.\n'
                          'Please re-enter a direction you want to go (N: North| E: East| S: South| W: West): ').upper()
    return direction


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
    if encounter < 1:
        return True
    else:
        return False


def event(character, difficulty):
    progress = 0
    print('You are trying solve a Leetcode Question. (Hint: You can type anything to try to solve.)')
    print('You have finished %d%%' % progress)
    while progress < 100:
        attempt = input()
        # the player will make progress when the enter something
        if attempt is not "":
            progress += random.randint(5, 50)
            if progress <= 100:
                print('You have finished %d%%' % progress)
            else:
                print('You have finished 100% ! Great Job.')
                character["Knowledge"] += (4 - difficulty) * 1  # higher difficulty will have less gained knowledge
                character["Stress"] += 5 * difficulty  # higher difficulty will result in higher stress
                print('You have learned from this. You knowledge is now %d.' % character["Knowledge"])
                print('However, you are more stressed now. [Stress = %d]' % character["Stress"])
        else:
            print('Hint: You can type anything to try to solve.')


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


def at_interview(character):
    """
    Check if character is at term 4 and location (4,4).
    """
    x_coordinate = character.get("X-coordinate")
    y_coordinate = character.get("Y-coordinate")

    if x_coordinate == 4 and y_coordinate == 4:
        return True
    else:
        return False


def interview(character):
    """
    Determine if character has enough knowledge to get hired.
    """
    # if character's knowledge is less than 10, 0 chance
    # after 10, each point of knowledge increase 10% chances

    character_knowledge = character["Knowledge"]
    character_stress = character["Stress"]
    if character_knowledge <= 15:
        character["Stress"] += 10
        print('Sorry, your skills and experience do not meet our current needs.')
        print('[Stress +10], your current stress is %d' % character_stress)
        print('However, you also learn from this [Knowledge +1], you knowledge is %d' % character_knowledge)
        return character
    else:
        actual_number = 1
        guess_number = input('People say interviewing is a numbers game, let\'s pick a number between 1 and 5. ')
        try:
            guess_number = int(guess_number)
        except ValueError:
            character["Stress"] += 5
            print("Oh, you can't even type numbers?!")
            print('Sorry, your skills and experience do not meet our current needs.')
            print('[Stress +5], your current stress is %d' % character_stress)
        else:
            if actual_number != guess_number:
                character["Stress"] += 5
                print('Sorry, your skills and experience do not meet our current needs.')
                print('[Stress +5], your current stress is %d' % character_stress)
            else:
                print("We need you!")
                character["Hired"] = True
            return character


def overwhelmed(character):
    """
    Check if character's stress reached 100.
    """
    if character["Stress"] >= 100:
        return True
    else:
        return False


def check_if_hired(character):
    if character["Hired"]:
        return True
    else:
        return False


def game():
    """
    Start the game.
    """
    character = create_character()
    difficulty = game_difficulty()
    board = make_board()
    got_hired = False
    while not overwhelmed(character) and not got_hired:
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            if at_interview(character):
                interview(character)
            else:
                there_is_an_event = encounter_event()
                if there_is_an_event:
                    event(character, difficulty)
                    if character_advance(character):
                        advance(character)
            got_hired = check_if_hired(character)
        else:
            print("You hit a wall! ")
    if got_hired:
        print('-'*80)
        print("Congrats! You have landed your dream job!")
        print('-'*80)

    if overwhelmed(character):
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
    game()


if __name__ == '__main__':
    main()
