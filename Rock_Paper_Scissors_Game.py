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
list= [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(f"User choose: {user}")
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
else:
    print(scissors)

computer = random.randint(0,2)
print(f"Computer choose: {computer}")
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

if (computer == 0 and user == 0) or (computer == 1 and user == 1) or (computer == 2 and user == 2):
    print("DRAW!")
elif (user == 0 and computer == 1) or (user == 1 and computer == 2) or (user == 2 and computer == 0):
    print("YOU LOSE!")
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print("YOU WIN!")
