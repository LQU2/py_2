import random

try: 
    import pyperclip #pyperclip copies text to the clipboard
except ImportError:
    pass #if pyperclip isn't installed, it does nothing

def main():
    print('''L3375P34]< (leetspeak)
          
Enter your leet messsage:''')
    english = input('> ')
    print() #produces an empty line
    leetspeak = englishToLeetspeak(english) #The code calls a function named englishToLeetspeak() and passes the english variable as an argument. This function is responsible for converting the English text to leetspeak.
    print(leetspeak)

    try: 
        #if pyperclip wasn't imported it will raise a NameError exception
        pyperclip.copy(leetspeak) # function is pyperclip.copy and passes the variable leetspeak as an argument
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass # do nothing if pyperclip wasn't installed


def englishToLeetspeak(message): #function and parameter
    """convert the english string in message and returns it to leetspeak."""
    # make sure all keys in 'charMapping' are lowercase
    charMapping = {
    'a': ['4'], 'e': ['3'],
    'i': ['1'],
    }
    leetspeak = ''
    for char in message: #check each character:
        # there's a 100% chance we change the character to leetspeak
        if char.lower() in charMapping and random.random() <= 100:
            possibleLeetReplacements = charMapping[char.lower()]
            leetReplacement = random.choice(possibleLeetReplacements)
            leetspeak = leetspeak + leetReplacement
        else:
            # don't translate this character:
            leetspeak = leetspeak + char
    return leetspeak

# if this program was run (instead of imported), run the game:
if __name__ == '__main__': 
    main()
 