import requests
import json
from os import name, system
import sys
from .CONFIG_DEF import CONFIG

def define(word: str) -> str:
    '''
    Defines a word after retrieving data from oxford.
    Please keep in mind that the oxford's free api plan only allows 1000 requests per month and is rate-limited
    '''

    url = f'https://od-api.oxforddictionaries.com:443/api/v2/entries/en/{word.lower()}?fields=definitions,etymologies,examples&strictMatch=false'
    r = requests.get(url, headers = {'app_id' : CONFIG.app_id, 'app_key' : CONFIG.app_key})   
    result = json.loads(r.text)
    if 'results' in result:
        data = result['results'][0]['lexicalEntries']
        out = f'\n{result["id"]}\n\n'                       # Name of the word retrieved
        # Gets all the Etymologies
        if 'etymologies' in data[0]['entries'][0]:
            out += '[*] Etymology: \n'
            for i, etymo in enumerate(data[0]['entries'][0]['etymologies']):
                out += f'       {i+1}. {etymo}\n'
            out += '\n'
        # Gets all the definitions and examples
        for info in data:
            out += f"[*] {info['lexicalCategory']['text']}\n"   # The part of speech the definition is for
            if 'entries'in info:
                defs = info['entries'][0]['senses'][0]
                if 'definitions' in defs:
                    for i, _def in enumerate(defs['definitions']):
                        out += f'       {i+1}. {_def}\n'
                if 'examples' in defs:
                    out += f'\n -> Examples: \n'
                    for i, examp in enumerate(defs['examples']):
                        out +=  f"      {i+1}. {examp['text']}\n"
                    out += '\n'
    else:
        out = 'No Results'
    return out

def run():
    '''Connects to program to the main menu and contains the code required to start the script and to explain the user on what to do'''
    system('cls') if name == 'nt' else system('clear')
    while True:
        inp = input('>>> Please enter a word to find the definition of [Press enter without typing anything to quit]: ')
        if inp == '': break
        print(define(inp))
    system(f'"{sys.executable}" main.py')

if __name__ == '__main__':
    run()