from random import randint


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, elements=None):
        self.head = None
        self.tail = None
        self.length = 0
        if elements is not None:
            self.add_elements(elements)

    # Print the linked list
    def __print__(self):
        current = self.head
        linked_list = []
        while (current):
            linked_list.append(str(current.data))
            current = current.next
        print(' --> '.join(linked_list))

    # Randomly generate a linked list
    def __generate__(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.insert(randint(min_value, max_value))
        return self

    # Insert at tail
    def insert(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.length += 1
        return self.tail

    # Insert at head
    def insert_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self.head

    # Insert at tail
    def insert_tail(self, value):
        new_node = LinkedList(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            #new_node = self.tail
            self.tail = new_node
        self.length += 1
        return self.tail

    # Insert at a given position
    def insert_at_position(self, position, data):
        new_node = Node(data)
        if position > self.length:
            return None
        elif position == 0:
            self.insert_head(data)
        elif position == self.length:
                self.tail.next = new_node
        else:
            current = self.head
            count = 0
            while count < position -1:
                count += 1
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # Insert to Linked List from a List
    def insert_multiple(self, values):
        for i in values:
            self.insert(i)

    # Delete Head
    def delete_head(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.length -= 1

    # Delete the tail
    def delete_tail(self):
        if self.head is None:
            return
        current = self.head
        previous = self.head
        while current.next:
            previous = current
            current = current.next
        previous.next = None
        self.tail = previous.next
        self.length -= 1

    # Delete from Linked List with a node with given data
    def delete_given_node(self,data):
        if self.length == 0:
            return
        current = self.head
        previous = None
        while current:
            if current.data == data:
                previous.next = current.next
            previous = current
            current = current.next
        self.length -= 1

   # Delete the entire Linked List
    def delete_linked_list(self):
        self.head = None


linked_list = LinkedList()
linked_list.__generate__(10,0,9)
linked_list.__print__()
linked_list.delete_linked_list()
linked_list.__print__()