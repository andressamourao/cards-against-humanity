# Game: Cards Against Humanities 
# Program to read a random question or phrase from a 
# file and print the game card with the user's response

import random

# Open the Cards Against text file
open_file = open('cards.txt', 'r')

# Read the whole file and store each line in a list
card_lst = open_file.read().splitlines()

# Choose a random line from the list
phrase = random.choice(card_lst)

# Program to pick 3 random answers from a 
# file and print, show to the user so they can chose one among them

# Open, read the file and create a list 
fileanswer = open('answers.txt', 'r')
answer_lst = fileanswer.read().splitlines()

# Store in a list 3 answers 

cards3 = random.sample(answer_lst, 3)

# Display to the user 
chosencard = input(f'For the phrase "{phrase}", \n Which one do you prefer: 1, 2 or 3? \n{cards3}: ')
if chosencard == '1':
    card = phrase.replace('________', cards3[0])
    print(card)
if chosencard == '2':
    card = phrase.replace('________', cards3[1])
    print(card)
if chosencard == '3':
    card = phrase.replace('________', cards3[2])
    print(card)
