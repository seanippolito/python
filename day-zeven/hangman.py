import random
from hangman_art import logo, stages
from hangman_words import word_list as word_dict

print(logo)
word = random.choice(word_dict)
print(word)
word_list = list(word)
word_hidden = list("_" * len(word))
print("H A N G M A N")
hangman = ""
# hangman = list("hangman")
# hangman_hidden = list("_" * len(hangman))
for i in range(len(word_list) + 7):
    print()
    print("".join(word_hidden))
    print(hangman)
    letter = input("Guess a letter: ")
    if letter in word_list:
        for j in range(len(word_list)):
            if letter == word_list[j]:
                word_hidden[j] = letter

        if (word_hidden == word_list):
            print("You guessed the word!")
            break
    else:
        print("No such letter in the word")
        if (len(stages) == 0):
            print("You are hanged!")
            break
        hangman = stages.pop()
print(word_hidden)
print(hangman)
print("Thanks for playing!")
print("We'll see how well you did in the next stage")