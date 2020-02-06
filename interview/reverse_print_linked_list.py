class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

LLNode1 = Node(1)
LLNode2 = Node(2)
LLNode3 = Node(3)
LLNode4 = Node(4)
LLNode5 = Node(5)
LLNode6 = Node(6)
LLNode7 = Node(7)

LLNode1.next = LLNode2
LLNode2.next = LLNode3
LLNode3.next = LLNode4
LLNode4.next = LLNode5
LLNode5.next = LLNode6
LLNode6.next = LLNode7
LLNode7.next = None



if __name__ == "__main__":
    node = LLNode1
    node.previous = None
    while node.next is not None:
        node.next.previous = node
        node = node.next 
    while node is not None:
        print(node.data)
        node = node.previous
