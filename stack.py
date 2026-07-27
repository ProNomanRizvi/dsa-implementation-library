"""
# Data Structure: Stack (LIFO)
# Methods: insert (push), delete (pop), search, display
"""


class Stack:
    def __init__(self):
        self.items = []

    def insert(self, data):
        """
        Push an item onto the stack.
        Time Complexity: O(1)
        """
        self.items.append(data)

    def delete(self):
        """
        Pop and return the top item.
        Time Complexity: O(1)

        Returns:
            Popped item if stack is not empty, otherwise None.
        """
        if not self.items:
            return None

        return self.items.pop()

    def search(self, data):
        """
        Search for a value in the stack.
        Time Complexity: O(n)
        """
        return data in self.items

    def display(self):
        """
        Display stack contents from bottom to top.
        """
        if not self.items:
            print("Empty")
        else:
            print(" -> ".join(str(item) for item in self.items))


def main():
    print("=" * 40)
    print("STACK (LIFO)")
    print("=" * 40)

    stack = Stack()

    print("\nInserting values: 10, 20, 30, 40")
    for value in [10, 20, 30, 40]:
        stack.insert(value)

    print("\nStack:")
    stack.display()

    popped = stack.delete()
    print(f"\nDeleted (Popped): {popped}")

    print("\nStack After Delete:")
    stack.display()

    print("\nSearch Results:")
    print(f"Search 20: {stack.search(20)}")
    print(f"Search 100: {stack.search(100)}")


if __name__ == "__main__":
    main()