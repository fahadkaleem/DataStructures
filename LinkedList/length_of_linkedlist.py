from LinkedList import LinkedList


def length_of_linkedlist(ll):
    if ll.head is None:
        return 0
    current = ll.head
    count = 0
    while current:
        current = current.next
        count += 1
    return count

linked_list = LinkedList()
linked_list.__generate__(10,0,9)
linked_list.__print__()
print(length_of_linkedlist(linked_list))