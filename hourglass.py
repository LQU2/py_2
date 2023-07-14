




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
for i in range(1, 5):
    HOURGLASS.add((18, i)) # add walls for the top left straight wall
    HOURGLASS.add((36, i)) # add walls for the top right straight wall
    HOURGLASS.add((18, i + 19)) # add walls for the bottom left
    HOURGLASS.add((36, i + 19)) # add walls for the bottom right
for i in range(8):
    HOURGLASS.add((19 + i, 5 + i)) # add the top left slanted wall
    HOURGLASS.add((35 - i, 5+ i)) # add the top right slanted wall
    HOURGLASS.add((25 - i, 13 + i)) # add the bottom left slanted wall
    HOURGLASS.add((29 + i, 13 +i)) # add the bottom right slanted wall

#set up the initial sand at the top of the hourglass:
TOP_SAND = set()
for y in range(8):
    for x in range(19 + y, 36 - y):
        TOP_SAND.add((x, y + 4))


def main():
    bext.fg('yellow')
    bext.clear()

    # draw the quit message:
    bext.goto(0, 0)
    print('Ctrl-c to quit.', end='')

    # display the walls of the hourglass:
    for wall in HOURGLASS:
        bext.goto(wall[X], wall[Y])
        print(WALL, end='')

        while True: # main program loop
            allSand = list(TOP_SAND)

            # draw the initial sand:
            for sand in allSand:
                bext.goto(sand[X], sand[Y])
                print(SAND, end='')

            runHourglassSimulation(allSand)


def runHourglassSimulation(allSand):
    """run the stand falling simulation until the sand stops moving"""
    while True: #keep looping until sand has run out. while loop, it's going to keep looping until something in the program tells it to exit
        random.shuffle(allSand) #random order of grain simulaton

        sandMovedOnThisStep = False
        for i, sand in enumerate(allSand): 
            if sand[Y] == SCREEN_HEIGHT - 1: 
                # sand is on the bottom, it won't move: continue

            # if nothing is under this sand, move it down:
                noSandBelow = (sand[X], sand[Y] + 1) not in allSand
            noWallBelow = (sand[X], sand[Y] + 1) not in HOURGLASS
            canFallDown = noSandBelow and noWallBelow

            if canFallDown:
                # draw the sand in its new position down one space:
                bext.goto(sand[X], sand[Y])
                print(' ', end='') # clear the old position
                bext.goto(sand[X], sand[Y] + 1)
                print(SAND, end='')

                # set the sand in its new position down one space:
                allSand[i] = (sand[X], sand[Y] +1)
                sandMovedOnThisStep = True
            else:
                # check if the sand can fall to the left:
                belowLeft = (sand[X] - 1, sand[Y] + 1)
                noSandBelowLeft = belowLeft not in allSand
                noWallBelowLeft = belowLeft not in HOURGLASS
                left = (sand[X] - 1, sand[Y])
                noWallLeft = left not in HOURGLASS
                notOnLeftEdge = sand[X] > 0
                canFallLeft = (noSandBelowLeft and noWallBelowLeft
                    and noWallLeft and notOnLeftEdge)
                
                # check if the sand can fall to the right:
                belowRight = (sand[X] +1, sand[Y] + 1)
                noSandBelowRight = belowRight not in allSand
                nowWallBelowRight = belowRight not in HOURGLASS
                right = (sand [X] + 1, sand[Y])
                noWallRight = right not in HOURGLASS
                notOnRightEdge = sand[X] < SCREEN_WIDTH - 1
                canFallRight = (noSandBelowRight and nowWallBelowRight
                    and noWallRight and notOnRightEdge)
                
                # set the falling direction:
                fallingDirection = None
                if canFallLeft and not canFallRight:
                    fallingDirection = -1 #set the sand to fall left
                elif not canFallLeft and canFallRight:
                    # both are possible, so randomly set it:
                    fallingDirection = random.choice((-1, 1))

                # check if the sand can "far" fall two spaces to
                # the left or right instead of just one space:
                if random.random() * 100 <= WIDE_FALL_CHANCE:
                    belowTwoLeft = (sand[X] - 2, sand[Y] + 1)
                    noSandBelowTwoLeft = belowTwoLeft not in allSand
                    noWallBelowTwoLeft = belowTwoLeft not in HOURGLASS
                    notOnSecondToLeftEdge = sand[X] > 1
                    canFallTwoLeft = (canFallLeft and noSandBelowTwoLeft
                        and noWallBelowTwoLeft and notOnSecondToLeftEdge)
                    
                    belowTwoRight = (sand[X] +2, sand[Y] + 1)
                    noSandBelowTwoRight = belowTwoRight not in allSand
                    noWallBelowTwoRight = belowTwoRight not in HOURGLASS
                    notOnSecondToRightEdge = sand[X] < SCREEN_WIDTH - 2
                    canFallTwoRight = (canFallRight
                        and noSandBelowTwoRight and noWallBelowTwoRight
                        and notOnSecondToRightEdge)
                    
                    if canFallTwoLeft and not canFallTwoRight:
                        fallDirection = -2
                    elif not canFallTwoLeft and canFallTwoRight:
                        fallingDirection = 2
                    elif canFallTwoLeft and canFallTwoRight:
                        fallingDirection = random.choice((-2, 2))

                if fallingDirection == None:
                    # this sand can't fall, so move on continue

                # draw the sand in its new position:
                    bext.goto(sand[X], sand[Y])
                print(' ', end='') # erase old sand
                bext.goto(sand[X] + fallingDirection, sand[Y] + 1)
                sandMovedOnThisStep = True

                # move the grain of sand to its new position:
                allSand[i] = (sand[X] + fallingDirection, sand[Y] + 1)
                sandMovedOnThisStep = True

            sys.stdout.flush() # (required for bext-using programs)
            time.sleep(PAUSE_LENGTH) # pause after this

            # if no sand has moved on this step, reset the hourglass:
            if not sandMovedOnThisStep:
                time.sleep(2)
                # erase all of the sand:
                for sand in allSand:
                    bext.goto(sand[X], sand[Y])
                    print(' ', end='')
                break # break out of the main simulation loop

# if this program was run (instead of imported), run the game:

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() #when ctrl-c is pressed, end the program