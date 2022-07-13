#!/usr/bin/python3
"""student module.
"""


class Student:
    """class Student."""

    def __init__(self, first_name, last_name, age):
        """Creates an instance.

        Args:
            first_name (str): the firstname of the student
            last_name (str): the lastname of the student
            age (int): the age of the student

        Returns:
            Always nothing.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): list of attributes that must be retrieved

        Returns:
            (dict): a dictionary representation of a student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
