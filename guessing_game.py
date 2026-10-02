import random


def check_guess(secret_number, guess):
    # Check if the guess is between 1 and 1000
    if guess < 1 or guess > 1000:
        return "Please enter a number between 1 and 1000."

    # Check if the guess is odd
    elif guess % 2 == 0:
        return "Please enter an odd number."

    # Check if the guess is too low
    elif guess < secret_number:
        return "Too low!"

    # Check if the guess is too high
    elif guess > secret_number:
        return "Too high!"

    # The guess is correct
    else:
        return "Correct! You guessed the number!"


def play_game():
    # Pick a random odd number between 1 and 1000
    secret_number = random.randrange(1, 1001, 2)

    print("Guessing Game")
    print("Guess an odd integer between 1 and 1000.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        result = check_guess(secret_number, guess)
        print(result)

        if guess == secret_number:
            break


# Start the game
if __name__ == "__main__":
    play_game()