# Health Management System

opt1 = int(input("Enter 1 to Lock\nEnter 2 to Retrieve\n"))
opt2 = int(input("Enter 1 for Harry\nEnter 2 for Rohan\nEnter 3 for Hamad\n"))
opt3 = int(input("Enter 1 for Diet\nEnter 2 for Exercise\n"))


def datetime():
    import datetime
    return datetime.datetime.now()


def harry_diet():
    if opt1 == 1:
        file = open("Harry_diet.txt", "a")
        context = file.write(str(datetime()) + " " + input("What did Harry ate:\n") + "\n")
        print(context)

        file.close()
    elif opt1 == 2:
        file = open("Harry_diet.txt", "r")
        context = file.read()
        print(context)

        file.close()
    else:
        print("Sorry, You have selected wrong option!!!")


def harry_exercise():
    if opt1 == 1:
        file = open("Harry_exercise.txt", "a")
        context = file.write(str(datetime()) + " " + input("What exercise Harry did:\n") + "\n")
        print(context)

        file.close()
    elif opt1 == 2:
        file = open("Harry_exercise.txt", "r")
        context = file.read()
        print(context)

        file.close()
    else:
        print("Sorry, You have selected wrong option!!!")


def rohan_diet():
    if opt1 == 1:
        file = open("Rohan_diet.txt", "a")
        context = file.write(str(datetime()) + " " + input("What did Rohan ate:\n") + "\n")
        print(context)

        file.close()
    elif opt1 == 2:
        file = open("Rohan_diet.txt", "r")
        context = file.read()
        print(context)

        file.close()
    else:
        print("Sorry, You have selected wrong option!!!")


def rohan_exercise():
    if opt1 == 1:
        file = open("Rohan_exercise.txt", "a")
        context = file.write(str(datetime()) + " " + input("What exercise Rohan did:\n") + "\n")
        print(context)

        file.close()
    elif opt1 == 2:
        file = open("Rohan_exercise.txt", "r")
        context = file.read()
        print(context)

        file.close()
    else:
        print("Sorry, You have selected wrong option!!!")


def hamad_diet():
    if opt1 == 1:
        file = open("Hamad_diet.txt", "a")
        context = file.write(str(datetime()) + " " + input("What did Hamad ate:\n") + "\n")
        print(context)

        file.close()
    elif opt1 == 2:
        file = open("Hamad_diet.txt", "r")
        context = file.read()
        print(context)

        file.close()
    else:
        print("Sorry, You have selected wrong option!!!")


def hamad_exercise():
    if opt1 == 1:
        file = open("Hamad_exercise.txt", "a")
        context = file.write(str(datetime()) + " " + input("What exercise Hamad did:\n") + "\n")
        print(context)

        file.close()
    elif opt1 == 2:
        file = open("Hamad_exercise.txt", "r")
        context = file.read()
        print(context)

        file.close()
    else:
        print("Sorry, You have selected wrong option!!!")


if opt2 == 1 and opt3 == 1:
    print(harry_diet())
elif opt2 == 1 and opt3 == 2:
    print(harry_exercise())
elif opt2 == 2 and opt3 == 1:
    print(rohan_diet())
elif opt2 == 2 and opt3 == 2:
    print(rohan_exercise())
elif opt2 == 3 and opt3 == 1:
    print(hamad_diet())
elif opt2 == 3 and opt3 == 2:
    print(hamad_exercise())
else:
    print("Sorry, You have selected wrong option!!!")
