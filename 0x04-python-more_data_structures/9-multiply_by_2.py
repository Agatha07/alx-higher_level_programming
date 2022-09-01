#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return ({keys: a_dictionary[k] * 2 for keys in a_dictionary})
