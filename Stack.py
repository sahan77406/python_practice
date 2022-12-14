class StackData:

    def __init__(self):
        self.item_list = []

    def add(self, item):
        """ Add items to the list (append) """
        self.item_list.append(item)

    def remove(self):
        """ Remove top item from the list (pop)"""
        if self.item_list:
            return self.item_list.pop()

        return None

    def fetch_top_item(self):
        """ Return top item from the list (pop)"""
        if self.item_list:
            return self.item_list[-1]

        return None

    def size(self):
        """ Return the size of the list"""
        return len(self.item_list)

    def is_empty(self):
        """ Return true if the list empty """
        return self.item_list == []


def main():

    stack_colors = StackData()

# Adding item to the stack

    # add_item = input("Enter a color: ")
    # stack_colors.add(add_item)
    print("Adding item to the stack")
    stack_colors.add("red")
    stack_colors.add("yellow")
    stack_colors.add("green")
    stack_colors.add("black")
    stack_colors.add("white")

    print(stack_colors.item_list)
    print()

# Removing item from the stack

    print("Removing item from the stack")

    removed_item = stack_colors.remove()

    print(removed_item)
    print()

# Getting the top item of the stack

    print("Getting the top item of the stack")

    top_item = stack_colors.fetch_top_item()

    print(top_item)
    print()

# Getting the size of the stack
    print("Getting the size of the stack")
    size_of_stack = stack_colors.size()

    print(size_of_stack)
    print()

# Checking if the stack is empty

    print("Checking if the stack is empty")

    is_empty = stack_colors.is_empty()
    print(is_empty)


if __name__ == "__main__":
    main()
