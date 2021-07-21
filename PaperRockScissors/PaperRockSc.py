import random
import sys
import time

import keyboard

choices = ['Rock', 'Paper', 'Scissors']


def play():
    input("Press start to play")
    print("Shi")
    time.sleep(1)
    print("Fu")
    time.sleep(1)
    print("Mi")
    print("\n"+ random.choices(choices)[0] + "\n")
    time.sleep(2)
    print("Press Space to continue or anything else to cancel\n")

    if keyboard.read_key() == "space" :
        play()
    else :
        sys.exit()

play()



