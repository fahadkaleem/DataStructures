"""
Author: Mohammed Fahad Kaleem

Problem: Insert a Node in a Sorted Linked List

Method:
1. Traverse the list to find the appropriate position
2. Insert the node in that position
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

    def insert_node_in_sorted_linked_list(self,data):
        new_node = Node(data)
        current_node = self.head
        previous_node = None
        running = True
        while current_node:
            if current_node.get_data() < new_node.get_data():
                previous_node = current_node
                current_node = current_node.get_next_node()
            else:
                running = False
        new_node.set_next_node(current_node)
        previous_node.set_next_node(new_node)


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(5)
    linked_list.insert_node_in_sorted_linked_list(4)
    linked_list.print_linked_list()
