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

#Write your code below this line 👇
import random
user_choice = input("what do you choose? 0 for rock ,1 for paper or 2 for scissors \n")
if user_choice  >= 3 or user_choice == <0:
     print("You typed an invalid number, you lose!")
else:
  print(game_images[user_choice])
  
  computer_choice = random.randint(0,2)
  print("computer_choice:")
  print(game_images[computer_choice])
  
  game_images = [rock , papers , scissors]
  print(game_images[user_choice])
  
  
  if user_choice == 0 and computer_choice == 2
     print("you win")
  elif computer_choice == 0 and user_choice == 2
     print("you lose")
  elif computer_choice > user_choice :
     print("you lose")
  elif user_choice > computer_choice:
     print("you win")
  elif computer_choice == user_choice :
  print("Its a draw")
  
 