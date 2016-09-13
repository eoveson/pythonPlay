class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, node):
        if not node: return
        if self.head is None:
            self.head = node
        elif node.val < self.head.val:
            node.next = self.head
            self.head = node
        else:
            nodeT = self.head
            while nodeT.next and nodeT.next.val < node.val:
                nodeT = nodeT.next
            node.next = nodeT.next
            nodeT.next = node

    def printList(self):
        nodeT = self.head
        while nodeT:
            print(nodeT.val)
            nodeT = nodeT.next

ll = LinkedList()
node1 = Node(2)

ll.insertNode(node1)
node1 = Node(5)
ll.insertNode(node1)
ll.insertNode(Node(7))
ll.insertNode(Node(10))
ll.insertNode(Node(15))
ll.printList()