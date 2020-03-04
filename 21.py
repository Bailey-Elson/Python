#!/usr/bin/env python3.8
from random import randint

def create_pack():
    deck = []
    for i in range (1,5):
        for j in range(1,14):
            if j == 1:
                card_num = str('A')
            elif j == 11:
                card_num = str('J')
            elif j == 12:
                card_num = str('Q')
            elif j == 13:
                card_num = str('K')
            else:
                card_num = str(j)
            if i == 1:
                card_suit = str(' H')
            elif i == 2:
                card_suit = str(' D')
            elif i == 3:
                card_suit = str(' S')
            elif i == 4:
                card_suit = str(' C')
            card = str(card_num + card_suit)
            deck.append(card)
    return deck

def shuffle_cards(deck):
    shuffled_deck = []
    for i in range(0,len(deck)):
        card = randint(0,len(deck)-1)
        shuffled_deck.append(deck[card])
        deck.pop(card)
    deck = shuffled_deck
    return deck

def deal_hands(deck):
    comp_hand = []
    users_hand = []
    for i in range(0,4):
        if i == 0 or i == 2:
            users_hand.append(deck[0])
        else:
            comp_hand.append(deck[0])
        deck.pop(0)
    print("Your cards are\ncard1: "+ users_hand[0] + "\ncard2: "+ users_hand[1])
    return users_hand, comp_hand, deck

def calculate_hand_value(hand):
    total_ace_high = 0
    total_ace_low = 0
    for i in range(0,len(hand)):
        card = (list(hand[i]))
        if card[0] == '1'  or card[0] == 'K' or card[0] == 'Q' or card[0] == 'J':
            value_ace_high = 10
            value_ace_low = 10
        elif card[0] == 'A':
            value_ace_high = 11
            value_ace_low = 1
        elif int(card[0]) > 1:
            value_ace_high = int(card[0])
            value_ace_low = int(card[0])
        total_ace_high = total_ace_high + value_ace_high 
        total_ace_low = total_ace_low + value_ace_low
    if total_ace_high == total_ace_low:
        hand_value = total_ace_high
    elif total_ace_high <= 21:
        hand_value = total_ace_high
    else:
        hand_value = total_ace_low
    return hand_value

def hit(hand, deck, bust):
    print("new card: "+ deck[0])
    hand.append(deck[0])
    deck.pop(0)
    for i in range(0, len(hand)):
        print(hand[i])
    hand_value = calculate_hand_value(hand)
    if hand_value > 21:
        bust = True
        print("BUST")
    return hand, bust, deck
    
def comp_hit_stick(deck, hand, bust):
    hand_value = calculate_hand_value(hand)
    card_percent = (int((21- int(hand_value))*4))
    num = randint(1,52)
    if hand_value <= 21:
        if num <= card_percent:
            print("hit")
            hand, bust, deck = hit(hand, deck, bust)
            stick = False
        else:
            print("stick")
            stick = True
    else:
        stick = True
    return stick, deck, hand

deck = create_pack()
deck = shuffle_cards(deck)
users_hand, comp_hand, deck = deal_hands(deck)
bust = False
stick = False
while bust == False:
    hit_stick = input("Would you like to hit or stick: ")
    if hit_stick == "hit":
        users_hand, bust, deck = hit(users_hand, deck, bust)
    elif hit_stick == "stick":
        hand_value = calculate_hand_value(users_hand)
        print(hand_value)
        break
while stick == False:
    stick, deck, cemp_hand = comp_hit_stick(deck, comp_hand, bust)
comp_hand_value = calculate_hand_value(comp_hand)
user_hand_value = calculate_hand_value(users_hand)
print("\nyour hand value: " + str(user_hand_value))
print("comp hand value: " + str(comp_hand_value))
if user_hand_value < 21 and (user_hand_value > comp_hand_value or comp_hand_value > 21):
    print("\nYOU WIN!!!\n")
elif comp_hand_value < 21 and (comp_hand_value > user_hand_value or user_hand_value > 21):
    print("\nCOMPUTER WINS!!!\n")
elif comp_hand_value > 21 and user_hand_value > 21:
    print("\nBoth Lose\n")
else:  
    print("Tie")
print("Your cards")
for i in range(0, len(users_hand)):
    print(users_hand[i])  
print("Total Value: "+ str(user_hand_value))
print("\nComputers Cards")
for i in range(0, len(comp_hand)):
    print(comp_hand[i]) 
print("Total Value: "+ str(comp_hand_value))