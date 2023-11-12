"""
Charlie Ho
A01358146
"""


def create_character():
    character_name = input("Tell me, what is your name? ")
    print("So, your name is %s" % character_name)
    proceed = input("Is this correct? (Y/N) ").upper()
    while proceed != 'Y':
        proceed = input("Is this correct? (Y/N) ").upper()
    print("OK. Let's begin!")


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
