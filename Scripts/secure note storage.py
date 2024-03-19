import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import json
from os import name, system
import sys
from getpass import getpass

class LockerSession:
    data_loaded = False
    data = {}

    def __init__(self):
        '''Loads data if it isn't loaded yet and starts the login/registration process'''
        if not LockerSession.data_loaded:
            LockerSession.load_data()
        choice = self.prompt('Login', 'Register', 'Quit')
        self.user = self.parse_login_choice(choice)

    def make_note(self):
        '''Encrpyts the user's'''
        content = input(">>> Enter the note's content that you would like to store: ")
        LockerSession.data[self.user].append(self.sym_enc.encrypt(content.encode('latin-1')).decode('latin-1'))

    def read_notes(self):
        '''Gets all the notes of the current user and decrypts and prints them'''
        num_notes = len(LockerSession.data[self.user][1:])
        if num_notes == 0: print('[*] No notes found.\n')
        for i, enc_note in enumerate(LockerSession.data[self.user][1:]):
            print(f'[*] Note {i+1} out of {num_notes}')
            print(self.sym_enc.decrypt(enc_note.encode('latin-1')).decode('latin-1'))
            print()
      
    def prompt(self, *choices) -> int:
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
        
    def parse_login_choice(self, choice: int):
        '''Handles Login or Registration of the user'''
        cls()
        if choice == 0:
            name = input('>>> Username: ')
            pw = getpass('>>> Password: ')
            # Compares the blake2b hash of the password to the one stored under that username in the db
            if name in LockerSession.data and LockerSession.data[name][0] == LockerSession.blake(pw):
                cls()
                print('[*] You are now successfully logged in\n')
                # Initialises the Key derivation function parameters
                kdf = PBKDF2HMAC(
                    algorithm = hashes.SHA256(),
                    length = 32,
                    salt = b'\x11\x03\x71\x41' * 4,
                    iterations = 10000,
                )
                # Generates a b64 key of the password using kdf and stores the Fernet encrpytion base with that key
                key = base64.urlsafe_b64encode(kdf.derive(pw.encode('latin-1')))
                self.sym_enc = Fernet(key)
                del pw
                return name
            else:
                print('\n[*] Invalid Credentials\n')
                if self.prompt('Retry', 'Choose another option'):
                    cls()
                    choice = self.prompt('Login', 'Register', 'Quit')
                return self.parse_login_choice(choice)
        elif choice == 1:
            name = input('>>> Username: ')
            pw = getpass('>>> Password: ')
            if name not in LockerSession.data:
                # Stores the blake2b hash of the user password in the data
                LockerSession.data[name] = [LockerSession.blake(pw)]
                cls()
                print('[*] Successfully Registered\n')
                # Initialises the Key derivation function parameters
                kdf = PBKDF2HMAC(
                    algorithm = hashes.SHA256(),
                    length = 32,
                    salt = b'\x11\x03\x71\x41' * 4,
                    iterations = 10000,
                )
                # Generates a b64 key of the password using kdf and stores the Fernet encrpytion base with that key
                key = base64.urlsafe_b64encode(kdf.derive(pw.encode('latin-1')))
                self.sym_enc = Fernet(key)
                del pw
                return name
            else:
                print('\n[*] That username is already taken\n')
                if self.prompt('Retry', 'Choose another option'):
                    cls()
                    choice = self.prompt('Login', 'Register', 'Quit')
                return self.parse_login_choice(choice)
        else:
            leave()

    @staticmethod
    def blake(msg: str) -> str:
        '''Gets the blake2b hash of a string'''
        digest = hashes.Hash(hashes.BLAKE2b(64))
        digest.update(msg.encode('latin-1'))
        return digest.finalize().decode('latin-1')

    @staticmethod
    def load_data():
        '''Loads Data from the JSON if it exists'''
        try:
            with open('locker_data.json', 'r') as f:
                LockerSession.data = json.load(f)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            print("[!] Save file was found to be corrupt. Proceeding further will risk in data overide\n")

def leave(session = None):
    '''Saves all the data and returns to the menu'''
    with open('locker_data.json', 'w') as f:
        json.dump(LockerSession.data, f)
    del session
    raise SystemExit

def cls():
    system('cls') if name == 'nt' else system('clear')

def run():
    '''Connects to program to the main menu and contains the code required to start the script and to explain the user on what to do'''
    cls()
    try:
        session = LockerSession()
        while True:
            choice = session.prompt('Make Note', 'Read Notes', 'Quit and Save Notes')
            cls()
            if choice == 0:
                session.make_note()
                cls()
                print('[*] Note successfully made!\n')
            elif choice == 1:
                session.read_notes()
            else:
                leave(session)
    except SystemExit:
        system(f'"{sys.executable}" main.py')

if __name__ == '__main__':
    run()