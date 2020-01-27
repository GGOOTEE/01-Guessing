import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

name = input("\n~ HELLO! What is your name new challenger?\n")
quit = False
range = 20
while not quit:
    random_number = random.randint(1,range)
    count = 0
    number = -1
    print("\n~ Welcome to the guessing game, %s" % name)
    while number != random_number:
        number = input("~ Please guess a number between 1 and {}:\n".format(range))
        if not number.isdigit():
            print("~ Please guess a number!\n")
        
        else:
            number = int(number)
            count = count + 1
            if number > random_number:
                print("~ Sorry, you have guessed wrong!")
                print("~ Your guess is too high!\n")
            elif number < random_number:
                print("~ Sorry, you have guessed wrong!")
                print("~ Your guess too low!\n")

    print("~ Congratulations, you have guessed correctly!")
    print("~ You guessed the correct number in {} tries!\n".format(count))
    play_again = input("~ Would you like to play again (yes or no)?\n")
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y":
        quit = False
    else:
        quit = True
print("~ Thanks for playing!\n")


