import random
mark = 0

while (True):

    print ("mark : " +str (mark))

    choice = input ("1. stone \n2. paper \n3. Scissors \nChoose your option : ")
    choice = int (choice)

    if (choice == 0) :
        break
    
    if (choice != 1) and (choice != 2) and (choice != 3):
        print ("Your input is invalid")

    choicesystem = random.randint(1,3)
    x = ""

    if choicesystem == 1 : x = "stone"
    elif choicesystem == 2 : x = "paper"
    elif choicesystem == 3 : x = "Scissors"
    print ("System selection : "+x)

    if (choicesystem == 1 and choice == 2) or (choicesystem == 2 and choice == 3) or (choicesystem == 3 and choice == 1):
        print ("You got a positive score")
        mark += 1

    elif (choicesystem == choice):
        print ("Your choice is equal to the choice of system")

    else :
        print ("game over")
        mark -= 1

    print ("\n") 
