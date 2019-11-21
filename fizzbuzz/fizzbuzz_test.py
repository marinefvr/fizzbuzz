#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:00:35 2019

@author: marinefavre
"""

from fizzbuzz import fizzbuzz

def test_passing_3_returns_fizz():
    
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(99) == "Fizz"
    assert fizzbuzz(15) == "Fizz"

def test_passing_5_returns_fizz():
    
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(50) == "Buzz"
    assert fizzbuzz(40) == "Buzz"
    