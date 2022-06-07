""" Generate the Fibonacci number at a given position.

Recursive version.

Author: Josiah Wang
"""

def fibonacci(position):
    """ Generate the Fibonacci number at a given position.
    
    Args:
        position (int): The position of the Fibonacci number (starting from 0)
    
    Returns:
        int: The Fibonacci number as the given position.
    """
    
    if position in [0, 1]:
        return position
    else:
        return fibonacci(position-1) + fibonacci(position-2)


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55


test_fibonacci()
