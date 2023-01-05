#!/usr/bin/python3
"""
Module for a class that prevents dynamic attributes creation

"""


class LockedClass:
    """class to prevent dynamic attribute creation"""
    __slot__ = ['first_name']

    def __init__(self):
        """init method"""
        pass
