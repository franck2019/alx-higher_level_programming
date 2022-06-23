#!/usr/bin/python3

"""This module defines a singly linked list Data Structures."""


class Node:
    """This class defines a node of a singly linked

    Attributes:
            __data (int): The data of the node.
                It mus be an integer, otherwise raise a TypeError
                with the message `data must be an integer`.
            __next_node (Node): The next node of the current.
                It can be None or must be a Node, otherwise raise a
                TypeError exception msg = next_node must be a Node object.
    """

    def __init__(self, data, next_node=None):
        """Instanciates a Node.

        Args:
            data (int): The data node
            next_node (Node): The next node
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        self.__data = data

        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = next_node

    @property
    def data(self):
        """Retrieve the data node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the new value of the data node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the value of the next node.

        Args:
            value (:obj:`Node`): The new value of the next node.
        """
        if value and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """this class defines a singly linked list

    Attributes:
              __head: The head of the linked list.
    """
    def __init__(self):
        """Instanciate the singly linked list."""
        self.__head = None

    def __str__(self):
        """Printable version of a singly linked list."""
        result = ""
        current = self.__head

        while current is not None:
            if current.next_node is not None:
                result += "{:d}\n".format(current.data)
            else:
                result += "{:d}".format(current.data)
            current = current.next_node

        return result

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position
        in the list (increasing order).

        Args:
            value: The data value of the node
        """
        new = Node(value, None)

        if self.__head is None:
            self.__head = new
        else:

            prev = None
            current = self.__head

            while current is not None and current.data < new.data:
                prev = current
                current = current.next_node

            if prev is None:
                new.next_node = current
                self.__head = new
            else:
                prev.next_node = new
                new.next_node = current
