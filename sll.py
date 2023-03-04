class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)

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


if __name__ == '__main__':

    node1 = SLLNode('blue')
    node1.set_data('yellow')
    node2 = SLLNode('red')
    node3 = SLLNode('green')
    node1.set_next(node2)
    node2.set_next(node3)
    node1.get_next()

    print(node1.get_data())

    print(node1.get_next())

    print(node2.get_next())
