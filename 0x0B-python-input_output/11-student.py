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

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json (stream): a dictionary containing the
                new value of attributes.

        Returns:
            the modified instance
        """
        # instance attributes
        try:
            self.first_name = json['first_name']
        except Exception:
            pass
        try:
            self.last_name = json['last_name']
        except Exception:
            pass
        try:
            self.age = json['age']
        except Exception:
            pass
