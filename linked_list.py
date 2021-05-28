from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def add_to_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def contains_node(self, value):
        current_node = self.head
        node_id = 1
        results = []
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
                print(value)
            current_node = current_node.next
            node_id = node_id + 1
        return results
