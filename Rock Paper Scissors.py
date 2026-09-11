import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
i=input("Enter your choice (rock/paper/scissors):- ")
if(i !="rock" and i !="paper" and  i!="scissors"  ):
    print("Invalid Input")
elif (i==computer):
    print("Draw!")
elif (i == "rock" and computer == "scissors")or (i == "paper" and computer == "rock") or (i == "scissors" and computer == "paper"):
    print("You Win!")
else:
    print("You Lost ! ")

