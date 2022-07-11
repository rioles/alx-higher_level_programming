import unittest
"""Base class"""
class Base:
    __nb_object = 0
    def __init__(self, id = None):
        """Constructor of base class
        Args:
            id (int): The object id
        """
        if self.id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
