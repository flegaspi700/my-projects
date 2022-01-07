#Create Linked List
#Create a class Node:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class create_linked_list:
    def __init__(self):
        self.head = None

    def insert_nodes(self, data):
        for item in data:
            new_node = Node(item)

            if self.head == None:
                self.head = new_node
            else:
                current = self.head
                while current.next != None:
                    current = current.next
                current.next = new_node
    
    def nodecount(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def print_list(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next  

first_list = create_linked_list()
first_list.insert_nodes([1, 2, 3, 4, 5])

print("Number of Nodes:", first_list.nodecount())
print("Printing List:")
first_list.print_list()
print("end of list")

second_list = create_linked_list()
second_list.insert_nodes([1, 1, 1, 1, 1])

print("Number of Nodes:", second_list.nodecount())
print("Printing List:")
second_list.print_list()
print("end of list")

print("Print")
print(first_list.head.data)


