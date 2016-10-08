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

    def insert_at_position(self,position,data):
        node_to_be_inserted = Node(data,None,None)
        if self.length == 0:
            self.insert_head(data)
            return
        elif position > 0:
            current_node = self.get_node_at_nth_position(position)
            if current_node is None or current_node.get_next_node() is None:
                self.insert_tail(data)
            else:
                node_to_be_inserted.set_next_node(current_node.get_next_node())
                current_node.get_next_node().set_previous_node(node_to_be_inserted)
                current_node.set_next_node(node_to_be_inserted)
                node_to_be_inserted.set_previous_node(current_node)
        else:
            self.insert_head(data)

    def delete_head(self):
        if self.length == 0:
            return None
        else:
            self.head.get_next_node().set_previous_node(None)
            self.head = self.head.get_next_node()

    def delete_tail(self):
        if self.length == 0:
            return None
        else:
            current_node = self.head
            while current_node.get_next_node() is not None:
                current_node = current_node.get_next_node()
            current_node.get_previous_node().set_next_node(None)

    def delete_at_nth_position(self,position):
        if self.length == 0:
            print("Linked list is empty")
            return None
        elif 0 < position < self.length:
            current_node = self.get_node_at_nth_position(position)
            if current_node:
                current_node.get_previous_node().set_next_node(current_node.get_next_node())
                current_node.get_next_node().set_previous_node(current_node.get_previous_node())

    def delete_node_with_data(self,data):
        if self.length == 0:
            return None
        if self.head.get_data() == data:
            self.head.get_next_node().set_previous_node(None)
            self.head = self.head.get_next_node()
            return True
        if self.tail.get_data() == data:
            self.tail.get_previous_node().set_next_node(None)
            self.tail = self.tail.get_previous_node()
            return True
        current_node = self.head
        while current_node is not None:
            if current_node.get_data() == data:
                if current_node.get_next_node() is not None:
                    current_node.get_previous_node().set_next_node(current_node.get_next_node())
                    current_node.get_next_node().set_previous_node(current_node.get_previous_node())
                    return True
            current_node = current_node.get_next_node()
        return False

    def get_node_at_nth_position(self,position):
        if self.length == 0:
            return None
        count = 0
        current_node = self.head
        while count<position and current_node.get_next_node() is not None:
            current_node =  current_node.get_next_node()
            if current_node.get_next_node() is None:
                break
            count += 1
        return current_node

    def print_linkedlist(self):
        if self.length == 0:
            print("Linked List Empty")
        else:
            current_node = self.head
            while current_node is not None:
                print('[%s]'%current_node.get_data(),end=' <===> ')
                current_node = current_node.get_next_node()
            print('X')

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_head(45)
    dll.insert_head(33)
    dll.insert_tail(46)
    dll.insert_tail(47)
    dll.insert_tail(48)
    dll.insert_at_position(2,13)
    dll.insert_at_position(3,15)
    dll.insert_at_position(15,90)
    dll.insert_at_position(-1,12)
    dll.delete_node_with_data(45)
    dll.print_linkedlist()




