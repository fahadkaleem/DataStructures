"""
Author: Mohammed Fahad Kaleem


Problem: Find the nth node from the end of Linked List

Method:
Maintain two pointers
1. Reference pointer and main pointer.
2. Initialize both reference and main pointers to head.
3. First move reference pointer to n nodes from head.
4. Move both pointers one by one until reference pointer reaches end.
5. Main pointer will point to nth node from the end. Return main pointer.
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        new_node = Node(data)
        if self.length == 0:
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
                print("[%s]" % current_node.get_data(), end=" ==> ")
                current_node = current_node.get_next_node()
            print()

    def nth_node(self,n):
        if self.length == 0:
            print("Linked List is empty")
            return False
        reference_pointer = self.head
        main_pointer = self.head
        nth_node = self.length - n +1
        if nth_node > self.length:
            print("Value of n is greater than length of the Linked List")
            return False
        for i in range(nth_node + 1):
            reference_pointer = reference_pointer.get_next_node()
        while reference_pointer:
            reference_pointer = reference_pointer.get_next_node()
            main_pointer = main_pointer.get_next_node()
        print(main_pointer.get_data())
        return main_pointer.get_data()

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(12)
    linked_list.insert(16)
    linked_list.insert(3)
    linked_list.insert(15)
    linked_list.print_linked_list()
    linked_list.nth_node(0)
