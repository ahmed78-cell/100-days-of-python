print("Welcome to the treasure island\n Your mission is to find the treasure.");
choose1 = input("You are at a cross road. Where do you want to go? Type 'left' or 'right': ")
if choose1.lower() == "left":
    choose2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ")
    if choose2.lower() == "wait":
        choose3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
        if choose3.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif choose3.lower() == "yellow":
            print("You found the treasure! You Win!")
        elif choose3.lower() == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
