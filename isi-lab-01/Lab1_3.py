#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:32:08 2023

@author: dmarts05
"""


def get_factorial(number):
    if number < 0:
      return None
  
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


valid_input = False
number = 0

while not valid_input:
    try:
        number = int(input('Enter a number: '))
        valid_input = True
    except ValueError:
        print('Invalid input detected, try again...')

factorial = get_factorial(number)
print('Factorial of the given number:', factorial)
