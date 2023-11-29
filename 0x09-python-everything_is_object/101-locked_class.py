#!/usr/bin/python3
"""Defines a locked class"""

class LockedClass:
    """
    Prevent the user from instantiating new locked Class attributes
    for anything but the attributes called "first_name"
    """

    __slots__ = ["first_name"]
