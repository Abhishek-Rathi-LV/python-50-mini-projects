import random 
number=random.randint(1,100)
count=0
while True :
    a=int(input("Guess the number (1-100):-"))
    count+=1
    if a==number:
        print("🎉 Correct! You guessed it in ",count," attempts.")
        break
    elif a>number:
        print("Too High!")
    else:
        print("Too Low!")