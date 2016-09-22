"""
The following is the implementation of Singly Linked List in python
Author: Mohammed Fahad Kaleem
"""

class Node:

    def __init__(self,data,next=None):
        self.data = data
        self.nextNode = next

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
        self.nextNode = next

    def getNext(self):
        """
        Method to get the next node for a node
        :return: Next node
        """
        return self.nextNode

    def hasNext(self):
        """
        Method to check if the present node has a next node or not
        :return: True if there is a next node, False if there is no next node
        :rtype: Boolean
        """
        return self.nextNode != None


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

    def insertNode(self,data):
        """
        Method to insert a node to the Linked List
        :param node: Node to be inserted
        :return: None
        """
        if self.length == 0:
            self.insertHead(data)
        else:
            self.insertTail(data)

    def insertHead(self, data):
        """
        Method to add a node at the beginning of the list
        :param data: the data of the node to be inserted
        :return: None
        """
        nodeToBeInserted = Node(data)
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
        nodeToBeInserted = Node(data)
        currentNode = self.head

        while currentNode.getNext() != None:
            currentNode = currentNode.getNext()
        currentNode.setNext(nodeToBeInserted)
        self.length = self.length + 1

    def insertAtPosition(self, data, position):
        """
        Method to insert a node at a given position
        :param data: Data of the new node which has to be inserted
        :param position: Position in the Linked List where the new node has to be inserted
        :var currentNode: Node that is being processed
        :var count: Count variable
        :return: None
        """
        if position > self.length or position < 0:
            print("Invalid position!, The size of the Linked List is:%s" % self.length)
        else:
            if position == 0:
                self.insertHead(data)
            else:
                nodeToBeInserted = Node(data)
                currentNode = self.head
                count = 0
                while count < position - 1:
                    currentNode = currentNode.getNext()
                    count = count + 1
                nodeToBeInserted.setNext(currentNode.getNext())
                currentNode.setNext(nodeToBeInserted)
                self.length = self.length + 1

    def printLinkedList(self):
        if self.length == 0:
            print("Linked List is empty")
        else:
            current = self.head
            linkedlist = []
            while current!=None:
                linkedlist.append(current.getData())
                print(' [%s] =====>'%current.getData(),end='')
                current = current.getNext()
        print('[X]')

    def deleteHead(self):
        if self.length == 0:
            print("Linked List is Empty")
        else:
            self.head = self.head.getNext()
            self.length = self.length - 1

    def deleteTail(self):
        if self.length == 0:
            print("Linked List is Empty")
        else:
            current = self.head
            while current.getNext().getNext() != None:
                current = current.getNext()
            current.setNext(None)

    def deleteNodeByPosition(self, position):
        if self.isEmpty():
            print("Linked List is Empty")
        elif position>self.length:
            print("Invalid position")
        elif position == self.length:
            self.deleteTail()
        elif position == 0:
            self.deleteHead()
        else:
            count = 0
            current = self.head
            while count < position-1:
                current = current.getNext()
                count = count + 1
            current.setNext(current.getNext().getNext())

    def deleteNodeByValue(self,data):
        if self.isEmpty():
            print("Linked List is empty")
        else:
            current = self.head
            while current.getNext()!=None and current.getNext().getData()!= data:
                current = current.getNext()
            current.setNext(current.getNext().getNext())

    def isEmpty(self):
        if self.length==0:
            return True
        return False




ll = LinkedList()
ll.insertNode(1)
ll.insertNode(2)
ll.insertNode(3)
ll.insertNode(4)
ll.printLinkedList()

