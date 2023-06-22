#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:51:03 2023

@author: dmarts05
"""


def convert_celsius_to_farenheit(celsius):
    return (9/5 * celsius) + 32


valid_input = False
celsius = 0
farenheit = 0

while not valid_input:
    try:
        celsius = float(input('Enter Celsius degrees: '))
        valid_input = True
    except ValueError:
        print('Invalid input detected, try again...')

farenheit = convert_celsius_to_farenheit(celsius)
print(
    f'The temperature of {round(celsius, 1)} degrees Celsius corresponds to {round(farenheit, 1)} degrees Farenheit.')
