#Python Data Structures
#Python has a number of built-in data structures that you can use to store collections of data.

#Linked Lists
#Linked lists are a data structure that store a sequence of data elements, 
#   each of which is connected to the next element in the sequence.
#Linked lists are a good choice for storing sequences of data elements that are not too long.

#example
#Create a linked list
#Create a class Node:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def countNodes(self):
        current = self
        count = 0
        while current != None: #while current is not None
            count += 1
            current = current.next
        return count

    def printNodes(self):
        current = self
        while current:
            print(current.data)
            current = current.next

head = Node(["Test", "Test2", "Test3"])
head.next = Node(["Test4", "Test5", "Test6"])
head.next.next = Node(["Test7", "Test8", "Test9"])

print(head.countNodes())
head.printNodes()

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(head.countNodes())
head.printNodes()

#Singly Linked Lists
#Singly linked lists are a data structure that store a sequence of data elements,
#   each of which is connected to the next element in the sequence.
#Singly linked lists are a good choice for storing sequences of data elements that are not too long.

#example
#Create a singly linked list
#Create a class Node:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def countNodes(self):
        current = self
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def printNodes(self):
        current = self
        while current:
            print(current.data)
            current = current.next

#defining a linked list
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

#connecting nodes
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

#printing the linked list
print(head.countNodes())
head.printNodes()

#Doubly Linked Lists
#Doubly linked lists are a data structure that store a sequence of data elements,
#   each of which is connected to the next element in the sequence and to the previous element in the sequence.
#Doubly linked lists are a good choice for storing sequences of data elements that are not too long.
#example
#Create a doubly linked list
#Create a class Node:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def countNodes(self):
        current = self
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def printNodes(self):
        current = self
        while current:
            print(current.data)
            current = current.next

    def printNodesReverse(self):
        current = self 
        while current.next: #while current is not None
            current = current.next 
        while current: #while current is not None
            print(current.data)
            current = current.prev 

#defining a linked list
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

#connecting nodes
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

#printing the linked list
print(head.countNodes())
head.printNodes()
head.printNodesReverse()


