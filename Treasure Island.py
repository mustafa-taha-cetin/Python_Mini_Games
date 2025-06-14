
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome the Treasure Island.")
print("Your mission is to find the treasure.")

secim1 = input("where do you want to go? left or right\n")
secim1 = secim1.lower()
print(secim1)


if secim1 == "left":
    print("hmmmm you chose left. Not bad keep going")
    left_cs = input("You walk and walk, you see special gold spoon, it has an incredible shine, Do you want take? (yes or no)\n")
    left_cs = left_cs.lower()

    if left_cs == "yes":
        print("It's not yours but who cares?")
        spoon_cs = input("You walked very too much and you see big lake and old man,\n old man cannot drink water because his hands are shaking, will you give him your spoon? maybe he may not give it back? (yes or no)\n")
        spoon_cs = spoon_cs.lower()

        if spoon_cs == "yes":
            print("You very good person, this old man nobody but you give gold spoon for nothing,\n I respect you. He wasn't an old man, this was a test and you passed. Old man gives a lot of gold and silver and drinks water together (BEST ENDİNG)")

        elif spoon_cs == "no":
            print("You very thirst drink water bro. But wait")
            print("Old man calling 'Hey help me to drink water please young man'")
            last_cs = input("What will you do, Will you help the old man or drink water yourself?\n (drink or help)")
            last_cs = last_cs.lower()

            if last_cs == "help":
                print("You very good person, this old man nobody but you give gold spoon for nothing,\n I respect you. He wasn't an old man, this was a test and you passed. Old man gives a lot of gold and silver and drinks water together (BEST ENDİNG)")
            elif last_cs == "drink":
                print("You choose drink yourself but you are stupid because this was all a test,\n The old man suddenly disappears and the golden spoon melts in your hand. You have nothing left. Whatever you do now (BAD ENDİNG)")

    elif left_cs == "no":
        print("Never mind, it wasn't yours anyway. Keep walking. You find a temple and you get into it.\n An impossibly large diamond welcomes you.")
        diamond_cs = input("Will you take it? (yes or no)")
        diamond_cs = diamond_cs.lower()

        if diamond_cs == "yes":
            print("The temple suddenly started to collapse! But but calm down you running. You forgot which way you came, that's not good")
            way_cs = input("What will you do? HURRY UP LEFT OR RİGHT")
            way_cs = way_cs.lower()

            if way_cs == "right":
                print("You running right and this way right so you bring the diamond and survived that (GOOD ENDİNG)")
            if way_cs == "left":
                print("You running left and this way right so you bring the diamond and survived that (GOOD ENDİNG)")

        elif diamond_cs == "no":
            print("You're really boring and a coward bro. What is your problem?\n You found golden spoon but you didn't take it, you find diamond but still didn't take ")
            print("So That's why you come home empty handed (BORİNG ENDİNG)")

elif secim1 == "right":
    print("This is not right way (laughing) So you lose")

else:
    print("WTF bro you just choose two option")
    print("Game over congratulations")


