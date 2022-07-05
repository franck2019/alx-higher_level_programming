#!/usr/bin/python3
""" my_list module."""


class MyList(list):
    """class MyList"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)."""
        temp = self.copy()
        temp.sort()
        print(temp)
