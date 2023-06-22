#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:17:24 2023

@author: dmarts05
"""


def get_num_dni():
    valid_input = False
    num_dni = 0

    while not valid_input:
        try:
            num_dni = int(input('Enter an 8 digit number: '))
            if len(str(num_dni)) == 8:
                valid_input = True
            else:
                print('Invalid input, number must have exactly 8 digits, try again...')
        except ValueError:
            print('Invalid input detected, entered input is not a number, try again...')

    return num_dni


def get_letter_num_dni(num_dni):
    letters = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
               'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

    return letters[num_dni % 23]


num_dni = get_num_dni()
letter = get_letter_num_dni(num_dni)
print('DNI letter:', letter)
print(f'Full DNI: {num_dni}{letter}')
