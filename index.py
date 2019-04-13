print("Welcome in 'Guess th secret number' game!")

secret_number = 5


for x in range(5):
    guess = int(input("Enter number between 1 and 20: "))
    if guess == secret_number:
        print("Congratulations, you guessed secret number!")
        break
    else:
        print("Sorry, secret number is not " + str(guess))