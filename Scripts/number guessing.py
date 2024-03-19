import random
from os import name, system
from pathlib import Path
import sys

def intput(prompt: str = '') -> int: 
    while True: 
        x = input(prompt) #validates what the user inputs 
        if x.isnumeric(): #checks if the prompt is a number
            return int(x) #converts it to an integer
        print('[!] Please enter a valid integer') #if not, it prints this

def main():
    ranmin = intput('Enter the minimuim number: ') #asks for the minimuim range for the secret number
    ranmax = intput('Enter the maximuim number: ') #asks for the maximuim range for the secret number
    x = random.randint(ranmin,ranmax) #x has any value from the minimuim value and maximuim value inputted by the user
    while True:
      n = intput("Guess the number: ") #asks the user to guess the number
      if n > x: #if the number inputted is more than the secret number
        print('The number is too high. Please try again')
      elif n < x: #if the number inputted is less than the secret number
        print('The number is too low. Please try again.')
      else: #if the person guessed the secret number correctly
        print('Congrats! You have gueesed the right number.')
        break
    c = input('>>> Do you want to continue playing? [Yes/No] ').strip().lower()[0] #asks the user if he/she wants to continue playing
    if c == 'y': #if she answers 'y' as per the given prompt
        main() #the main function is called causing the user to start the game all over again

def run():
    system('cls') if name == 'nt' else system('clear') #clears the system
    main() #calls the function main
    system(f'"{sys.executable}" main.py') #goes back to the menu

if __name__ == '__main__':
    run()
