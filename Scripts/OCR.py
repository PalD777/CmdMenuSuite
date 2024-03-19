import pytesseract
import cv2
import numpy as np
import os
import sys


def main(path: str, mode: str = '000'):
    '''Adds preprocessing filters to image and scan it for text'''
    # Generate a grey scale image
    im = cv2.imread(path)
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Add filters
    if mode[0] == '0':
        _, grey = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    else:
        grey = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    if mode[1] == '0': 
        grey = cv2.medianBlur(grey, 3)
    else:
        grey = cv2.GaussianBlur(grey, (5,5), 0)
    if mode[2] == '1':
        kernel_1 = np.ones((3, 3), np.uint8)
        kernel_2 = np.ones((1, 1), np.uint8)
        grey = cv2.erode(grey, kernel_1)
        grey = cv2.dilate(grey, kernel_2)
    cv2.imwrite('_temp.png', grey)
    # Scan Image with prebuilt neural network
    print('Scanned Text:')
    print(pytesseract.image_to_string('_temp.png'))
    cv2.imshow('Post-processed image', grey)
    cv2.waitKey(0)
    os.remove('_temp.png')

def prompt(*choices) -> str:
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
    return str(selection - 1)

def run():
    '''Connects to program to the main menu and contains the code required to start the script and to explain the user on what to do'''
    os.system('cls') if os.name == 'nt' else os.system('clear')
    while True:
        print('Please select choices based on the image being scanned. In can you are unsure of what to select, you can try different modes one by one to see which gives the best output.')
        mode = ''
        mode += prompt('The foreground and background are constrasting colors', 'The contrast differs throughout the image')
        mode += prompt('Salt & Pepper noise - Black/White pixels spread around the image irrespective of lighting', 'Gaussian Noise - Noise with similar distribution as the colors in the image')
        mode += prompt('Continue', 'Reduce even more noise - [only use this if the previous settings cant remove sufficient noise]')
        try:
            main(input('>>> Please enter the path to the image: '), mode)
        except:
            print('[!] Some error occured. Please check whether the path you entered is valid.')
        if prompt('Try Again', 'Quit') == '1':
            break
    os.system(f'"{sys.executable}" main.py')

if __name__ == '__main__':
    run()
