import curses
from pathlib import Path
from importlib import import_module

class App:

    def __init__(self, stdscr):
        '''Initialises the screen with basic settings and gets all the Scripts to be shown in the menu'''
        self.stdscr = stdscr
        # Get component scripts for menu option
        blacklist = ('__init__', 'CONFIG_DEF')
        self.options = [file.stem for file in Path(r'.\Scripts').glob('*.py') if file.stem not in blacklist]
        self.selected = 0
        self.stdscr.bkgdset(' ', curses.color_pair(0))
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.curs_set(0) # Make cursor invisible
        self.stdscr.erase()
        self.print_menu()
    
    def print_menu(self):
        """Prints the Menu"""        
        self.stdscr.erase()
        self.draw_box()
        self.centerstr(0, ' MENU ')
        for i, option in enumerate(self.options):
            x = self.centerstr(i + 3, option)
        self.stdscr.addstr(curses.LINES - 2, 2, 'Press q to exit')
        self.event_loop()

    def event_loop(self):
        '''Detects user inputs like screen resize or arrow keys or q or enter'''
        while True:
            self.update_marker()
            # refreshing the screen ensures that the screen always shows the updates options
            self.stdscr.refresh()
            key = self.stdscr.getch()
            if key == ord('q') or key == ord('Q'):
                break
            elif key == curses.KEY_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif key == curses.KEY_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif key == curses.KEY_RESIZE:
                curses.update_lines_cols()
                # Checks if the windows size is below minimum and resizes it to fit content
                if curses.LINES < len(self.options) + 6 or curses.COLS < len(max(self.options, key=len)) + 10:
                    rows = curses.LINES if curses.LINES > len(self.options) + 6 else len(self.options) + 6
                    cols = curses.COLS if curses.COLS > len(max(self.options, key=len)) + 10 else len(max(self.options, key=len)) + 10
                    print(cols, curses.COLS, len(max(self.options, key=len)) + 8)
                    curses.resize_term(rows, cols)
                return self.print_menu()
            elif key == 10 or key == curses.KEY_ENTER:
                self.choice = import_module(f'Scripts.{self.options[self.selected]}')
                break

    def update_marker(self):
        '''To update the position of the arrow which shows the currently selected option'''
        for i, option in enumerate(self.options):
            x = curses.COLS // 2 - len(option) // 2
            # i + 3 is the row of an option. The arrow is added 2 characters behind the start of the option
            self.stdscr.addstr(i + 3, x - 2, ' ' if i != self.selected else '→', curses.color_pair(1))

    def draw_box(self):
        '''Helper function to draw a box around the screen based on the current screen size'''
        self.stdscr.addstr(0, 0, '╔' + '═'*(curses.COLS-2) + '╗')
        for y in range(1, curses.LINES-1):
            self.stdscr.addstr(y, 0, '║')
            self.stdscr.addstr(y, curses.COLS - 1, '║')
        try:
            self.stdscr.addstr(curses.LINES - 1, 0, '╚' + '═'*(curses.COLS-2) + '╝')
        except:
            # An exception is triggered when the bottom right corner is filled as the cursor has no space to move to the right.
            # This line makes python ignore it as the position of the cursor isnt vital for the code
            pass

    def centerstr(self, y: int, text: str, color=None):
        '''Helper function that adds a string at the center of the screen at a given row'''
        x = curses.COLS // 2 - len(text) // 2
        if color is None:
            self.stdscr.addstr(y, x, text)
        else:
            self.stdscr.addstr(y, x, text, color)


if __name__ == '__main__':
    # curses.wrapper modifies basic settings to allow us to use the menu by turning cbreak and echo off
    app = curses.wrapper(App)
    # Once the event loop breaks, it checks if an option was selected and runs it
    if hasattr(app, 'choice'):
        app.choice.run()