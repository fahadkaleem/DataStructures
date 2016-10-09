"""
Author: Mohammed Fahad Kaleem
"""


class Node:
    def __init__(self):
        self.data = None
        self.next_node = None

    def set_data(self,data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next_node(self,next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node


class CircularLinkedList(object):
    def __init__(self):
        self.head = None
        self.length = None

    def circular_linkedlist_length(self):
        if self.length == 0:
            print("Linked List is empty")
            return None
        else:
            current_node = self.head
            while current_node.get_next_node() is not self.head:
                current_node = current_node.get_next_node()
                self.length += 1
        return self.length

    def print_circular_linkedlist(self):
        if self.length == 0:
            print("Linkedlist empty")
            return None
        else:
            current_node = self.head
            while current_node.get_next_node() is not self.head:
                print('[%s]'%current_node.get_data(),end=' ===>')
                current_node = current_node.get_next_node()

    def insert_head(self,data):
        node_to_be_inserted = Node().set_data(data)

