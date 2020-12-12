# HANGMAN
# Hangman ASCII ART and Word Bank from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
# Title ASCII Art from http://patorjk.com/software/taag

from random import choice

title = '''
    __                                          
   / /_  ____ _____  ____ _____ ___  ____ _____ 
  / __ \/ __ `/ __ \/ __ `/ __ `__ \/ __ `/ __ \
  
 / / / / /_/ / / / / /_/ / / / / / / /_/ / / / /
/_/ /_/\__,_/_/ /_/\__, /_/ /_/ /_/\__,_/_/ /_/ 
                  /____/                        
'''
print(title)
print('\n')

# Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

HANGMANPICS = ['''
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
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word = choice(words)
word_list = list(word)
player_word_view = []
lives = 6
current_word = ""

for i in range(len(word)):
    player_word_view += "_"


def ask_input():
    inp = input("Guess a Letter: ")
    return(inp)


def turn():
    p_input = ask_input()
    global lives
    global current_word
    integer = 0
    has_letter = False
    for letter in word_list:
        if(p_input == letter):
            has_letter = True
            player_word_view[integer] = letter
        integer += 1

    if(has_letter == False):
        print(''.join(player_word_view))
        print(f"There is no {p_input} in the word. You lose a life.")
        lives -= 1
        print(HANGMANPICS[6-lives])
    else:
        print(''.join(player_word_view))
        print(HANGMANPICS[6-lives])

    print('\n\n')
    current_word = ''.join(player_word_view)


while((lives > 0) and (current_word != word)):
    turn()

if(lives == 0):
    print("You Lose")
else:
    print("Congratulations, You Won!")
