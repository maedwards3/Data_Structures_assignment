class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left_branch = None
        self.right_branch = None

    def insert_node(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left_branch:
                self.left_branch.insert_node(data)
            else:
                self.left_branch = BinarySearchTree(data)
        else:
            if self.right_branch:
                self.right_branch.insert_node(data)
            else:
                self.right_branch = BinarySearchTree(data)

    def search_for_node(self, data):
        pass
