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

def add_node(first_list, second_list):
    sum_nodes = []

    first_current = first_list.head
    second_current = second_list.head
          
    while first_current != None and second_current != None:
        sum_nodes.append(first_current.data + second_current.data)
        first_current = first_current.next
        second_current = second_current.next

    if first_current == None:
        while second_current != None:
            sum_nodes.append(second_current.data)
            second_current = second_current.next
    else:
        while first_current != None:
            sum_nodes.append(first_current.data)
            first_current = first_current.next

    return sum_nodes

first_list = create_linked_list()
first_list.insert_nodes([1, 2, 3, 4])

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

print("Final List:")
final_list = add_node(first_list, second_list)
sum_final_list = create_linked_list()
sum_final_list.insert_nodes(final_list)
sum_final_list.print_list()


