class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "DLLNode object: data={}".format(self.data)

    def get_data(self):
        """Return the self.data attribute."""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data
        parameter."""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next
        parameter."""
        self.next = new_next

    def get_previous(self):
        """Return the self.previous attribute"""
        return self.previous

    def set_previous(self, new_previous):
        """Replace the existing value of the self.previous attribute with
        new_previous parameter."""
        self.previous = new_previous


if __name__ == '__main__':

    node1 = DLLNode('blue')
    node1.set_data('yellow')
    node2 = DLLNode('red')
    node3 = DLLNode('green')
    node1.set_next(node2)
    node2.set_next(node3)
    node1.get_next()

    node2.set_previous(node1)

    print(node1.get_data())

    print(node1.get_next())

    print(node2.get_next())

    print(node2.get_previous())
