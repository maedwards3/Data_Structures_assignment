class Node:

    def __init__(self, data):
        self.next = None
        self.data = data

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False
