# Time: O(n)


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def level_order_traversal(root):
    if root is None:
        return None
    node_list = []
    node_list.append(root)
    while len(node_list) > 0:
        print(node_list[0].data,end=" ")
        node = node_list.pop(0)
        if node.left is not None:
            node_list.append(node.left)
        if node.right is not None:
            node_list.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
level_order_traversal(root)
