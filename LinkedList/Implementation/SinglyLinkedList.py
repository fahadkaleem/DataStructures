"""
The following is the implementation of Singly Linked List in python
Author: Mohammed Fahad Kaleem
"""

class Node:

    def __init__(self):
        self.data = None
        self.next = Node

    def setData(self,data):
        """
        Method to set data for a node

        Argument:
        :param data: data for a node

        Return:
        :return: None
        """
        self.data = data

    def getData(self):
        """
        Method to get data for a node
        :return: Data
        """
        return self.data

    def setNext(self,next):
        """
        Method to set next node for a node
        :param next: next node
        :return: None
        """
        self.next = next

    def getNext(self):
        """
        Method to get the next node for a node
        :return: Next node
        """
        return self.next

    def hasNext(self):
        """
        Method to check if the present node has a next node or not
        :return: True if there is a next node, False if there is no next node
        :rtype: Boolean
        """
        return self.next!=None


class LinkedList(object):

    def __init__(self):
        self.length = 0
        self.head = None

    def listLength(self):
        """
        Method to return the length of a given Linked List
        :var currentNode: The Node being processed
        :var length: Variable to store the length of the linked list
        :
        :return:
        """
        currentNode = self.head
        length = 0

        while currentNode.hasNext:
            length = length + 1
            currentNode = currentNode.getNext()
        return length

    """
    Methods to Insert nodes in a Linked List:
    # insertNode: Use this method to simply insert a node to the Linked List
    # insertHead: Use this method to insert a node at the head of the Linked List
    # insertTail: Use this method to insert a node at the tail of the Linked List
    # insertAtPosition: Use this method to insert a node at a particular position of the Linked List
    """

    def insertNode(self,node):
        """
        Method to insert a node to the Linked List
        :param node: Node to be inserted
        :return: None
        """
        if self.length == 0:
            self.insertHead(node)
        else:
            self.insertTail(node)

    def insertHead(self, data):
        """
        Method to add a node at the beginning of the list
        :param data: the data of the node to be inserted
        :return: None
        """
        nodeToBeInserted = Node()
        nodeToBeInserted.setData(data)
        if self.length == 0:
            self.head = nodeToBeInserted
        else:
            nodeToBeInserted.setNext(self.head)
            self.head = nodeToBeInserted
        self.length = self.length + 1

    def insertTail(self,data):
        """
        Method to insert a node at the end of the Linked List
        :param data: Data of the node to be inserted
        :return: None
        :var currentNode: The node being processed
        :var length: The variable that holds the length of the Linked List
        """
        nodeToBeInserted = Node()
        nodeToBeInserted.setData(data)
        currentNode = self.head

        while currentNode.getNext() != None:
            currentNode = currentNode.getNext()
        currentNode.setNext(nodeToBeInserted)
        self.length = self.length + 1

    def insertAtPosition(self,data, position):
        """
        Method to insert a node at a given position
        :param data: Data of the new node which has to be inserted
        :param position: Position in the Linked List where the new node has to be inserted
        :var currentNode: Node that is being processed
        :var count: Count variable
        :return: None
        """
        if position > self.length or position < 0:
            print("Invalid position!, The size of the Linked List is:%s"%self.length)
        else:
            if position ==0:
                self.insertHead(data)
            else:
                nodeToBeInserted = Node()
                nodeToBeInserted.setData(data)
                currentNode = self.head
                count = 0
                while count < position - 1:
                    currentNode = currentNode.getNext()
                    count = count + 1
                nodeToBeInserted.setNext(currentNode.getNext())
                currentNode.setNext(nodeToBeInserted)
                self.length = self.length+1

    """
    Methods to Delete nodes from a Linked List

    """