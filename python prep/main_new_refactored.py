"""
My amazing robot!! (Refactored!)
"""

import random


def get_robot_name():
    """ Read robot's name from user.

    Returns:
        str : Robot name
    """
    name = input("What is the name of robot? ")
    return name


def generate_robot_id():
    """ Generate a unique ID for the robot. 

    Currently always returns 1000.

    Returns:
        int : robot ID
    """
    return 1000


def generate_random_position(grid_size):
    """ Generate a random (row, col) position for the robot.

    The coordinates will be between 0 to grid_size.

    Args:
        grid_size (int)

    Returns:
        int : row coordinates
        int : column coordinates
    """
    row = random.randint(0, grid_size-1) 
    col = random.randint(0, grid_size-1)
    return (row, col)


def generate_random_direction():
    """ Generate a random direction for the robot.

    Returns:
        str : direction ("n", "s", "e" or "w")
    """
    direction_index = random.randint(0, 3)
    if direction_index == 0:
        return "n"
    elif direction_index == 1:
        return "e"
    elif direction_index == 2:
        return "s"
    else:
        return "w"


def clip_position_to_boundary(row, col, grid_size):
    """ Clip the row and col to be within the grid. 

    Args:
        grid_size (int): Size of the grid

    Returns:
        int : row coordinates after clipping
        int : column coordinates after clipping
    """
    row = max(row, 0)
    col = max(col, 0)
    row = min(row, grid_size-1)
    col = min(col, grid_size-1)
    return (row, col)


def compute_quadrant(row, col, grid_size):
    """ Compute the quadrant of (row, col) in the grid. Unused at the moment.

    Args:
        row (int) : the row coordinate
        col (int) : the column coordinate
        grid_size (int) : the size of the grid

    Returns:
        str : A string description of the quadrant
    """
    midpoint = grid_size // 2

    if 0 <= row <= midpoint-1:
        row_quadrant = "top"
    else:
        row_quadrant = "bottom"

    if 0 <= col <= midpoint-1:
        col_quadrant = "left"
    else:
        col_quadrant = "right"

    return f"{row_quadrant} {col_quadrant}"


def initialise_robot(grid_size):
    """ Initialise the robot name, ID, and initial position and direction.

    Args:
        grid_size (int): The size of the grid.

    Returns:
        str : Robot name
        int : Robot ID
        int : Robot's row coordinate
        int : Robot's column coordinate
        str : Robot's direction ("n", "s", "e", or "w")
    """
    name = get_robot_name()
    identifier = generate_robot_id()
    initial_row, initial_col = generate_random_position(grid_size)
    initial_direction = generate_random_direction()
    return (name, identifier, initial_row, initial_col, initial_direction)


def print_robot_greeting(name, identifier):
    print(f"Hello. My name is {name}. My ID is {identifier}.")


def generate_direction_string(direction):
    """ Convert the shorthand direction to its full string representation.
    
    Args:
        direction (str) : current direction
        
    Returns:
        str : the full string representation of direction
    """
    if direction == "n":
        return "North"
    elif direction == "s":
        return "South"
    elif direction == "e":
        return "East"
    elif direction == "w":
        return "West"
    else:
        # Return north by default
        return "North"


def print_robot_location(row, col, direction):
    direction_string = generate_direction_string(direction)
    print(f"I am currently at ({row}, {col}), facing {direction_string}.")


def step_forward(row, col, direction):
    """ Make robot move one step forward in the current direction.

    Args:
        row (int) : current row coordinate
        col (int) : current column coordinate
        direction (str) : current direction
    
    Returns:
        row (int) : row coordinate after taking one step forward
        col (int) : column coordinate after taking one step forward
    """
    if direction == "n":
        if row > 0:
            row -= 1

    elif direction == "s":
        if row < grid_size - 1:
            row += 1

    elif direction == "w":
        if col > 0:
            col -= 1

    elif direction == "e":
        if col < grid_size - 1:
            col += 1

    return (row, col)


