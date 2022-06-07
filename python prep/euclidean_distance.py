#implement a function using a test first approach [incrementally]


import math

def euclidean_distance(x1, y1, x2, y2):
    """ Compute the Euclidean distance between two 2D points.

    Args:
        x1 (float): x-coordinate of the first point
        y1 (float): y-coordinate of the first point
        x2 (float): x-coordinate of the second point
        y2 (float): y-coordinate of the second point

    Returns:
        float: The Euclidean distance
    """
    dx = x2 - x1
    dy = y2 - y1
    d_squared = dx**2 + dy**2
    dist = math.sqrt(d_squared)
    return dist
    
distance = euclidean_distance(2, 3, -2, 1)
expected_answer = 4.4721
epsilon = 0.0001
if abs(distance - expected_answer) < epsilon:
    print("Test passed")
else:
    print(f"Test failed. {expected_answer} expected, but {distance} returned.")