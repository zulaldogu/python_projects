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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
road = input("Type Left or Right!\n").lower()

if road == "Right":
    print("Fall into a hole. Game over!")
else:
    print("You have come to a lake. There is an island in the middle of the lake.")
    action = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if action == "swim":
        print("Attacked by a trout. Game over!")
    else:
        print("You have arrived at the island unharmed. There is a house with 3 doors.")
        door = input("One red, one yellow and one blue. Which color fo you choose?\n").lower()
        if door == "red":
            print("Burned by fire. Game over!")
        elif door == "blue":
            print("Eaten by beasts. Game over!")
        elif door == "yellow":
            print("You win!!! Congratulations!")
        else:
            print("You chose a door that doesnt exists. Game over!")
