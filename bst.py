import collections

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def Insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        curNode = self.root
        while curNode:
            if val < curNode.val:
                if curNode.left is None:
                    curNode.left = Node(val)
                    return
                curNode = curNode.left
            else:
                if curNode.right is None:
                    curNode.right = Node(val)
                    return
                curNode = curNode.right

    def InOrder(self, node):
        if node is None:
            return
        self.InOrder(node.left)
        print(node.val)
        self.InOrder(node.right)

    def PreOrderIter(self, node):
        s = [node]
        while s != []:
            nodeCur = s.pop()
            print(nodeCur.val)
            if nodeCur.right:
                s.append(nodeCur.right)
            if nodeCur.left:
                s.append(nodeCur.left)

    def Find(self, val):
        curNode = self.root
        while curNode is not None:
            if curNode.val == val:
                print("found it")
                return
            if val < curNode.val:
                curNode = curNode.left
            else:
                curNode = curNode.right

    def MaxHeight(self, node):
        if node is None: 
            return 0
        return 1+max(self.MaxHeight(node.left), self.MaxHeight(node.right))
               
bst = BST()
bst.Insert(5)
bst.Insert(2)
bst.Insert(3)
bst.Insert(7)
bst.Insert(9)
bst.Insert(1)
#print(bst.MaxHeight(bst.root))
bst.PreOrderIter(bst.root)