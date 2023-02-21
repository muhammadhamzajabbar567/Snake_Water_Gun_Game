print(
    ""
    " Snake, Water and Gun is a variation of the children's game rock-paper-scissors where players use hand gestures to represent \n"
    "a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water \n")


import random

def check(comp, user):
    if comp == user:
        return 0
    elif (comp == 0 and user == 1):
        return -1
    elif (comp == 1 and user ==  2):
        return -1
    else:
        (comp == 2 and user == 0)
        return -1
    return 1


comp = random.randint(0,2)
user = (int(input("Select! O For Snake, 1 For water, and 2 For Gun: \n")))

score = check(comp, user)
print("You: ", user)
print("Computer: ", comp)

if (score == 0):
    print("Match Draw")
elif (score == -1):
    print("You Lose")
else:
    print("You Won")