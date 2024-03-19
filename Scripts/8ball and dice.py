import random
from os import name, system
from pathlib import Path
import sys

l1 = ["It is certain.","It is decidedly so.","Without a doubt.","Yes – definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]

def prompt(*choices):
    print('Select an option by entering its corresponding number') 
    for i, choice in enumerate(choices): # enumerate helps the choices and the corresponding number
        print(f'[{i+1}] {choice}') # prints the choices and the corresponding numbers
    print()
    while True:
        selection = input('>>> Select a number: ') # asks the user to select a number
        if selection.isnumeric() and 0 < int(selection) <= len(choices): # checks if the number is alpha numberic or if the length is valid
            selection = int(selection) # converts the string to an int
            break
        print('[!] Please enter a valid number') # if the condition is not satisfied, then it gives this message
    return selection - 1 # subtarcts (-1) as the option numbers 1,2,3 instead 0,1,2

def _8ball():
    arg = input('>>> Enter a Yes or No question: ') # asks the user to enter a question
    print('[*] Outcome:', random.choice(l1)) # from list l1 it chooses a random element and prints the output
    c = input('>>> Do you want to continue? [Yes/No] ').strip().lower()[0] # asks the user to continue playing
    if c == 'y': # if the user says y, then the function is 8ball is called and the game continues
        _8ball() # calls the 8ball function and starts the game again

def dice():
    while True:
        sides = input('>>> Enter the sides of the dice: ') 
        if sides.isdigit() and int(sides) > 0: # it verifies whether the sides entered is a digit and greater than 0
            sides = int(sides) # converting the string to an integer
            break
        print('[!] Please enter a valid number of sides')
    dice = random.randint(1, sides) # will choose a number b/w 1 and value inputted in the variable sides
    print(f'\n[*] You rolled {dice}!\n') # prints the number that is in the variable dice randomly

def run():
    system('cls') if name == 'nt' else system('clear') # clears screen
    while True:
        opt = prompt('Roll a die', 'Ask a question to the 8ball', 'Quit') # Calls the prompt function
        print()
        if opt == 0: # if the user enters 0 then it goes to the function dice
            dice()
        elif opt == 1: # if the user chooses 1 then it to to 8ball function
            _8ball()
        else: # if the user enters anything else
            system(f'"{sys.executable}" main.py') # it goes to the main.py (menu) and goes out of the while loop
            break 

if __name__ == '__main__':
    run()