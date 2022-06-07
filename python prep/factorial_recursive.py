""" Factorial (recursive version)

Author: Josiah Wang
"""

def factorial(n):
    """ Compute the factorial of n.
    
    Args:
        n (int) : A positive integer
        
    Returns:
        int : The factorial of n
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def test_factorial():
    assert factorial(1)  == 1
    assert factorial(2) == 2
    assert factorial(3)  == 6
    assert factorial(4)  == 24
    assert factorial(5)  == 120


test_factorial()

print(factorial(3))
print(factorial(5))
