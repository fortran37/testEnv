"""Shortcuts for commonly used functions during testing"""

from time import sleep
import os
import sys

def cls():
    """Clears the screen after sleeping for 1 second."""
    print("Clearing")
    sleep(1)
    os.system('cls')

def cwd():
    """Returns current directory."""
    x = os.getcwd()
    return x

def walk():
    """Return directory info using os.walk."""
    x = cwd()
    for i in os.walk(x):
        return i
def lsd():
    """Print available directories in current location."""
    x = cwd()
    print("Available directories in:",x,"\n")
    count = 1
    for i in os.listdir():
        if os.path.isdir(i):
            print(count,i)
            count += 1
def lsf():
    """Print available files in current location."""
    x = cwd()
    count = 1
    print("Available files in: ",x,"\n")
    for i in os.listdir():
        if not os.path.isdir(i):
            print(count,i)
            count+=1


def cd():
    """Prompts for desired location then changes directory."""
    x = os.getcwd()
    y = os.listdir()
    print("Current directory: ",x,y)
    count = 0
    while True:
        
        try:
            desDir = input("Where to? ")
            if desDir:
                try:
                    os.chdir(desDir)
                    z = os.getcwd()
                    print("Now in: ",os.getcwd())
                    break
                except:
                    print("Input was invalid.")
                    
                    count += 1
                    if count >= 3:
                        print("Failed 3 times, returning...")
                        break
                    continue
            else:
                print("No input, staying in: ", os.getcwd())
                break
        except:
            print("Exception!!!")
            break


def sdel():
    f2d = input("What file would you like to delete?")
    os.remove(f2d)


def clnStr(dirtyString):
    cleanString = ''.join(i for i in dirtyString if i.isalnum())    
    return cleanString


