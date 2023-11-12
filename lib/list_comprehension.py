#!/usr/bin/env python3

def return_evens(num_list):
    final_list = []
    for num in num_list:
        if num % 2 == 0:
            final_list.append(num)
    return final_list

def make_exclamation(sentence_list):
    new_list = []
    for sentence in sentence_list:
        new_list.append(sentence + "!")
    return new_list