#!/usr/bin/python3
"""
Finds if the object is an instance of, or if the object is an
instance of a class that inherited from, the specified class 
"""


def is_kind_of_class(obj, a_class):
"""Checks if an object is an instance of or inherited from a specified class
    
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False
    """
    return(isinstance(obj, a_class))
