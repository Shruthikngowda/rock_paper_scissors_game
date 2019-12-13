import random
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
computer_input_list = [ROCK, PAPER, SCISSORS]
computer_input = random.choice(computer_input_list)
#print(computer_input)
comp = ""
if(computer_input == ROCK):
  comp = 1;
elif(computer_input == SCISSORS):
  comp = 2
else:
  comp = 3
user_input = input("Enter your choice - rock, paper, scissors : ")
user_choice = ""
if(user_input == ROCK):
  user_choice = 1
elif(user_input == SCISSORS):
  user_choice = 2
else:
  user_choice = 3
#print(user_input)
print("Your opponent opted : ", computer_input)
if(comp == user_choice):
  print("its a tie")
elif(comp == 1 and user_choice == 2):
  print("Sorry , you loose")
elif(comp == 2 and user_choice == 3):
  print("Sorry , you loose")
elif(comp == 3 and user_choice == 1):
  print("Sorry , you loose")
else:
  print("You won")
