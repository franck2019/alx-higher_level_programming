#!/usr/bin/python3
"""This module has a class called LockedClass."""


class LockedClass:
    """The LockedClass."""

    def __setattr__(self, attr_name, attr_value):
        """Prevents the user from dynamically creating
        new instance attributes except if the new instance
        attribute is called <first_name>.

        Args:
            attr_name: the name of the attribute
            attr_value: the value of the attribute."""

        if attr_name != "first_name":
            sms = "'LockedClass' object has no attribute '{}'"
            raise AttributeError(sms.format(attr_name))
        else:
            self.__dict__[attr_name] = attr_value

