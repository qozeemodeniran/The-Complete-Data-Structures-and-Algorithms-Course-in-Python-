# node class - empty node 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# empty linked list: head and tail nodes point to None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # creating a method to print the proper linkedliat to the console using the __str__ merthod
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result  
    
    # implementing the Append logic
    def append(self, value):
        
        # How do we identify an empty linkedlist? - when both the Head and Tail points to None or if the length atribute we have delcared is 0!
        
        # creating a new node object  using the Node() class
        new_node = Node(value)

        # check if the linkedlis is empty (using the condition if self.head points to None), if true, then make a new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            # at this point, we have successfull create alogin to append a new node to an empty linkedlist.

        else: # if the linkedlist is not empty, access the tail, access the next pointer of the last node and make it point to the last (new) node
            self.tail.next = new_node
            self.tail = new_node

            # we need to increate the lenght of the linkedlist as we've created a new node:
        self.length += 1 
        # next is to add the new element(node) to the end the linkedlist - Append >> see the `else` block above
   
# created object of the LinkedList and call the append merthod
linkedlist = Linkedlist()
linkedlist.append(5)
linkedlist.append(10)
print(linkedlist)
