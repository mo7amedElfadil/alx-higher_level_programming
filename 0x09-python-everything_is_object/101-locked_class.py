#!/usr/bin/python3
"""Locked Class Module"""


class LockedClass():
    """Definition of a LockedClass where:
    - there are no class or object attributes
    - dynamically created instance attributes are prevented
        - except if the new instance is called first_name

    """
    def __setattr__(self, attr, value):
        if attr == 'first_name':
            self.__dict__[attr] = value
        else:
            raise AttributeError(f"'{LockedClass.__name__}'" +
                                 f" object has no attribute '{attr}'")
