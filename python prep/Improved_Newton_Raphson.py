n = float(input("Please enter a positive number: "))
guess = n - 1
epsilon = 0.0000001

while abs(guess*guess - n) > epsilon:
    guess = (guess + n/guess) * 0.5

print(guess)