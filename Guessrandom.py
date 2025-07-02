import random

number=random.randint(1,100)

while(True):
    guess=int(input("Enter your Guess"))
    if guess>number:
        print("YOUR GUESS IS HIGHER, TRY LOWER")
    elif guess<number:
        print("YOUR GUESS IS LOWER, TRY HIGHER")
    elif guess==number:
        print("CONGRATS YOU WON !!!🙌🥳👾")
        break