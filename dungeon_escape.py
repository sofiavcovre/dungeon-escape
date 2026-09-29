print("===============================")
print("        DUNGEON ESCAPE         ")
print("===============================")

print()

print("You wake up in a dark dungeon cell.")
print("There is a wooden door in front of you.")

print()

print("What do you do?")

print()

print("1. Try to open the door")
print("2. Search the cell")
print("3. Try to shout for help.")

answer_1 = int(input("Which choice do you choose?: "))


# FIRST CHOICE
if answer_1 == 1:
    print()
    print("The door is locked. You cannot open it.")
    print()


elif answer_1 == 2:
    print()
    print("You find 3 items. Which one do you choose?")
    print("1. An old hair brush")
    print("2. A human skull.")
    print("3. A rusty screwdriver.")
    print()

    answer_2 = int(input("Which choice do you choose?: "))


    # SECOND CHOICE
    if answer_2 == 1:
        print()
        print("Now is not the time to groom yourself.")


    elif answer_2 == 2:
        print()
        print("Whose head is that?")


    elif answer_2 == 3:
        print()
        print("Maybe this screwdriver can be useful.")
        print()
        print("Do you want to use the screwdriver to:")
        print("1. Open the door")
        print("2. Open a nearby chest")
        print()

        answer_3 = int(input("Which choice do you choose?: "))


        # THIRD CHOICE
        if answer_3 == 1:
            print()
            print("The door successfully opened!")
            print()
            print("You walk out of the cell only to find a long hallway")
            print("with a door on the left, and another on the right.")
            print()
            print("Do you want to enter the door on the:")
            print()
            print("Left")
            print("or")
            print("Right")
            print()

            #Fourth Choice

            answer_4 = input("What choice do you choose?: ")
            if answer_4.lower() == "left":
                print()
                print("The door opens to a dimly lit old library room.")
                print()
                print("You go inside and find nothing but old books writted in languages you dont understand.")
                print()
                print("You reach to pick up a book from the bookshelf, only for it to open a secret door")
                print("You go inside to spot a small tunnel that you can barely fit in, but you decide to crawl in either way to try to find the exist.")
                print()
                print("As you continue crawling, you have the choice to crawl left or right.")
                answer_5 = input("Do you go left or right?").lower()
                if answer_5.lower() == "left":
                    print("As you turned left, you heard the low hiss of a snake that was waiting for you.")
                    print()
                    print("It wrapped itself around your neck, leaving you unable to breathe.")
                    print()
                    print("Game over.")
                    print()
                elif answer_5.lower() == "right":
                    print()
                    print("You managed to crawl your way up and out of the sewers. You're officially out of the dungeon!")
                    print()
                    print("Congratulations! You won the game!")
                    print()
                else:
                    print("Ivalid Choice")
            elif answer_4.lower() == "right":
                print()
                print("You enter the room to find an abandoned cave mine.")
                print()
                print("You hear footsteps getting closer to you. Do you:")
                print()
                print("A. Run away from the footsteps")
                print("B. Walk towards the footstep.")
                answer_6 = input("Which do you choose?: ").upper()
                if answer_6 == "A":
                    print("You ran away as fast as you could from the footsteps.")
                    print()
                    print("The cave mine was dark and you couldn't see your surroundings, causing you to hit your head on a heavyrock as you ran.")
                    print()
                    print("Game Over.")
                elif answer_6 == "B":
                    print()
                    print("You decide to swallow your fear and walk towards the footsteps.")
                    print()
                    print("You finally reach a tall man in police clothing with a flashlight, "
                    "and he reveals that he had been searching for you after your daughter filed a missing person report.")
                    print()
                    print("He revealed to you that you have Alzeimers and you wandered off alone to try and find your late spouse that passed 20 years ago.")
                    print()
                    print("You are taken back to the seniors home.")
                    print()
                    print("Game over.")
                    print()

            
            
            else:
                print("Invalid Choice.")

        elif answer_3 == 2:
            print()
            print("A tarantula jumped out of the chest and bit you in the neck.")
            print()
            print("Game Over.")
            print()


        else:
            print()
            print("Invalid Choice.")


    else:
        print()
        print("Invalid Choice.")


elif answer_1 == 3:
    print()
    print("No one is nearby to hear you.")


else:
    print()
    print("Invalid Choice.")


    