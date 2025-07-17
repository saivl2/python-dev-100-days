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

options = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(options[user_choice])
computer_choice = random.randint(0, len(options) - 1)
print(options[computer_choice])

if user_choice == computer_choice:
    print("Draw!")
elif user_choice == 0:
    if computer_choice == 2:
        print('User Wins!')
    else:
        print("Computer Wins!")
elif user_choice == 2:
    if computer_choice == 1:
        print('User Wins!')
    else:
        print('Computer Wins!')

elif user_choice == 1:
    if computer_choice == 0:
        print('User Wins!')
    else:
        print('Computer Wins!')

