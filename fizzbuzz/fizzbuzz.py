#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:54:46 2019

@author: marinefavre
"""

def fizzbuzz(number):
    
    if number % 3 == 0:
        
        return "Fizz"
    
    elif number % 5 == 0:
        
        return "Buzz"
    
    else:
        
        return number
    
print(fizzbuzz(13))
print(fizzbuzz(3))
print(fizzbuzz(50))