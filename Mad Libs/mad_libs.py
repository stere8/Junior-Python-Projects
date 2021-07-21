import os
import sys
import time


def closing():
    #os.system('cmd /c "cls"')
    for char in "Closing...":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(2)
    sys.exit()


def playing():
    #os.system('cmd /k "cls"')
    print("Stories : ")
    print("1. Tacos\n2. Jobs\n3. Photo Shoot\n4. Pizza Party\n")
         # "5. A Gingerbread man\n6. About Me\n7. Queen\n8. "
        #"ButterFlies")

    try:
        number = int(input("\nChoose a story number : "))
    except:
        print("\nError: Wrong Input,")
        choice = input("\nTry again ? (Y to try again or Something else to stop)")

        if choice == "Y":
            playing()
        else:
            closing()

    if number == 1 :
        words = [("Adjective",""),("Foods (plural)",""),("Verb",""),("Saying",""),("Noun",""),("Foods (plural)",""),
                 ("Color",""),("Something you would ride in",""),("Animal",""),("Person","")]
        max = len(words)
        for i in range(max):
            prompt = "\nPlease give a " + words[i][0] + " : "
            x = list(words[i])
            x[1] = input(prompt)
            words[i] = tuple(x)

        print("\nToday I went to my favorite Taco Stand called the " + words[0][1] + " " + words[8][1] + ". Unlike most food stands, they cook and prepare the food in a " + words[7][1] + " while you " + words[2][1] + ". The best thing on the menu is the " + words[6][1] + " " + words[4][1] + ". Instead of ground beef they fill the taco with " + words[5][1] + ", cheese, and top it off with a salsa made from " + words[1][1] + ". If that doesn't make your mouth water, then it' just like " + words[9][1] + " always says: " + words[3][1] + "!")
    if number == 2 :
        words = [("Occupation (a job)",""),("Noun",""),("Adjective",""),("Noun",""),("Verb",""),("Adjective",""),("Noun",""),
                 ("Verb",""),("Noun",""),("Verb","")]
        max = len(words)
        for i in range(max):
            prompt = "\nPlease give a " + words[i][0] + " : "
            x = list(words[i])
            x[1] = input(prompt)
            words[i] = tuple(x)

        print("\nToday a " + words[0][1] + " named " + words[8][1] + " came to our school to talk to us about her job. She said the most important skill you need to know to do her job is to be able to " + words[7][1] + " around (a) " + words[2][1] + " " + words[6][1] + ". She said it was easy for her to learn her job because she loved to " + words[4][1] + " when she was my age--and that helps a lot! If you're considering her profession, I hope you can be near (a) " + words[5][1] + " " + words[1][1] + ". That's very important! If you get too distracted in that situation you won't be able to " + words[9][1] + " next to (a) " + words[3][1] + "!")

    if number == 3:
        words = [("Animals", ""), ("Feeling", ""), ("Things (plural)", ""), ("A professional (like \"Baker\")", ""), ("A piece of clothing", ""),
                 ("Things (plural)", ""),("A person", ""), ("A place", ""), ("Verb (ending in -ing)", ""), ("Food", "")]
        max = len(words)
        for i in range(max):
            prompt = "\nPlease give a " + words[i][0] + " : "
            x = list(words[i])
            x[1] = input(prompt)
            words[i] = tuple(x)

        print("Say '" + words[9][1] + ",' the photographer said as the camera flashed! " + words[6][1] + " and I had gone to " + words[7][1] + " to get our photos taken today. The first photo we really wanted was a picture of us dressed as " + words[0][1] + " pretending to be a " + words[3][1] + ". When we saw the proofs of it, I was a bit " + words[1][1] + " because it looked different than in my head. (I hadn't imagined so many " + words[2][1] + " behind us.) However, the second photo was exactly what I wanted. We both looked like " + words[5][1] + " wearing " + words[4][1] + " and " + words[8][1] + "--exactly what I had in mind!")

    if number == 4:
        words = [("Things (plural) ", ""), ("Adjective", ""), ("Song Title", ""), ("A Celebrity", ""),
                 ("Feeling", ""),("Verb", ""), ("A Place", ""), ("Food", ""), ("Things (plural)", ""),
                 ("Person", "")]
        max = len(words)
        for i in range(max):
            prompt = "\nPlease give a " + words[i][0] + " : "
            x = list(words[i])
            x[1] = input(prompt)
            words[i] = tuple(x)

        print("\nI just got back from a pizza party with " + words[9][1] + ". Can you believe we got to eat " + words[1][1] + " pizza in " + words[6][1] + "?! Everyone got to choose their own toppings. I made '" + words[7][1] + " and " + words[0][1] + "' pizza, which is my favorite! They even stuffed the crust with " + words[8][1] + ". How " + words[4][1] + "! If that wasn't good enough already, " + words[3][1] + " was there singing " + words[2][1] + ". I was so inspired by the music, I had to get up out of my seat and " + words[5][1] + ".")

        input()
        sys.exit()
playing()