def move_forward_to_wall(current_row, current_col, current_direction, grid_size):
    """ Move robot forward in the current direction until it hits a wall.

    Args:
        current_row (int) : current row coordinate
        current_col (int) : current column coordinate
        current_direction (str) : current direction
        grid_size (int) : size of the grid

    Returns:
        int : row coordinate after hitting a wall
        int : column coordinate after hitting a wall
    """
    while not is_robot_facing_wall(current_row, current_col, current_direction, 
                                   grid_size):
        print_step_message()
        current_row, current_col = step_forward(current_row, current_col, 
                                                current_direction)   
        print_robot_location(current_row, current_col, current_direction)
    return (current_row, current_col)


def is_robot_facing_wall(row, col, direction, grid_size):
    """ Check if robot is currently facing a wall

    Args:
        row (int) : row coordinate
        col (int) : column coordinate
        direction (str) : direction
        grid_size (int) : size of the grid

    Returns:
        bool
    """
    return (direction == "w" and col == 0
           or direction == "e" and col == grid_size-1
           or direction == "n" and row == 0
           or direction == "s" and row == grid_size-1)


def is_robot_at_target(row, col, target_row, target_col):
    """ Check if robot is at a certain target grid cell.

    Args:
        row (int) : row coordinate
        col (int) : column coordinate
        target_row (int) : row coordinate
        target_col (int) : column coordinate

    Returns:
        bool
    """
    return row == target_row and col == target_col


def print_step_message():
    print("Moving one step forward.")


def print_wall_message():
    print("I have a wall in front of me!")


def print_rotate_message():
    print("Turning 90 degrees clockwise.")


def print_target_reached_message():
    print("I am drinking Ribena! I am happy!")


def rotate_90_deg_clockwise(direction):
    """ Rotate the robot 90 degrees clockwise.
        
    Args:
        direction (str) : "n", "e", "s" or "w"

    Returns:
        str : the direction after rotation
    """
    if direction == "n":
        return "e"
    elif direction == "e":
        return "s"
    elif direction == "s":
        return "w"
    elif direction == "w":
        return "n"
    else:
        print(f"Error rotating 90 degrees clockwise. Unknown direction {direction}.")
        exit()


def navigate(current_direction, 
            current_row, 
            current_col, 
            target_row, 
            target_col,
            grid_size):
    """ Have robot automatically navigate to a target grid cell.

    Args:
        current_direction (str) : Robot's current direction ("n", "s", "e" or "w")
        current_row (int) : Robot's current row coordinate
        current_col (int) : Robot's current column coordinate
        target_row (int) : The target row coordinate
        target_col (int) : The target column coordinate
        grid_size (int) : The size of the grid
    """
    print_robot_location(current_row, current_col, current_direction)

    while not is_robot_at_target(current_row, current_col, target_row, 
                                 target_col):
        current_row, current_col = move_forward_to_wall(current_row, 
                                                        current_col, 
                                                        current_direction, 
                                                        grid_size)

        if is_robot_at_target(current_row, current_col, target_row, target_col):
            break
        
        print_wall_message()
        
        print_rotate_message()
        current_direction = rotate_90_deg_clockwise(current_direction)
        
        print_robot_location(current_row, current_col, current_direction)
        
    print_target_reached_message()


def simulate_robot_navigation(grid_size=10, target_row=9, target_col=9):
    """ Starts a simulation session of a robot navigating to a target

    Args:
        grid_size (int) : The size of the grid. Defaults to 10.
        target_row (int) : The target row coordinate. Defaults to 9.
        target_col (int) : The target column coordinate. Defaults to 9.
    """
    name, identifier, row, col, direction = initialise_robot(grid_size)
    print_robot_greeting(name, identifier)
    navigate(direction, row, col, target_row, target_col, grid_size)


# Robot program starts here!
grid_size = 10
simulate_robot_navigation(grid_size)
