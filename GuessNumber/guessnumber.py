import random
import sys
import time


def play():
    global guess
    print("\nGuess the number : \n")
    number = random.randint(1, 50)
    found = False
    while not found:
        try:
            guess = int(input("Give a number between 1-50\n"))

        except:
            print("Please input a number \n")
            pass
        if guess > 50 or guess < 0:
            print("please respect the boundaries\n")
            pass
        else:
            if guess > number:
                print("Your number is higher\n")
                pass
            elif guess < number:
                print("Your number is lower\n")
                pass
            elif guess == number:
                print("Congrats you have the right number ", number)
                time.sleep(10)
                sys.exit()


play()
