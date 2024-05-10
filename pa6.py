#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:24:13 2024

@author: annette
"""


def make_change(total):
    '''returns a list of all distinct combinations of coins'''
    coins = [1, 5, 10, 25, 100]
    def find_combinations(amount, current_index):
        if amount == 0:
            return [[]]
        if amount < 0 or current_index >= len(coins):
            return []
        with_coin = find_combinations(amount - coins[current_index],\
                                      current_index)
        with_coin = [[coins[current_index]] + combo for combo in with_coin]
        without_coin = find_combinations(amount, current_index + 1)
        return with_coin + without_coin
    return find_combinations(total, 0)
print(make_change(10))

def dict_filter(function, dictionary):
    '''Filters dictionary and returns a dictionary where function returns
    True for all key and value pairs in the dictionary'''
    new_dict = {}
    for x in dictionary.keys():
        if function(x, dictionary[x]):
            new_dict[x] = dictionary[x]
    return new_dict


def treemap(function, tree):
    '''Maps function to the tree'''
    tree.key, tree.value = function(tree.key, tree.value)
    if len(tree.children) != 0:
        for x in tree.children:
            treemap(function, x)


class DTree:
    '''Trees modeling decisions'''
    def __init__(self, variable, threshold, lessequal, greater, outcome):
        if variable is threshold is lessequal is greater is outcome is None:
            raise ValueError('all values are None')
        if outcome is None:
            if variable is None or threshold is None or lessequal is None or\
            greater is None:
                raise ValueError('atleast one of the first four arguments is missing')
        if variable is not None and threshold is not None and lessequal\
            is not None and greater is not None and outcome is not None:
            raise ValueError('first four values and last value is not None')
        self.variable = variable
        self.threshold = threshold
        self.lessequal = lessequal
        self.greater = greater
        self.outcome = outcome

    def tuple_atleast(self):
        '''finding least'''
        atleast = 0
        if self.outcome is None:
            atleast = self.variable + 1
            if self.lessequal.tuple_atleast() > atleast:
                atleast = self.lessequal.tuple_atleast()
            if self.greater.tuple_atleast() > atleast:
                atleast = self.greater.tuple_atleast()
        return atleast

    def find_outcome(self, tuple1):
        if self.outcome is None:
            if tuple1[self.variable] <= self.threshold:
                return self.lessequal.find_outcome(tuple1)
            return self.greater.find_outcome(tuple1)
        return self.outcome

    def no_repeats(self):
        if self.outcome is None:
            if self.variable in (self.lessequal.variable, self.greater.variable):
                return False
            if self.lessequal.no_repeats is False:
                return False
            if self.greater.no_repeats is False:
                return False
        return True

