import random

computer_input_list = ["rock", "paper", "scissors"]
computer_input = random.choice(computer_input_list)
print(computer_input)

user_input = input("Enter your choice - rock, paper, scissors : ")
print(user_input)
if(computer_input == user_input):
  print("its a tie")
elif