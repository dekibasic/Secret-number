print("Welcome in 'Guess th secret number' game!")

secret_number = 5
guess = int(input("Enter number between 1 and 20: "))

if guess == secret_number:
    print("Congratulations, you guessed secret number!")
else:
    print("Sorry, more luck next time!")

print("Thank you for playing our game!")