# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "MITx6.00.1x/unit3-structured-types/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # read letters of secretword into a dict
    db = {
        x: 1 for x in secretWord
    }

    # subtract letters guessed from the keys
    for x in lettersGuessed:
        if x in db:
            db[x] -= 1

    # db values to a list, and do a sum.
    result = sum(db.values())

    # if result is greater than one, no bueno
    if result > 0:
        return False
    else:
        return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # store the feedback for the user as a list
    feedback = []

    # now iterate over the word. If we have a guessed letter, show it
    # and if we do not then, then use an underscore with a space > 
    for letter in secretWord:
        if letter in lettersGuessed:
            feedback.append(letter)
        else:
            feedback.append("_ ")

    # string the list and we're done
    return "".join(feedback)





def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # it is a little code golfy, but this is perfect for list comprehension
    results = [x for x in string.ascii_lowercase if x not in lettersGuessed]

    # now join it up as a string
    return "".join(results)

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # first thing is first, we need a game loop based on a variable
    completed = False

    # user gets 8 guesses.
    guesses = 8

    # list for the input
    users_input = []

    # now print out the introduction text
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {0} letters long.".format(len(secretWord)))
    print("-------------")
    # entre la loop
    while not completed:
      # if there are no guesses left, end the game
      if guesses < 1:
          print('Sorry, you ran out of guesses. The word was {0}. '.format(secretWord))
          break

      # 
      print("You have {0} guesses left.".format(guesses))
      print("Available letters: {0}".format(getAvailableLetters(users_input)))

      # take input as a guess
      guess = input("Please guess a letter: ")


      # if user has already guessed the letter, short circuit and continue
      if guess in users_input:
        feedback = getGuessedWord(secretWord, users_input)
        print("Oops! You've already guessed that letter: {0}".format(feedback))
        print("-------------")
        continue

      # whilst we never trust user input, let's trust user input.
      users_input.append(guess)

      # is the word guessed?
      if isWordGuessed(secretWord, users_input):
        print('Good guess: {0}'.format(secretWord))
        print("-------------")
        print("Congratulations, you won!")
        break
          

      # we need this in both cases
      feedback = getGuessedWord(secretWord, users_input)

      # process the input
      if guess in secretWord:
        # it was good, so feedback and decrement guesses.
        print('Good guess: {0}'.format(feedback))
      
      else:
        # uh-oh, it was a bad guess.
        print("Oops! That letter is not in my word: {0}".format(feedback))
        
        # decrement guesses
        guesses -= 1

      # now the feedback 
      print("-------------")









# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

import sys
if not 'test' in sys.argv:
  secretWord = chooseWord(wordlist).lower()
  hangman(secretWord)




