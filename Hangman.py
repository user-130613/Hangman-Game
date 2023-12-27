import random
import time


print("Welcome to hangman game :)")
print()
time.sleep(1)

name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print()

print("Before you play The Hangman game ,lets get to know the rules.")
print()

time.sleep(3)
print()

print (" 1) Players should try to figure out an unknown word by guessing letters.")
print()

time.sleep(2)
print(" 2) As letters in the word are guessed, that leeter gets printed above its cooresponding underline.")
print()

time.sleep(2)
print(" 3) If the you letter guessed is not in the word, one part of the person gets hanged.")
print()

time.sleep(2)
print(" 4) The person is drawn in 6 parts in the order: head, body, left leg, right leg, left arm, right arm.")
print()

time.sleep(2)
print(" 5) So to win, you have to guess the word before you get 6 letters wrong.")
print()

time.sleep(2)
print(" 6) If you guessed 6 letters wrong, then the man will be hanged and you loose.")
print()

time.sleep(2)
print()

print("ALL THE VERY BEST :)")
time.sleep(2)
hang = ["""
H A N G M A N
   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]


def getRandomWord():
    words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple','bear'
             'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'peach', 'lychee', 'muskmelon']

    word = random.choice(words)
    return word


def displayBoard(hang, missedLetters, correctLetters, secretWord):
    print(hang[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print("\n")


def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():

     print('Do you want to play again? (yes or no)')
     return input().lower().startswith('y')


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord()
gameIsDone = False

while True:
    displayBoard(hang, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\nYes! The secret word is "' +
                  secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(hang) - 1:
            displayBoard(hang, missedLetters,
                         correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord()
        else:
            break


