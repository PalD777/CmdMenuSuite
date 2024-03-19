import re
from os import name, system
import sys
import matplotlib.pyplot as plt
import numpy as np

def parse_expr(expr: str):
    '''Evaluates the mathematical expression safely'''
    conv = {
        '\^': '**',
        'cosec\(': '1/degcalc(sin,',
        'sec\(': '1/degcalc(sin,',
        'cot\(': '1/degcalc(sin,',
        'sin\(': 'degcalc(sin,',
        'cos\(': 'degcalc(cos,',
        'tan\(': 'degcalc(tan,',
        'cosecr': '1/sin',
        'secr': '1/sin',
        'cotr': '1/sin',
        'sinr': 'sin',
        'cosr': 'cos',
        'tanr': 'tan',
        '([0-9]+)!': 'factorial(\\1)',
        '([0-9]+)([A-Za-z]+)': '\\1 * \\2'
    }
    # This stores all the functions that are allowed in the string
    ALLOWED_NAMES = {**{
        key: val for key, val in np.__dict__.items() if not key.startswith("__")
    }, **{'degcalc': degcalc, 'x': np.linspace(-500, 500, 10000), 'graph': graph}}
    # This parses the user's input in valid syntax using regex substitution
    for pattern in conv:
        expr = re.sub(pattern, conv[pattern], expr)
    code = compile(expr, "<string>", "eval")
    # If a token that isn't allowed is present, the code isn't evaluated
    for name in code.co_names:
        if name not in ALLOWED_NAMES:
            raise NameError(f"The use of `{name}` is not allowed")
    # Evaluates the code after removing access to builtin functions
    out = eval(code, {"__builtins__": {}}, ALLOWED_NAMES)
    # Rounds floats to prevent floating point errors of small magnitudes
    if isinstance(out, float): out = round(out, 15)
    return out

def degcalc(func, val: float):
    '''Function to run a command after converting a value from degress to radians'''
    return func(np.radians(val))

def graph(y: np.ndarray) -> None:
    '''Function that takes an array of y values and plots them in a graph'''
    plt.plot(np.linspace(-500, 500, 10000), y)
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.grid(alpha=0.4)
    print('Please close the graph window to continue.' )
    plt.show()
    return None 

def clear():
    '''Clears Screen'''
    system('cls') if name == 'nt' else system('clear')

def run():
    '''Connects to program to the main menu and contains the code required to start the script and to explain the user on what to do'''
    clear()
    print('Calculator v1.1.037a')
    print('You can press q to exit')
    print()
    print('You may use trignometric and logarithmic functions by using parenthesis. For example: sin(45) or log(e) or log10(10)')
    print('Trignometric functions default to using degrees. In order to use radians, suffix them with an r. For example: sinr(pi) or cosr(pi/2)')
    print('It also supports common functions and constants like pi, e, floor(x), ceil(x)')
    print()
    print('You can graph functions by giving a function in terms of x as the argument to the graph function. For example: graph(x^2), graph(sin(2x)), graph(log(abs(x)))')
    print()
    while True:
        inp = input('>>> Enter an expression to evaluate: ')
        if inp == 'q' or inp == 'Q':
            clear()
            break
        else:
            try:
                out = parse_expr(inp)
                if out is not None:
                    print(out)
            except Exception as e:
                print(f'Error: {e}')
    system(f'"{sys.executable}" main.py')

if __name__ == '__main__':
    run()