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