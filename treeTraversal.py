class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def preOrderTraverse(tree):
    if tree:
        print(tree.val)
        preOrderTraverse(tree.left)
        preOrderTraverse(tree.right)

def inOrderTraverse(tree):
    if not tree: return
    inOrderTraverse(tree.left)
    print(tree.val)
    inOrderTraverse(tree.right)

def postOrderTraverse(tree):
    if not tree: return
    postOrderTraverse(tree.left)
    postOrderTraverse(tree.right)
    print(tree.val)

def breadthFirst(tree):
    queue = []
    queue.append(tree)
    while len(queue) > 0:
        node1 = queue.pop(0)
        print(node1.val)
        if node1.left is not None:
            queue.append(node1.left)
        if node1.right is not None:
            queue.append(node1.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(8)

#preOrderTraverse(root)
#inOrderTraverse(root)
#postOrderTraverse(root)

breadthFirst(root)