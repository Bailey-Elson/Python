#!/usr/bin/env python3.8

from random import randint

num = randint(1,100)
correct = False

def guess(num, correct):
    for i in range (0,10):
        guess = int(input("what is your guess:"))
        if guess == num:
            correct = True
            return correct, num
            break 
        elif guess > num:
            print("Too high")
        elif guess < num:
            print("too small")
    return correct, num

def output(num, correct):
    if correct == True:
        print("Congrats you have guessed the number")
    elif correct == False:
        print("you didn't manage to guess the number \n the number was:"+ str(num))

correct, num = guess(num, correct)
output(num, correct)
