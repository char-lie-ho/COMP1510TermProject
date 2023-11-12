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
                board[(row, column)] = 'home'  # make the start location home
            elif row == 0 or column == 0:
                board[(row, column)] = 'street'  # make the top and left edge locations to street
            elif row == 4 and column == 4:
                board[(row, column)] = 'interview'  # the final 'boss' location
            else:
                board[(row, column)] = random.choice(list_of_locations)  # randomly create locations
    return board


def describe_current_location(board, character):
    x_coordinate = character.get("X-coordinate")
    y_coordinate = character.get("Y-coordinate")
    current_location = board[(x_coordinate, y_coordinate)]
    print(f"You are now at %s on location (%d, %d)" % (current_location, x_coordinate, y_coordinate))
    return current_location


def game():
    character = create_character()
    # game_difficulty()
    # make_board()
    board = make_board()
    got_hired = False
    describe_current_location(board, character)




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
