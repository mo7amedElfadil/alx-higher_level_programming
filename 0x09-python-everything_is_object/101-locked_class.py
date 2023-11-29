#!/usr/bin/python3
"""Locked Class Module"""


class LockedClass():
    """Definition of a LockedClass where:
    - there are no class or object attributes
    - dynamically created instance attributes are prevented
        - except if the new instance is called first_name

    """
    __slots__ = ['first_name']
