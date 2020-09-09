import random

random_number = random.randint(1,10)

while True:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if guess > random_number:
        print("Your number is too high! Try again.")
    elif guess < random_number:
        print("Your number is too low! Try again.")
    else: 
        print("YOU WIN!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thanks for playing!")
            break
