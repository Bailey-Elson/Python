#!/usr/bin/env python3.8

def print_image(word_list, output_word, turns_left, correct, wrongGuess, complete):
    while turns_left == True and complete == False:
        if wrongGuess == 0:
            output_word, wrongGuess = input_guess(word_list, output_word, wrongGuess, correct)
        elif wrongGuess == 1:
            print(level1)
            output_word, wrongGuess = input_guess(word_list, output_word, wrongGuess, correct)
        elif wrongGuess == 2:
            print(level2)    
            output_word, wrongGuess = input_guess(word_list, output_word, wrongGuess, correct)
        elif wrongGuess == 3:
            print(level3)    
            output_word, wrongGuess = input_guess(word_list, output_word, wrongGuess, correct)
        elif wrongGuess == 4:
            print(level4)    
            output_word, wrongGuess = input_guess(word_list, output_word, wrongGuess, correct)
        elif wrongGuess == 5:
            print(level5)    
            output_word, wrongGuess = input_guess(word_list, output_word, wrongGuess, correct)
        elif wrongGuess == 6:
            print(level6)    
            output_word, wrongGuess = input_guess(word_list, output_word, wrongGuess, correct)
        elif wrongGuess == 7:
            print(level7)    
            output_word, wrongGuess = input_guess(word_list, output_word, wrongGuess, correct)
        elif wrongGuess == 8:
            print(level8)    
            output_word, wrongGuess = input_guess(word_list, output_word, wrongGuess, correct)
        elif wrongGuess == 9:
            print(level9)    
            output_word, wrongGuess = input_guess(word_list, output_word, wrongGuess, correct)
        elif wrongGuess == 10:
            print(level10)    
            output_word, wrongGuess = input_guess(word_list, output_word, wrongGuess, correct)
        elif wrongGuess == 11:
            print(level11)
            print("oh no \nyou lose")    
            turns_left = False
            return output_word, complete, turns_left
            break
        complete = check_complete(complete, output_word)
    return output_word, complete, turns_left

def input_guess(word_list, output_word, wrongGuess, correct):
    guess = input("Guess a letter:")
    correct = False
    for i in range(0,len(word_list)): 
        if word_list[i] == guess:
            output_word[i] = guess
            correct = True
    if correct == True:
        correct = False
        return output_word, wrongGuess
    else:
        wrongGuess = wrongGuess + 1
        return output_word, wrongGuess

def check_complete(complete, output_word):
    complete = True
    print(output_word)
    print("")
    for i in range(0,len(output_word)):
        if output_word[i] == "_":
            complete = False
    return complete



level1 =str("_____________________\n")
level2 =str("|\n|\n|\n|\n|\n|\n|\n_____________________\n")
level3 =str("___________________\n|\n|\n|\n|\n|\n|\n|\n_____________________\n")
level4 =str("___________________\n|  /\n| /\n|/\n|\n|\n|\n|\n_____________________\n")
level5 =str("___________________\n|  /              |\n| /               |\n|/\n|\n|\n|\n|\n_____________________\n")
level6 =str("___________________\n|  /              |\n| /               |\n|/                0\n|\n|\n|\n|\n_____________________\n")
level7 =str("___________________\n|  /              |\n| /               |\n|/                0\n|                 |\n|                 |\n|\n|\n_____________________\n")
level8 =str("___________________\n|  /              |\n| /               |\n|/                0\n|              ---|\n|                 |\n|\n|\n_____________________\n")
level9 =str("___________________\n|  /              |\n| /               |\n|/                0\n|              ---|---\n|                 |\n|\n|\n_____________________\n")
level10 =str("___________________\n|  /              |\n| /               |\n|/                0\n|              ---|---\n|                 |\n|                /  \n|\n_____________________\n")
level11 = str("___________________\n|  /              |\n| /               |\n|/                0\n|              ---|---\n|                 |\n|                / \ \n|\n_____________________\n")

wrongGuess = int(0)

word = input("Player 1 enter the word:")
word_list = (list(word))
output_word = list = ['_' for x in range(len(word_list))]
print(output_word)
turns_left = True
correct = False
complete = False 

while complete == False and turns_left == True:
    output_word, complete, turns_left = print_image(word_list, output_word, turns_left, correct, wrongGuess, complete)
if complete == True:
    print("Congratualtions you have won")

