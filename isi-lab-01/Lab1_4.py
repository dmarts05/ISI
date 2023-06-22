#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:37:35 2023

@author: dmarts05
"""


def get_sentence():
    sentence = ''
    while len(sentence) == 0:
        sentence = input('Enter a sentence: ')
        if len(sentence) == 0:
            print('Sentence must be at least 1 character long, try again...')

    return sentence


def show_menu():
    print('***** SENTENCE CONVERSOR *****')
    print('a) Convert the sentence into uppercase.')
    print('b) Convert the sentence into lowercase.')
    print('c) Convert the first character of each word into uppercase.')
    print('d) Convert the characters that are in even positions into uppercase.')
    print('e) Exit.')


def convert_uppercase(sentence):
    return sentence.upper()


def convert_lowercase(sentence):
    return sentence.lower()


def convert_capitalize_each_word(sentence):
    words = [word[0].upper() + word[1:] for word in sentence.split(' ')]

    return ' '.join(words)


def convert_even_characters_uppercase(sentence):
    return ''.join([character.upper() if index % 2 else character for index, character in enumerate(sentence)])


sentence = get_sentence()
exit = False
option = ''
while True:
    show_menu()
    option = input('Select one of the previous options (a, b, c, d or e): ')

    result = ''

    if option == 'a':
        result = convert_uppercase(sentence)
    elif option == 'b':
        result = convert_lowercase(sentence)
    elif option == 'c':
        result = convert_capitalize_each_word(sentence)
    elif option == 'd':
        result = convert_even_characters_uppercase(sentence)
    elif option == 'e':
        break
    else:
        print('Invalid option, try again...')
        continue

    print('Result:', result)
