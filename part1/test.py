secret_number = 5

while True:
    guess = int(input("Guess the number (number is an integer between 0-9): "))
    if guess == secret_number:
        print("Congratulations, you have guessed the right number")
        break
    else:
        print("Sorry, wrong guess. Try once more")