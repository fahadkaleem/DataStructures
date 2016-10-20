"""
Author: Mohammed Fahad Kaleem


Problem: Find the nth node from the end of Linked List

Method:
"""


class Node:
    def __init__(self,data,next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data = data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self,next_node):
        self.next_node = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self,data):
        new_node = Node(data)
        if self.length==0:
            self.head = new_node
            self.length += 1
        else:
            current_node = self.head
            while current_node.get_next_node() is not None:
                current_node = current_node.get_next_node()
            current_node.set_next_node(new_node)
            self.length += 1

    def print_linked_list(self):
        if self.length == 0:
            print("Linked List is empty")
        else:
            current_node = self.head
            while current_node:
                print("[%s]"%current_node.get_data(),end=" ==> ")
                current_node = current_node.get_next_node()
            print()
