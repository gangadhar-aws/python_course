#Step 1
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random

word_list = ["aardvark", "baboon", "camel"]
choosen_word = random.choice(word_list)

print(choosen_word)

e_list = ["_" for i in range(len(choosen_word))]



game_on = True
lives = 7

while game_on:
    guess = input("Guess a Letter ? : ").lower()

    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            e_list[position] = letter

    if guess not in choosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_on = False
            print("You Lose")
    if "_" not in e_list:
        game_on = False
        print("You Won")

    print(stages[lives])
    print(e_list)