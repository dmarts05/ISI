#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:59:08 2023

@author: dmarts05
"""

negative_number = False
numbers = []
while not negative_number:
    try:
        current_number = float(input('Enter a number: '))

        if current_number < 0:
            negative_number = True
            print('Negative number entered!')

        numbers.append(current_number)
    except ValueError:
        print('Invalid input detected, try again...')

# Show entered numbers
print('Numbers:', numbers)

# Show squares of those numbers
squared_numbers = [number**2 for number in numbers]
print('Squared Numbers:', squared_numbers)

# Show sum of the squares of those numbers
sum_squared_numbers = sum(squared_numbers)
print('Sum of Squared Numbers:', sum_squared_numbers)
