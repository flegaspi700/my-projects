#Create Linked List
#Create a class Node:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class create_linked_list:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

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

my_list = create_linked_list()
my_list.insert_node([1, 2, 3, 4, 5])


print(my_list.nodecount())
my_list.print_list()