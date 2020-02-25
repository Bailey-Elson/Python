#!/usr/bin/env python3.8

from random import randint

def scissor(rsp):
    if users_rsp == "scissors":
        result = 'we tie'
    elif users_rsp == 'rock':
        result = 'you win'
    elif users_rsp == 'paper':
        result = 'you lose'
    return result

def paper(rsp):
    if users_rsp == "paper":
        result = 'we tie'
    elif users_rsp == 'scissors':
        result = 'you win'
    elif users_rsp == 'rock':
        result = 'you lose'
    return result

def rock(rsp):
    if users_rsp == "rock":
        result = 'we tie'
    elif users_rsp == 'paper':
        result = 'you win'
    elif users_rsp == 'scissors':
        result = 'you lose'
    return result

def comprps(rsp, users_rsp):
    if rsp == 1:
        result = scissor(users_rsp)
        comp_rsp = 'scissors'
    elif rsp == 2:
        result = paper(users_rsp)#
        comp_rsp = 'paper'
    elif rsp == 3:
        result = rock(users_rsp)
        comp_rsp = 'rock'
    return result, comp_rsp

def output(result, comp_rsp):
    print("i picked "+ comp_rsp + "\nyou picked "+users_rsp + "\n" + result)

rsp = randint(1,3)
users_rsp = input("what is your choice (rock, paper or scissors):\n")

result, comp_rsp = comprps(rsp, users_rsp)
output(result, comp_rsp)
