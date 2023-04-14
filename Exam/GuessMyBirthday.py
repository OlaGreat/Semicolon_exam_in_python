
birthday = int(input("Guess My BirthDay"))
if birthday == 18:
    print("Correct Guess")
else:
    print("Incorrect Guess")
    while birthday != 18:
        birthday = int(input("Guess My BirthDay"))
        if birthday == 18:
            print("Correct Guess")
        else:
            print("Incorrect Guess")

