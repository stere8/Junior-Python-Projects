def Ask():
    f = open("toread.txt","r")
    text = f.read()

    number = len(text.split(" "))

    print("You were able to say about your day in ", number," words")
Ask()