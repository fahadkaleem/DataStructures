"""
Author: Mohammed Fahad Kaleem
"""


class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right


