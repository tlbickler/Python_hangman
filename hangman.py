"""
Hangman Game
This module implements a simple Hangman game with ASCII art.
"""

from wonderwords import RandomWord
# import from https://pypi.org/project/wonderwords/

hangmanPics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# ASCII https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c


def hangman():
    """Basic Python game with ASCCI Art found on github"""

    # random word creator
    rw = RandomWord()
    word = rw.word()
    answer = list(word)

# Opening
    print("Let's play Hangman!")
    print(hangmanPics[0])

    # Basic varables
    character_count = len(answer)
    blanks = []
    incorrect = []
    tries = 0

    # Blanks set up
    while len(blanks) != character_count:
        blanks.append(" _ ")

    print("\n", *blanks, "\n", "\n"),

    # function for updating screen after user input
    def update_screen():
        print(hangmanPics[tries])
        print("\n", *blanks, "\n", "\n")
        print("Incorrect Guesses: ", incorrect)

    # Main game
    while " _ " in blanks and tries != 6:
        player_input = input("Guess a letter: ")

        # correct answers
        if player_input in answer and player_input not in blanks:
            for index, letter in enumerate(answer):
                i = []
                if letter == player_input:
                    i.append(index)
                    for index in i:
                        blanks[index] = player_input

            update_screen()
        # Repeat answers
        elif player_input in incorrect or player_input in blanks:
            print("You already tried that! Try again")

            # wrong answers
        else:
            tries += 1
            incorrect.append(player_input)
            update_screen()

    # winning the game
    if " _ " not in blanks:
        print("You win!!!")
        return
    # Losing the game
    elif tries == 6:
        print("Nice try! The word was: ", word)
        return


hangman()
