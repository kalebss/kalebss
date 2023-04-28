
# a game of rock paper scissors

import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

img = [rock, paper, scissors]



user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
# assign the image list to the index of options

if user_choice > 2 or user_choice < 0:
    print("invalid number, you lose!")
else:
    print(img[user_choice]) 

    # computer choice
    comp_choice = random.randint(0,2) # range
    print("computer chose")
    print(img[comp_choice])


    if user_choice == 0 and comp_choice == 2:
        print("user wins!")
    elif comp_choice == 0 and user_choice == 2:
        print("computer wins!")
    elif comp_choice > user_choice:
        print("computer wins!")
    elif user_choice > comp_choice:
        print("user wins!")
    elif comp_choice == user_choice:
        print("draw")

