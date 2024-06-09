class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self, value):
        node1 = Node(value)
        self.head = node1
        self.tail = node1
        self.length = 1

# Empty Linked list
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0


linkedlsit1 = Linkedlist(20)
print(linkedlsit1.tail.value)

