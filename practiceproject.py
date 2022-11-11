import random
from secrets import choice
user_input=input("enter input(rock,paper,scissors")
possible_action=["rock","paper","scissors"]
computer_action=random.choice(possible_action)
print(f"you chose {user_input} and computer chose{computer_action}")
if computer_action==user_input:
    print("tie")
elif user_input=="rock":
    if computer_action=="scissor":
         print("you win")
    else:
        print("you lose")
elif user_input=="paper":
   if  computer_action=="scissors":
         print("you lose")
   else:
        print("you win ")
elif user_input=="scissor":
    if computer_action=="paper":
        print("you win")
    else:
        print("you lose")
