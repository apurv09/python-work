# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:18:03 2018

@author: avengers
"""

import random

comGuess=random.randint(0,100)

while True:
    userGuess=int(input("Guess a number between 0-100:"))
    if userGuess>comGuess:
        print("Guess lower")
    elif userGuess<comGuess:
        print("Guess Higher")
    else:
        print("congrats correct guess")
        break