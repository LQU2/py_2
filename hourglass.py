




import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# set up the constants:
PAUSE_LENGTH = 0.2 # change this to 0.0 or 1.0git i
# try changing this to any number between 0 and 100:
WIDE_FALL_CHANCE = 50

SCREEN_WIDTH = 79
SCREEN_HEIGHT = 25
X = 0 #the index of X values in an (x,y) tuple is 0
Y = 1 #the index of Y values in an (x,y) tuple is 1
SAND = chr(9617)
WALL = chr(9608)

# set up the walls of the hourglass:
HOURGLASS = set() #Has (x,y) tuples for where hourglass walls are
# (!) comment some HOURGLASS.add() lines to erase walls:
for i in range(18, 37):
    HOURGLASS.add((i, 1)) # add walls for the top cap of the hourglass
    HOURGLASS.add((i, 23)) # add walls for the bottom cap

    #hey