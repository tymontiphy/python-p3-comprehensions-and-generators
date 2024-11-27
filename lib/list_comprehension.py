#!/usr/bin/env python3

def return_evens(num_list):
    '''Returns a new list containing only the even numbers from num_list.'''    
    return [num for num in num_list if num % 2 == 0]
    pass

def make_exclamation(sentence_list):
    '''Returns a new list containing sentences with an exclamation mark at the end.'''
    return [sentence + '!' for sentence in sentence_list]
    pass