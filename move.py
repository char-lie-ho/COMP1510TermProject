def validate_move(board, character, direction):
    """
    Receive the move direction and determine if the move is valid.

    :param board: a dictionary describing the board
    :param character: a dictionary describing the character
    :param direction: a string describing the desired direction
    :precondition: board must contain the location coordinates as key and each value is a string description
    :precondition: character must contain "X-coordinate", "Y-coordinate" and "Current HP" as keys
    :postcondition: validate moves based on character coordinates, width, and height of the board
    :return: boolean value True if the move is valid, otherwise False

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
    if ((current_character_y_coordinate == 0 and direction == "N") or
            (current_character_x_coordinate == 0 and direction == "W") or
            (current_character_x_coordinate == max_x_location and direction == "E") or
            (current_character_y_coordinate == max_y_location and direction == "S")):
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
    return character
