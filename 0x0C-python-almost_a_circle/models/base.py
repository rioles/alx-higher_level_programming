#!/usr/bin/python3
# base.py
"""Defines a base model class."""


class Base:
    """Represente the base class
    Attributes:
        __nb_objects (int) The number of intantiate Bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Base Constructor
        Args:
            id (int): The instance id
        """
        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
