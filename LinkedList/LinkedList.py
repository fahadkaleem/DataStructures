from random import randint


class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, elements=None):
        self.head = None
        self.tail = None
        if elements is not None:
            self.add_elements(elements)

    def __print__(self):
        current = self.head
        linked_list = []
        while (current):
            linked_list.append(str(current.data))
            current = current.next
        print(' --> '.join(linked_list))

    def insert(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def insert_head(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return self.head

    def insert_tail(self, value):
        new_node = LinkedList(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            #new_node = self.tail
            self.tail = new_node
        return self.tail

    def insert_multiple(self, values):
        for i in values:
            self.insert(i)

    def __generate__(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.insert(randint(min_value, max_value))
        return self
