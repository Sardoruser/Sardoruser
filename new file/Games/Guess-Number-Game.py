import random
import time

Tries = 0

name = input(("Hello, Welcome to the 'Guess Number Game' \nTo start the game Enter your name here : "))
number = random.randint(1, 50)
time.sleep(2)
print("\nHi, " + name + "!, I am thinking of a number between 1 and 50.\n")
time.sleep(2)
print("You have six tries to find my guess number.")
while Tries < 6:
    try:
        guess = int(input("Take a guess: "))  
        Tries = Tries + 1
########################################################################
        if guess < number:
            if number - guess <= 3:
                print("Your guess is a little bit lower.;)")    
            elif number - guess <= 5:
                print("your guess is low.")
            else:
                print("Your guess is too low.")
                
        if guess > number:  
            if guess - number <= 3:
                print("Your guess is a little bit higher.;)")  
            elif guess - number <= 5:
                print("your guess is high.")
            else:
                print("Your guess is too high.")
#In here You can know the your guessed number higher or lower to a random chose number
 
        if guess == number:
            break      
    except TypeError and ValueError: # Here you can handle errors 
        print("Please enter number!:(")

if guess == number:#Here if you guessed number less than 6 tries it will print 'Well done...'
    Tries = str(Tries)
    print('Well Done, ' + name + '! You guessed my number in ' + Tries + ' guesses! :-D')
if guess != number:# Here if you guessed number more than 6 tries it will print 'Nope...' 
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
    