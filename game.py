"""
Charlie Ho
A01358146
"""
import random


def create_character():
    character_name = input("Tell me, what is your name? ")
    print("So, your name is %s" % character_name)
    proceed = input("Is this correct? (Y/N) ").upper()
    # check if users want to change their mind
    while proceed != 'Y':
        proceed = input("Is this correct? (Y/N) ").upper()
    player = {"X-coordinate": 0, "Y-coordinate": 0, "Intelligence": 5, "Term": 1, "Stress": 0, "Name": character_name}
    return player


def game_difficulty():
    while True:
        difficulty = input("Life is hard, how hard you want this adventure to be on a scale "
                           "from 1 (easiest) to 3 (difficult)? ")
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
                return difficulty


def make_board():
    rows = 5
    columns = 5
    list_of_locations = ('study room', 'library', 'classroom', 'hackathon')  # may add more locations
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
                          'Please re-enter a direction you want to go (N: North| E: East| S: South| W: West): ')
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


def game():
    character = create_character()
    # game_difficulty()
    # make_board()
    board = make_board()
    got_hired = False
    while not got_hired:
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            pass
            # move_character(character)
        else:
            print("You hit a wall! ")


def main():
    """
    Execute the game function.
    """
    print('-' * 80)
    print("\t \t Welcome!")
    print('-' * 80)
    game()


if __name__ == '__main__':
    main()
