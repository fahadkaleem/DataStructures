"""
The following is the implementation of Singly Linked List in python
Author: Mohammed Fahad Kaleem
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.nextNode = next

    def set_data(self, data):
        """
        Method to set data for a node
        Argument:
        :param data: data for a node
        Return:
        :return: None
        """
        self.data = data

    def get_data(self):
        """
        Method to get data for a node
        :return: Data
        """
        return self.data

    def set_next(self, next):
        """
        Method to set next node for a node
        :param next: next node
        :return: None
        """
        self.nextNode = next

    def get_next(self):
        """
        Method to get the next node for a node
        :return: Next node
        """
        return self.nextNode

    def has_next(self):
        """
        Method to check if the present node has a next node or not
        :return: True if there is a next node, False if there is no next node
        :rtype: Boolean
        """
        return self.nextNode is not None


class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def list_length(self):
        """
        Method to return the length of a given Linked List
        :var current_node: The Node being processed
        :var length: Variable to store the length of the linked list
        :return:
        """
        current_node = self.head
        length = 0

        while current_node.has_next:
            length += 1
            current_node = current_node.get_next()
        return length

    """
    Methods to Insert nodes in a Linked List:
    # insertNode: Use this method to simply insert a node to the Linked List
    # insertHead: Use this method to insert a node at the head of the Linked List
    # insertTail: Use this method to insert a node at the tail of the Linked List
    # insertAtPosition: Use this method to insert a node at a particular position of the Linked List
    """

    def insert_node(self, data):
        """
        Method to insert a node to the Linked List
        :param node: Node to be inserted
        :return: None
        """
        if self.length == 0:
            self.insert_head(data)
        else:
            self.insert_tail(data)

    def insert_head(self, data):
        """
        Method to add a node at the beginning of the list
        :param data: the data of the node to be inserted
        :return: None
        """
        node_to_be_inserted = Node(data)
        if self.length == 0:
            self.head = node_to_be_inserted
        else:
            node_to_be_inserted.set_next(self.head)
            self.head = node_to_be_inserted
        self.length += 1

    def insert_tail(self, data):
        """
        Method to insert a node at the end of the Linked List
        :param data: Data of the node to be inserted
        :return: None
        :var current_node: The node being processed
        :var length: The variable that holds the length of the Linked List
        """
        node_to_be_inserted = Node(data)
        current_node = self.head

        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        current_node.set_next(node_to_be_inserted)
        self.length += 1

    def insertAtPosition(self, data, position):
        """
        Method to insert a node at a given position
        :param data: Data of the new node which has to be inserted
        :param position: Position in the Linked List where the new node has to be inserted
        :var current_node: Node that is being processed
        :var count: Count variable
        :return: None
        """
        if position > self.length or position < 0:
            print("Invalid position!, The size of the Linked List is:%s" % self.length)
        else:
            if position == 0:
                self.insert_head(data)
            else:
                node_to_be_inserted = Node(data)
                current_node = self.head
                count = 0
                while count < position - 1:
                    current_node = current_node.get_next()
                    count += 1
                node_to_be_inserted.set_next(current_node.get_next())
                current_node.set_next(node_to_be_inserted)
                self.length += 1

    def print_linkedlist(self):
        if self.length == 0:
            print("Linked List is empty")
        else:
            current = self.head
            #linkedlist = []
            while current is not None:
                #linkedlist.append(current.get_data())
                print(' [%s] =====>' % current.get_data(), end='')
                current = current.get_next()
        print('[X]')

    def delete_head(self):
        if self.length == 0:
            print("Linked List is Empty")
        else:
            self.head = self.head.get_next()
            self.length -= 1

    def delete_tail(self):
        if self.length == 0:
            print("Linked List is Empty")
        else:
            current = self.head
            while current.get_next().get_next() is not None:
                current = current.get_next()
            current.set_next(None)

    def delete_node_by_position(self, position):
        if self.is_empty():
            print("Linked List is Empty")
        elif position > self.length:
            print("Invalid position")
        elif position == self.length:
            self.delete_tail()
        elif position == 0:
            self.delete_head()
        else:
            count = 0
            current = self.head
            while count < position - 1:
                current = current.get_next()
                count += 1
            current.set_next(current.get_next().get_next())

    def delete_node_by_data(self, data):
        if self.is_empty():
            print("Linked List is empty")
        else:
            current = self.head
            while current.get_next() is not None and current.get_next().get_data() != data:
                current = current.get_next()
            current.set_next(current.get_next().get_next())

    def is_empty(self):
        if self.length == 0:
            return True
        return False

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_node(1)
    ll.insert_node(2)
    ll.insert_node(3)
    ll.insert_node(4)
    ll.print_linkedlist()
