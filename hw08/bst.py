class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
         
class BinarySearchTree:
    def __init__(self):
        self.head = None
 
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = Node(value)
                        return
                    elif current_node.left:
                        current_node = current_node.left
                        continue
                if value > current_node.value:
                    if current_node.right is None:
                        current_node.right = Node(value)
                        return
                    elif current_node.right:
                        current_node = current_node.right
                        continue
 
    def fromArray(self, array):
        for added_node in array:
            self.insert(added_node)
 
    def search(self, value):
        self.visited_nodes = 0
        current_node = self.head
        while current_node:
            self.visited_nodes += 1
            if current_node.value == value:
                return True
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return False
 
    def min(self):
        self.visited_nodes = 1
        current_node = self.head
        while current_node:
            if current_node.left is None:
                return current_node.value
            current_node = current_node.left
            self.visited_nodes += 1
 
    def max(self):
        self.visited_nodes = 1
        current_node = self.head
        while current_node:
            if current_node.right is None:
                return current_node.value
            current_node = current_node.right
            self.visited_nodes += 1
 
    def visitedNodes(self):
        return self.visited_nodes