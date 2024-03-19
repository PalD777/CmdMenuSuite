from os import name, system
import getpass
import sys

# Utility Functions
def clrScr():
    system('cls') if name == 'nt' else system('clear')

class Board:
    def __init__(self):
        self.state = {
            '7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' 
            }
        self.turn = 'X'

    def checkWin(self) -> bool:
        lines = (
            '123', '456', '789',
            '147', '258', '369',
            '159', '357'
        )
        for line in lines:
            if self.state[line[0]] == self.state[line[1]] == self.state[line[2]]: 
                if self.state[line[0]] != ' ': return True
        return False
        
    def printBoard(self):
        """Prints the entire board as per order and prints the corresponding value (X/O) on the side of the lines drawn"""
        print(self.state['1'] + '|' + self.state['2'] + '|' + self.state['3'])
        print('-+-+-')
        print(self.state['4'] + '|' + self.state['5'] + '|' + self.state['6'])
        print('-+-+-')
        print(self.state['7'] + '|' + self.state['8'] + '|' + self.state['9'])

    def play(self):
        for count in range(9):
            clrScr()
            self.printBoard()
            print(f"\n[*] It's your turn, {self.turn}. Which place would you like to play? [Choose from 1 to 9]") 
            while True:
                move = input()
                if move.isdigit() and 0 < int(move) < 10: # input validation
                    if self.state[move] == ' ': break
                    else: print("[!] That place is already filled. Please try another space.")
                else: print('[!] Please input a valid move')

            self.state[move] = self.turn
            if count >= 4: 
                if self.checkWin():
                    clrScr()
                    self.printBoard()
                    print("\n-- Game Over --\n")                
                    print(f"**** {self.turn} won in {count + 1} turns ****")                
                    return
            # If neither X nor O wins and the board is full, the result is a 'tie'.
            if count == 8:
                print("\n-- Game Over --\n")                 
                print("* It's a Tie! *")
                return

            # Change the player
            self.turn = "O" if self.turn == "X" else "X"

def main():
    clrScr()
    print("Tic Tac Toe\n")
    print("You may enter a number from 1 - 9 in order to fill the corresponding slot. The slots are numbered left to right, from top to bottom\n")
    getpass.getpass("Press any key to continue.")
    while True:
        game = Board()
        game.play()
        # Asks if player wants to restart the game or not.
        restart = input("Do you wish to play again? (Y/N) ").strip().lower()[0]
        if restart != "y": break
    system(f'"{sys.executable}" main.py')

if __name__ == '__main__':
    main()
