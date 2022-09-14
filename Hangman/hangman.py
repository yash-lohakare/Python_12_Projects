import string
import random
from word_list import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #getting letters from the word
    alphabet =set(string.ascii_uppercase) #getting uppercase alphabets
    used_letters = set() #adding already used letters

    #Getting user input
    while len(word_letters) > 0 :
        #letters used
        print("You have already used the letters ",' '.join(used_letters))

        char_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word is ', ' '.join(char_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You've already used the character. Try again!")
        
        else:
            print("Invalid character")

    print("The correct word was "+ word)
hangman()