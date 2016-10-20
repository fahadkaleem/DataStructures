# Linked List 
Linkedlist is a linear collection of data elements called "Nodes". Each node consists of data and a pointer to the next node. 

### Time complexity cheat sheet

|Linked List Type|Access|Search|Insertion|Deletion|Access|Search|Insertion|Deletion|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Singly|Θ(n)|Θ(n)|Θ(1)|Θ(1)|O(n)|O(n)|O(1)|O(1)|O(n)|
|Doubly|Θ(n)|Θ(n)|Θ(1)|Θ(1)|O(n)|O(n)|O(1)|O(1)|O(n)|

### Advantages
1. Linked lists can grow and shrink during execution.  
2. Insertion and deletion node operations are easily implemented in a linked list.
3. Linked list can be used to implement data structures such as stacks and queues.
4. Unlike arrays, there is no need to define an initial size for a linked list 
5. Items can be added or removed from the middle of list.
 
### Disadvantages
1. They use more memory than arrays because of the storage used by their pointers.
2. Nodes in a linked list must be read in order from the beginning as linked lists are inherently sequential access.
3. Nodes are stored incontiguously, greatly increasing the time required to access individual elements within the list, especially with a CPU cache.
4. Difficulties arise in linked lists when it comes to reverse traversing. For instance, singly linked lists are cumbersome to navigate backwards and while doubly linked lists are somewhat easier to read, memory is wasted in allocating space for a back-pointer.

### Definitions:
1. **Head:** The first element in the linked list is called the head of the linked list
2. **Tail:** The last element in the linked list is called the tail of the linked list

## [ Singly Linked List ](https://github.com/fahadkaleem/DataStructures/blob/master/LinkedList/Implementation/SinglyLinkedList.py)
Singly Linked List is a linked list where every element points to the next element of the list. Here the navigation of items is forward only.

|   |Operations|
|---|:---|
|1. |Length of Linked List|
|2. |Insert node at head|
|3. |Insert node at tail|
|4. |Insert node at position|
|5. |Print Linked List|
|6. |Delete node at head|
|7. |Delete node at tail|
|8. |Delete node at nth position|
|9. |Delete node by Data|

## [ Doubly Linked List ](https://github.com/fahadkaleem/DataStructures/blob/master/LinkedList/Implementation/DoublyLinkedList.py)
Doubly Linked List is a linked list where every element points to the next element and the previous element of the list. Here the navigation of the items is forward and backward.  

|   |Operations|
|---|:---|
|1.| Insert node at Head|
|2.| Insert node at Tail|
|3.| Insert at position|
|4.| Delete node at Head|
|5.| Delete node at Tail|
|6.| Delete a Node by Data|
|7.| Delete a Node on nth position|
|8.| Get node at nth position|
|9.| Print Double linked list|

## [ Circular Linked List ](https://github.com/fahadkaleem/DataStructures/blob/master/LinkedList/Implementation/CircularLinkedList.py) 
Circular Linked List is a linked list where the last element(tail) points to the first element(head).
 
|   |Operations|
|---|:---|
|1.| Insert node at Head|
|2.| Insert node at Tail|
|3.| Insert at position|
|4.| Delete node at Head|
|5.| Delete node at Tail|
|6.| Length of the linked list|

## Problems
Following is a list of problems which have been solved, you can find the solutions to these problems in the "Problems" directory

|   |Problem|Approach|Time Complexity|Space Complexity|Status|
|---|:---|:---:|:---:|:---:|:---:|
|1.|Implement Stack using Linked List|Linked List|||Not solved|
|2.|[Find nth node from the end of a Linked List](https://github.com/fahadkaleem/DataStructures/blob/master/LinkedList/Problems/nthNodeFromEndOfLinkedList/Solution1.py)|Length|**O(n)** where n is the length of linked list||Solved|
|3.|Find nth node from the end of Linked List|Two Pointers|||Not solved|
