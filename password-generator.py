#!/usr/bin/env python3.8
from random import randint 

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
special = "!£$%^&*()#@=/\<>"
letters_list = (list(letters))
numbers_list = (list(numbers))
special_list = (list(special))

length = int(input("How long do you want the password to be: "))
password =[]

for i in range(0,length):
    option = randint(1,3)
    if option == 1:
        select = randint(0,25)
        upper_lower = randint(1,2)
        if upper_lower == 1:
            password.append(letters_list[select].upper())
        else:
            password.append(letters_list[select])

    elif option == 2:
        select = randint(0,9)
        password.append(numbers_list[select])
    else:
        select = randint(0,15)
        password.append(special_list[select])

print(*password, sep="")

     

