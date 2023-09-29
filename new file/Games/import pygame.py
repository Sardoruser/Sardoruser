import pygame
import random 

pygame.init()

height, width = 800, 600 
window = pygame.display.set_mode((height, width))
pygame.display.set_caption("Snake and Ladders")

final = 100

player1 = input("Player 1 enter your name: ")
player2 = input("Player 2 enter your name: ")

        
def roll_dice():
    return random.randint(0, 6)
def update_position(current_position, dice_result):
    new_position = current_position + dice_result
    
    if new_position > final:
        return current_position
    
    #define snakes and ladders positions
    snakes = {16: 6, 47: 26, 49:11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80:100}
    
    if new_position in snakes:
        new_position = snakes[new_position]
    elif new_position in ladders: 
        new_position = ladders[new_position]
        
    return new_position

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Roll the dice for player 1 
        input("Player 1 - Press Enter to roll the dice")
        dice1 = roll_dice()
        print(player1 + " rolled a " + str(dice1))
        position1 = update_position(position1, dice1)
        print(player1 + " is at position " + str(position1))
        
        # check if player1 wins
        if position1 == final:
            print(player1 + "wins!")
            break
        
        
        # Roll the dice for player 2 
        input("Player 2 - Press Enter to roll the dice")
        dice2 = roll_dice()
        print(player2 + " rolled a " + str(dice2))
        position2 = update_position(position1, dice2)
        print(player2 + " is at position " + str(position1))
        
        # check if player2 wins
        if position2 == final:
            print(player2 + "wins!")
            break
        
        