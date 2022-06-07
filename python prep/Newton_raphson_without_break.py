n = float(input("Please enter a positive number: "))
guess = n
epsilon = 0.0000001
found = False

while not found:
    old_guess = guess
    guess = (guess + n/guess) * 0.5
    if abs(guess - old_guess) < epsilon:
        found = True
        print(guess)