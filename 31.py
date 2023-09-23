print("""You enter a room with orange and pink color.)
Do you go through pink  or orange color ?""")

door = input("> ")

if door == "pink":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do ?")
    print("1. Take the cake.")
    print("2. Scream at the bar.")
    
    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good Job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well , doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "orange":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Bluebrries.")
    print("2. Yellow jacket clothespin.")
    print("3. Understanidng revolvers yelling melodies.")
    
    insanity = input("> ")

    if insanity == "1" or insanity == "2":
       print("Your body survives powered by a mind of jello.")
       print("Good Job!")
    else:
        print("The instanity rots your eyes into a pool of muck.")
        print("Good job!")
    
else:
    print("You stumble around and fall on a knife and die. Good job!")

    