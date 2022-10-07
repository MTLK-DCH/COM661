# import random
# import os
import hefs

# # loading
# live = 6
# # test os
# # print(os.listdir())
# words_f = open("wk1/words.txt", "r")
# # test file
# i = 0
# for line in words_f:
#     i += 1
#     print(line)
#     if i > 3:
#         break
# words = []

# # start
# # name = input("Please set your username:")
# print("Please set your username:")
# name = "abc"
# print("Hello {}! Welcome to game!".format(name))
# while True:
#     # nol = input("Please enter the number of the letter of the word you want to guess:")
#     print("Please enter the number of the letter of the word you want to guess:")
#     nol = 5
#     for line in words_f:
#         word = line.strip()
#         if len(word) == int(nol):
#             print(word)
#             words.append(word)
#     n = len(words)
#     if n > 0:
#         print("We have found {} words in the word list.".format(n))
#         break
#     else:
#         print("Sorry we can't find a word like that. Please enter another number.")

# i = random.randint(0, len(words) - 1)
# print(i)
# guess_word = words[i]

# test
live = 6
name = "abc"
nol = 4
guess_word = "word"
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(guess_word)

# start
print("Now we have found a word. Please guess it now. You have {} chances.".format(live))
guessing = "_" * nol
for i in range(live):
    print(guessing)
    print("Letters available:" + alphabet)
    input("Guess a letter:")
    if guessing == guess_word:
        hefs.win(name)


