import random
import time

def displayIntro():
    print("You are in a land full of dragons.")
    print(" In front of you, you see two caves.")
    time.sleep(3)
    print(" In one cave, the dragon is friendly and will share his treasure with you.")
    time.sleep(3)
    print(" The other dragon is greedy and hungry, and will eat you on sight.")
    time.sleep(3)
    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print("Which cave do you want to ENTER (1 or 2)?: ")
        cave = input()
        
    return cave

def checkCave(chosenCave):
    print("You approuch to the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)
    
    friendlyCave = random.randint(1, 2)
    
    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain.lower() == 'yes' or playAgain.lower() == 'y':
    
    displayIntro()
    
    caveNumber = chooseCave()
    
    checkCave(caveNumber)
    
    playAgain = input('Do You Want to Play Again? (yes/no): ')
   