##
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class create_linked_list:
    #head = Node(n)
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

    def countnodes(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next 
        return count

    def print_nodes(self):
        current = self.head
        while current != None:
            print("Node Value", current.data)
            current = current.next

list1 = create_linked_list()
list1.insert_nodes([2,4,6,8,10])
print(list1.countnodes())
list1.print_nodes()

