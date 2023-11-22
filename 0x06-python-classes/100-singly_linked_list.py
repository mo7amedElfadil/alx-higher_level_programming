#!/usr/bin/python3
"""Defines a node class of a singly linked list"""


class Node:
    """definition of Node class
    Args:
        data (int) Optional
        next_node (Node) Optional, None by default

    Attributes:
        data (int, private): integer value to be stored in node
        next_node (node, private): pointer to next node in list or None

    Methods:
        data: property getter and setter
        next_node: property getter and setter

    """
    def __init__(self, data, next_node=None):
        """initialize instance of Node class
        Args:
            data: integer value to be stored in node
            next_node: points to next node in list or None
        Attributes:
            data: integer value of node
            next_node: pointer to next node in list

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data property"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter for data property
        if data is not integer --> raise TypeError
        msg : data must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for next_node property"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defines a SinglyLinkedList class"""


class SinglyLinkedList:
    """definition of SinglyLinkedList class
    Args:
        None

    Attributes:
        head (Node, private): pointer to the head of the list,
            starts as None
        next_node (node, private): pointer to next node in list or None

    Methods:
        sorted_insert: insert a new Node into correct sorted position
            (Ascending order)
    """

    def __init__(self):
        """initialise SinglyLinkedList instance
            instantiates head privated attribute as None
        """
        self.__head = None

    def __str__(self):
        """private method to define printing format
            list of ints is converted to list of strings and
            a string of these string formatted numbers
            is joined by a newline and returned
        """
        result = []
        node = self.__head
        while node:
            result.append(str(node.data))
            node = node.next_node
        return ("\n".join(result))

    def sorted_insert(self, val):
        """Public method that inserts a new Node into the correct
        sorted position in the list
        """
        if not self.__head:
            self.__head = Node(val, self.__head)
        elif self.__head.data > val:
            self.__head = Node(val, self.__head)
        else:
            self.recursive_add(val, self.__head)
            # cur = self.__head
            # while cur.next_node and cur.next_node.data < val:
            #     cur = cur.next_node
            # cur.next_node = Node(val, cur.next_node)

    def recursive_add(self, val, node):
        if node.next_node and node.next_node.data < val:
            self.recursive_add(val, node.next_node)
        else:
            node.next_node = Node(val, node.next_node)


