class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def level_order_traversal(root):
    if root is None:
        return None
    nodeList = []
    nodeList.append(root)
    while len(nodeList) > 0:
        print(nodeList[0].data,end=" ")
        node = nodeList.pop(0)
        if node.left is not None:
            nodeList.append(node.left)
        if node.right is not None:
            nodeList.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
level_order_traversal(root)
