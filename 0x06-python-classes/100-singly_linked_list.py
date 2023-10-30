#!/usr/bin/python3
"""Class Node that defines a singly linked list"""


class Node:
    """Represents a singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defines a singly linked list"""


class SinglyLinkedList:
    """Represents a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node in the correct sorted position in the list"""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self) -> str:
        """Prints the entire list, one node number by line"""
        result = []
        temp = self.__head
        while temp is not None:
            result.append(str(temp.data))
            temp = temp.next_node
        return ("\n".join(result))
