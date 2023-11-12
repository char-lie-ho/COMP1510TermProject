"""
Charlie Ho
A01358146
"""


def create_character():
    character_name = input("Tell me, what is your name? ")
    print("So, your name is %s" % character_name)
    proceed = input("Is this correct? (Y/N) ").upper()
    # check if users want to change their mind
    while proceed != 'Y':
        proceed = input("Is this correct? (Y/N) ").upper()
    player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Level": 1, "Name": character_name}
    print("OK. Let's begin!")
    return player


def game():
    create_character()


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
