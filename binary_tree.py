"""
# Data Structure: Binary Tree (no ordering rule, level-order insert)
# Methods: insert, search, display
"""

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert a node at the first available position (Level-Order).
        Time Complexity: O(n)
        """

        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue = deque([self.root])

        while queue:
            current = queue.popleft()

            if current.left is None:
                current.left = new_node
                return
            queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            queue.append(current.right)

    def search(self, data):
        """
        Search for a value using Level-Order Traversal.
        Time Complexity: O(n)
        """

        if self.root is None:
            return False

        queue = deque([self.root])

        while queue:
            current = queue.popleft()

            if current.data == data:
                return True

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return False

    def display(self):
        """
        Display the tree in Level-Order.
        """

        if self.root is None:
            print("Empty")
            return

        result = []
        queue = deque([self.root])

        while queue:
            current = queue.popleft()
            result.append(str(current.data))

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        print(" -> ".join(result))


def main():
    print("=" * 45)
    print("BINARY TREE")
    print("=" * 45)

    tree = BinaryTree()

    print("\nInserting values: 10, 20, 30, 40, 50")

    for value in [10, 20, 30, 40, 50]:
        tree.insert(value)

    print("\nLevel-Order Traversal:")
    tree.display()

    print("\nSearch Results:")
    print(f"Search 30: {tree.search(30)}")
    print(f"Search 100: {tree.search(100)}")


if __name__ == "__main__":
    main()