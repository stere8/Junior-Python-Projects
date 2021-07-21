def AcroMize():
    name = input("Input the Organization's name : ")
    words = name.split(" ")
    acronym = ""
    words = list(filter(None,words))
    print(words)
    for word in words:
        if word[0]:
            acronym = acronym + word[0].upper()
    print("\n"+acronym)

AcroMize()