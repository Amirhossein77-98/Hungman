# Import builtin packages
import subprocess
import random
import sys
# Trying to import nltk package or install it if it's not
try:
    import nltk
except ModuleNotFoundError as e:
    # Handle missing package error here, such as installing the package
    missing_package = str(e).split("'")[1]
    print(f"The '{missing_package}' package is not installed. Installing now...\n!!!!! You may have to restart your code editor after installing the package!!!!!")
    subprocess.call(['pip', 'install', missing_package])
from nltk.corpus import words

# Download words corpus if needed
def download_words_corpus():
    try:
        words.words()
    except LookupError:
        nltk.download('words')

# Download words corpus if needed
download_words_corpus()

# Load set of words from nltk corpus
word_set = {word.lower() for word in words.words() if word.isalpha() and len(word) > 5}

def play_game():
    # Choose a random word from the set
    word = random.choice(list(word_set))

    # Shuffle the letters of the word
    shuffled_word = list(word)
    random.shuffle(shuffled_word)
    shuffled_word = ''.join(shuffled_word)

    # Set the number of tries
    tries_left = 3

    # Print the user's chances to try and shuffled word
    print(f"Your Chances: {tries_left} tries")
    print(f"Shuffled Word: {shuffled_word}")

    while tries_left > 0:
        # Get the input from the user
        user_guess = input("What's the word? ").lower()

        # Check if user's input matches the original word
        if user_guess == word:
            print("You WIN!")
            return True
        else:
            tries_left -= 1
            if tries_left > 0:
                print(f"Wrong, Try again!\nChances Left: {tries_left}")

    # If user has no more tries, print that they lost their chances and the right word
    print(f"You LOSE! The word was: {word}")
    return False

play_game()
