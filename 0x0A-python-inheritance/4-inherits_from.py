#!/usr/bin/python3
"""Defines an inherited class (directly or indirectly) checking function."""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a_class that was (in)directly inherited
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
