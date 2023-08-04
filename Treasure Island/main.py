# Your mission is to find the treasure.
# You're at a cross road. Where do you want to go? Type "left" or "right"
# You come to a lake. There is an Island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim.
# You arrive at the Island unharmed. There is a house with 3 doors. One red , one yellow and one blue. Which colour do
# you choose?
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
stage1 = input("You're at a cross road. Where do you want to go? left or right\n").lower()
if stage1 == "left":
    stage2 = input('You come to a lake. Type "wait" to wait for a boat or Type "swim" to swim\n').lower()
    if stage2 == "wait":
        stage3 = input("You arrive at the Island unharmed. There is a house with 3 doors. One red, one yellow and one"
                       " blue. Which colour do you choose?\n").lower()
        if stage3 == "yellow":
            print("You Win!!")
        elif stage3 == "blue":
            print("Game Over. Demon ate you!!")
        else:
            print("Game Over. Witch ate you!!")
    else:
        print("Game Over. Crocodile ate you!!")
else:
    print("Game Over. You fell into a hole!!")
