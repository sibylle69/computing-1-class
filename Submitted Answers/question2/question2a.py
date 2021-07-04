'''
question2.py


Fix the errors so that this code runs when called
from the test file and passes all tests.

TOTAL POINTS AVAILABLE: 5 


Code Functionality (5)
5 points - no errors remain and code runs
4 points - only 1 error remains
1-3 points - multiple errors remain
0 points - all original errors remain or new ones introduced
'''


def nato_spelling(input_string):
    '''Takes in a string and replaces each letter with the NATO phoenetic 
    alphabet that corresponds with that letter.

    https://en.wikipedia.org/wiki/NATO_phonetic_alphabet
    
    e.g. 'hello' returns 'Hotel Echo Lima Lima Oscar' '''

    # create a new string
    nato_string = ''
    # for each letter in the input string
    for letter in input_string:
        # if it is a letter (not a number or puntcuation)
        if letter.isalpha():
            # look up the corresponding NATO word 
            # and add to the string separated by a space
            nato_string += look_up_word(letter) +  ' '
    
    # remove the last space added to the string and 
    nato_string = nato_string.strip()
    # then return the string
    return nato_string



def look_up_word(letter):
    '''Return the NATO phoetic alphabet word to the corresponding letter.
    Can handle only letters, but can be upper or lower case.
    
    e.g. both 'H' and 'h' will return 'hotel' '''

    nato_words = {'a':'Alfa', 'b':'Bravo', 'c':'Charlie', 'd':'Delta', 
                  'e':'Echo', 'f':'Foxtrot', 'g':'Golf', 'h':'Hotel', 
                  'i':'India', 'j':'Juliett', 'k':'Kilo', 'l':'Lima', 
                  'm':'Mike', 'n':'November', 'o':'Oscar', 'p':'Papa', 
                  'q':'Quebec', 'r':'Romeo', 's':'Sierra', 't':'Tango',
                  'u':'Uniform', 'v':'Victor', 'w':'Whiskey', 'x':'X-ray', 
                  'y':'Yankee', 'z':'Zulu'}

    # make sure the letter is lower case
    letter = letter.lower()

    # return the corresponding word
    return nato_words[letter]


