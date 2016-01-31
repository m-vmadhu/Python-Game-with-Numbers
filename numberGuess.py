'''
Game: Can you guess a secret number which python is going to pick ??
Player1 : Python code
Player2 : Its you !
You have 3 chances to Guess the number python is going to pick from 0-100
Give a try....All the best !

copyrights @ itzme-vasu '''

import sys
from random import randint

secret_number=randint(0,100) 
attempt_count=0
result=0

def input_guess(guess):
    if(guess==secret_number):
        print("Hurray !!! You got it right.... ")
        return 1
    elif(guess>secret_number):
        print("Your guess is Higher than my Secret Number !")
        return 0
    elif(guess<secret_number):
        print("Your guess in Lower than my Secret Number !")
        return 0
    else:
        print("please enter a valid number !!!")

print(" I have a number in my mind in the range (0,100)...You have 3 chances to guess my Secret !!")

while(attempt_count<3 and result==0):
    attempt_count+=1
    guess=int(input("Enter your Guess, lets check : "))
    print("your Guess was %d"%guess)
    result=input_guess(guess)

if(result != 1):
    print("sorry you lost the game !")
elif(result ==1):
    print("CONGRATSS.....................")
