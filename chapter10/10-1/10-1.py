""" 10-1 -- Hangman Game.

Modify the game, so a word is selected randomly from a list of words.
"""


import random

def hangman(word):
    """ Hangman game logic.
    
    Args:
        word: Word to be guessed.
        
    Returns:
        None.
    """
    wrong = 0
    stages = ["",
              "___________          ",
              "|                    ",
              "|          |         ",
              "|          0         ",
              "|         /|\        ",
              "|         / \        ",
              "|                    ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False

    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))


words = ["test",
         "cat",
         "dog",
         "elephant",
         "giraffe",
         "dinosaur",
         "panda"]

hangman(words[random.randint(0, len(words) - 1)])
