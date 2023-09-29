import random

Number1 = random.randint(1, 10)
Number2 = random.randint(1, 10)

correct = (Number1 + Number2)

answer = input("What is "+str(Number1)+" + "+str(Number2)+' ?'" \nEnter the answer: ")

if answer == str(correct):
    print("Correct answer!")
else:
    print("Nope! The answer was "+str(correct))