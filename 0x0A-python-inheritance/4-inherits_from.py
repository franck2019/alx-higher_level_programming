#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """Returns True if the object is exactly an instance of
    a class that inherited (directly or indirectly) from the
    specified class ; otherwise False.

    Args:
        obj (:obj): an object
        a_class: a class
    
    N.B: if an oject is an instance of a class that inherited from,
    that means the type of this object is different from the class
    """
    return False if type(obj) is a_class else issubclass(type(obj), a_class)
