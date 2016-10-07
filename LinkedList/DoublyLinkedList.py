class Node:
    def __init__(self,data=None, next_node=None, previous_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node

    def set_data(self,data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_previous_node(self, previous_node):
        self.previous_node = previous_node

    def get_previous_node(self):
        return self.previous_node


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def insert_head(self, data):
        node_to_be_inserted = Node(data,None,None)
        if self.length == 0:
            self.head = node_to_be_inserted
            self.tail = node_to_be_inserted
            self.length += 1
        else:
            node_to_be_inserted.set_previous_node(None)
            node_to_be_inserted.set_next_node(self.head)
            self.head.set_previous_node(node_to_be_inserted)
            self.head = node_to_be_inserted
            self.length += 1

    def insert_tail(self,data):
        node_to_be_inserted = Node(data,None,None)
        if self.length == 0:
            self.head = node_to_be_inserted
            self.tail = node_to_be_inserted
            self.length += 1
        else:
            current_node = self.head
            while current_node.get_next_node() is not None:
                current_node = current_node.get_next_node()
            current_node.set_next_node(node_to_be_inserted)
            node_to_be_inserted.set_previous_node(current_node)
            self.tail = current_node.get_next_node()

    def print_linkedlist(self):
        if self.length == 0:
            print("Linked List Empty")
        else:
            current_node = self.head
            while current_node is not None:
                print('[%s]'%current_node.get_data(),end=' <===> ')
                current_node = current_node.get_next_node()
            print('X')



dll = DoublyLinkedList()
dll.insert_head(45)
dll.insert_head(33)
dll.insert_tail(46)
dll.insert_tail(47)
dll.insert_tail(48)
dll.print_linkedlist()




