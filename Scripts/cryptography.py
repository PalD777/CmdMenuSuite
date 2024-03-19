import base64
import os
import sys
from getpass import getpass

class Crypto:
    ciphers = {}

    def __init__(self, data: str, key = None):
        '''Base Init Class for all the ciphers'''
        self.data = data
        self.key = key
        self.alpha = 'abcdefghijklmnopqrstuvwxyz'

class Caesar(Crypto):
    def encrypt(self) -> str:
        result = ""
        # Check if the key is valid and convert it to int
        if self.key.isdigit() or (self.key[0] == '-' and self.key[1:].isdigit()):
            key = int(self.key)
        else:
            raise ValueError
        # Performs Caesar Shift
        for char in self.data:
            if char.isupper():
                i = (self.alpha.index(char.lower()) + key) % 26
                result += self.alpha[i].upper()
            elif char.islower():
                i = (self.alpha.index(char) + key) % 26
                result += self.alpha[i]
            else:
                result += char
        return result
  
    def decrypt(self) -> str:
        '''Calls encrypt with the additive inverse of the key to shift in the opposite direction'''
        self.key = '-' + self.key if self.key[0] != '-' else self.key[1:]
        res = self.encrypt()
        self.key = self.key[1:] if self.key[0] != '-' else '-' + self.key
        return res

class Vigenere(Crypto):
    def encrypt(self, parity: int = 1) -> str:
        result = ""
        # Checks if the key is alphabetical
        if not self.key.isalpha():
            raise ValueError
        # Combines the index of the key and text to obtain a new encrypted index.
        # This implementation doesn't modify non-alphabetical characters but still counts them for progressing the key
        for index, char in enumerate(self.data):
            if char.isupper():
                i = self.alpha.index(char.lower())
                j = self.alpha.index(self.key[index % len(self.key)].lower()) * parity
                result += self.alpha[(i + j) % 26].upper()
            elif char.islower():
                i = self.alpha.index(char.lower())
                j = self.alpha.index(self.key[index % len(self.key)].lower()) * parity
                result += self.alpha[(i + j) % 26]
            else:
                result += char
        return result

    def decrypt(self) -> str:
        '''Calls encryption but makes it subtract the key instead of add'''
        return self.encrypt(-1)

class A1Z26(Crypto):
    def encrypt(self):
        result = ''
        for index, char in enumerate(self.data):
            if char.isalpha():
                result += f'{self.alpha.index(char.lower()) + 1}, '
            else:
                result += f'({char}), '
        return result[:-2]
    def decrypt(self):
        data = self.data.split(', ')
        result = ''
        for entry in data:
            if entry.isdigit():
                result += self.alpha[(int(entry) - 1) % 26]
            elif entry[0] == '(' and entry[-1] == ')':
                result += entry[1:-1]
            else:
                raise ValueError
        return result

class Base64(Crypto):
    def encrypt(self) -> str:
        return base64.b64encode(self.data.encode()).decode()
    def decrypt(self) -> str:
        return base64.b64decode(self.data.encode()).decode()

class Base32(Crypto):
    def encrypt(self) -> str:
        return base64.b32encode(self.data.encode()).decode()
    def decrypt(self) -> str:
        return base64.b32decode(self.data.encode()).decode()

class Base16(Crypto):
    def encrypt(self) -> str:
        return base64.b16encode(self.data.encode()).decode()
    def decrypt(self) -> str:
        return base64.b16decode(self.data.encode()).decode()

class Base85(Crypto):
    def encrypt(self) -> str:
        return base64.b85encode(self.data.encode()).decode()
    def decrypt(self) -> str:
        return base64.b85decode(self.data.encode()).decode()

def prompt(*choices) -> int:
    '''Function that gets a users choice from a list of options'''
    print('Select an option by entering its corresponding number')
    for i, choice in enumerate(choices):
        print(f'[{i+1}] {choice}')
    print()
    while True:
        selection = input('>>> Select a number: ')
        if selection.isnumeric() and 0 < int(selection) <= len(choices):
            selection = int(selection)
            break
        print('[!] Please enter a valid number')
    return selection - 1

def cls():
    '''Function to clear screen'''
    os.system('cls') if os.name == 'nt' else os.system('clear')

def leave(*args):
    '''Function to return to the main menu'''
    os.system(f'"{sys.executable}" main.py')
    raise SystemExit

def run():
    '''Connects to program to the main menu and contains the code required to start the script and to explain the user on what to do'''
    blacklist = ['Crypto', 'Path']
    for name, obj in globals().items():
        if isinstance(obj, type) and name not in blacklist:
            Crypto.ciphers[name] = obj
    Crypto.ciphers['Quit'] = leave
    while True:
        cls()
        data = input('>>> Enter the data to use the cipher on: ')
        key = input(">>> Enter the key [if the cipher doesn't require a key, you can press enter without entering anything]: ")
        print()
        cipher = list(Crypto.ciphers.values())[prompt(*Crypto.ciphers)](data, key)
        print()
        mode = prompt('Encrypt', 'Decrypt')
        print()
        try:
            if not mode:
                print('[*] Your result is:\n' + cipher.encrypt())
            else:
                print('[*] Your result is:\n' + cipher.decrypt())
            getpass('\nPress enter to continue...')
        except ValueError:
            print('[!] Please check whether the given key and data are valid for the selected cipher')
            getpass('\nPress enter to continue...')
        except SystemExit:
            break

if __name__ == '__main__':
    run()

