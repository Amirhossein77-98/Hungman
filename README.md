Word Game

This Python program is a simple word game where the player is presented with a shuffled word and has to guess the original word. The program uses the natural language toolkit (nltk) package to obtain a set of words from the English language corpus. It shuffles a random word from this set and prints it to the user. The user is then given three chances to guess the original word.


Dependencies

This program uses the subprocess, random, and sys packages that come with Python. nltk package is required to run this program. If nltk is not installed, the program will attempt to install it and download the words corpus. 


How to Run

To run the program, simply execute the code block in a Python environment.


Additional Notes

To change the number of tries the player has, the tries_left variable can be modified. 


The program only allows words that are alphabetical and have a length greater than 5. This can be changed by modifying the if statement on line 19.