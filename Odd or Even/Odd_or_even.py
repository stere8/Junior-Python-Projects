import sys, time


def closing():
    for char in "Closing...":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.2)

    time.sleep(5)
    sys.exit()


def playing():
    try:
        number = int(input("\n Please give your number: "))
    except:
        print("\nError: Wrong Input,")
        choice = input("\nTry again ? (Y to try again or Something else to stop)")

        if choice == "Y" :
            playing()
        else :
            closing()

    if number%2 == 0 :
        print("\nYour number is even")
    else :
        print("\nYour number is odd")

    choice = input("\nPlay again ? (Y to try again or Something else to stop)")

    if choice == "Y":
        playing()
    else:
        closing()

playing()

