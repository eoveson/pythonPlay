class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self):
        self.root = None
    def AddNode(self, val):
        curNode = self.root
        if curNode is None:
            self.root = Node(val)
            return
        while curNode.next is not None:
            curNode = curNode.next
        curNode.next = Node(val)
    def Print(self):
        curNode = self.root
        while curNode is not None:
            print(curNode.val)
            curNode = curNode.next
        print()
    def DelNode(self, val):
        curNode = self.root
        if curNode.val == val:
            self.root = curNode.next
            del curNode
            return
        while curNode.next is not None and curNode.next.val != val:
            curNode = curNode.next
        if curNode is not None and curNode.next.val == val:
            nodeT = curNode.next
            curNode.next = curNode.next.next
            del nodeT
    def DelTree(self):
        curNode = self.root
        while curNode is not None:
            nodeT = curNode
            curNode = curNode.next
            del nodeT
        self.root = None

ll = LinkedList()
ll.AddNode(2)
ll.AddNode(11)
ll.AddNode(3)
ll.AddNode(15)
ll.Print()
ll.DelTree()
ll.Print()
