#!/usr/bin/python3
# 0-lookup.py

""" File name : 0-lookup.py
    It is not allowed to import any module
"""

def lookup(obj):
    """Return a list of an object's available attributes
    Args:
        obj (object): given object
    """
    return dir(obj)
