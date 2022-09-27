#!/usr/bin/python3
"""
 Finds if the object is an instance of, or if the object is
 an instance of a class that inherited from, the specified class 
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of or inherited from a specified class
    """
    return(isinstance(obj, a_class))
