n = float(input("Please enter a positive number: "))
guess = n
epsilon = 0.0000001

while True:
    old_guess = guess
    guess = (guess + n/guess) * 0.5
    if abs(guess - old_guess) < epsilon:
        print(guess)
        break