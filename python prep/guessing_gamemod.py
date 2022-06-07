user_message = "Please enter a number: "
incorrect_message = "Incorrect."
correct_message = "Correct."
game_over_message = "Game over."

secret_number = 42
max_guesses = 5
num_of_guesses = 1

guess = int(input(user_message))

while guess != secret_number and num_of_guesses < max_guesses:
    print(incorrect_message)
    guess = int(input(user_message))
    num_of_guesses = num_of_guesses + 1

if guess == secret_number:
    print(correct_message)
else:
    print(incorrect_message + " " + game_over_message)