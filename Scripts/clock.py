from os import name, system
from pathlib import Path
import sys
import datetime
import time
from getpass import getpass
from threading import Thread, current_thread

def prompt(*choices) -> int:
    print('Select an option by entering its corresponding number')
    for i, choice in enumerate(choices): # enumerate helps to give the choice and the corresponding number
        print(f'[{i+1}] {choice}') # prints the choice and their corresponding number
    print()
    while True:
        selection = input('>>> Select a number: ') # asks the user to select the number choices given
        if selection.isnumeric() and 0 < int(selection) <= len(choices): # checks if the prompt is a number
            selection = int(selection) # converts it to an integer
            break
        print('[!] Please enter a valid number') # if the above if condition returns False, then it would print this statement
    return selection - 1 # subtarcts (-1) as the option numbers 1,2,3 instead 0,1,2

def stopwatch():
    print('''Commands:
    [*] P - Pause the timer
    [*] U - Unpause the timer
    [*] <Enter> - Start/Stop the timer
    ''')
    getpass('Press enter to start your stopwatch...') # tells the user to press enter to start the stopwatch
    start_time = datetime.datetime.now() # start_time holds the current time ie the time where the statement holds true
    paused = False 
    while True:
        cmd = getpass("Enter a command and press enter...").lower().strip()[0:1] # asks the user to click any of the commands given above
        if cmd == 'p': # if the user chooses to pause the time and clicks p
            paused_time = datetime.datetime.now() # paused_time holds the current time ie the time where this statement holds true
            paused = True
            print('[*] Stopwatch has been paused') # shows this message
        elif cmd == 'u': # if the user unpases the time
            if paused == True: # checks if the stopwatch has been paused once
                start_time += (datetime.datetime.now() - paused_time) # calculates and assigns start_time to the time that had been paused 
                paused = False
                print('[*] Stopwatch has been unpaused')
            else: # if the stopwatch has not been paused before
                print("[!] You must pause the timer before you can unpause it.")
        elif cmd == '': # if the user clicks enter
            end_time = datetime.datetime.now() # end_time has the time where this statement holds True
            break
        else: # if the user enters an invalid command
            print('[*] Unknown command')
    if paused:
        new_time = paused_time - start_time
    else:
        new_time = end_time - start_time # subtracts the final time from the initial time  
    print()
    print(new_time) # prints the time
    print()

def clock():
    t = current_thread() # allows init_clock to run simultaneously with this function
    while t.alive: # this will be True as we assigned it to init_clock
        now = datetime.datetime.now() # now variable holds the current time 
        system('cls') if name == 'nt' else system('clear') # it clears the screen every second so that the the previous print statements wont be printed and updates the time
        print(now.strftime("%d/%m/%Y, %H:%M:%S")) # this formats the clock in days/months/years hours/minutes/seconds
        print('\nPress enter to return to the option selection screen...') # asks the user to press enter to go back to the selection screen
        time.sleep(1) # updates time every second

def init_clock():
    t = Thread(target=clock, name='Time') # thread allows both the clock and init_clock function to run simultaneously
    t.daemon = True
    t.alive = True
    t.start() # starts the thread
    getpass() # calls the getpass function
    t.alive = False
    t.join() # waits for the clock function to get over
    cls()

def cls():
    system('cls') if name == 'nt' else system('clear') # clears the screen

def run():
    cls()
    while True:
        option = prompt('Clock', 'Stopwatch', 'Quit') # calls the prompt function
        if option == 0:
            init_clock() # calls the clock function
        elif option == 1:
            cls()
            stopwatch() # calls the stopwatch function
        else:
            system(f'"{sys.executable}" main.py') # it would quit the program and goes back to the menu
            break

if __name__ == '__main__':
    run()
