#!/usr/bin/env python3

def return_evens(num_list):
    final_list = []
    for i in range(len(num_list)):
        if i %2 == 0:
            final_list.append(num_list[i])

def make_exclamation(sentence_list):
    for i in range(len(sentence_list)):
        sentence_list.append(sentence_list[i] + "!")