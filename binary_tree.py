"""
# Data Structure: Binary Tree (no ordering rule, level-order insert)
# Methods: insert, search, display
"""

from collections import deque
from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.left: Optional["Node[T]"] = None
        self.right: Optional["Node[T]"] = None


class BinaryTree(Generic[T]):
    def __init__(self) -> None:
        self.root: Optional[Node[T]] = None

    def insert(self, data: T) -> None:
        """
        Insert a node at the first available position (Level-Order).
        Time Complexity: O(n)
        """

        new_node: Node[T] = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue: deque[Node[T]] = deque([self.root])

        while queue:
            current: Node[T] = queue.popleft()

            if current.left is None:
                current.left = new_node
                return
            queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            queue.append(current.right)

    def search(self, data: T) -> bool:
        """
        Search for a value using Level-Order Traversal.
        Time Complexity: O(n)
        """

        if self.root is None:
            return False

        queue: deque[Node[T]] = deque([self.root])

        while queue:
            current: Node[T] = queue.popleft()

            if current.data == data:
                return True

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return False

    def delete(self, data: T) -> bool:
        """
        Delete a node by replacing it with the deepest-rightmost node,
        then removing that deepest node.
        Time Complexity: O(n)
        """

        if self.root is None:
            return False

        # Tree has only one node
        if self.root.left is None and self.root.right is None:
            if self.root.data == data:
                self.root = None
                return True
            return False

        target: Optional[Node[T]] = None
        last_node: Optional[Node[T]] = None
        last_parent: Optional[Node[T]] = None

        # Queue contains a tuple of (current_node, parent_node)
        queue: deque[tuple[Node[T], Optional[Node[T]]]] = deque([(self.root, None)])

        while queue:
            current, parent = queue.popleft()

            if current.data == data:
                target = current

            last_node = current
            last_parent = parent

            if current.left:
                queue.append((current.left, current))

            if current.right:
                queue.append((current.right, current))

        # Ensure we found the target and valid last nodes for mypy safety
        if target is None or last_node is None or last_parent is None:
            return False

        # Replace target value with deepest-rightmost node value
        target.data = last_node.data

        # Remove deepest-rightmost node
        if last_parent.left == last_node:
            last_parent.left = None
        else:
            last_parent.right = None

        return True

    def display(self) -> None:
        """
        Display the tree in Level-Order.
        """

        if self.root is None:
            print("Empty")
            return

        result: list[str] = []
        queue: deque[Node[T]] = deque([self.root])

        while queue:
            current: Node[T] = queue.popleft()
            result.append(str(current.data))

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        print(" -> ".join(result))


def main() -> None:
    print("=" * 45)
    print("BINARY TREE")
    print("=" * 45)

    tree: BinaryTree[int] = BinaryTree()

    print("\nInserting values: 10, 20, 30, 40, 50")

    for value in [10, 20, 30, 40, 50]:
        tree.insert(value)

    print("\nLevel-Order Traversal:")
    tree.display()

    print("\nSearch Results:")
    print(f"Search 30: {tree.search(30)}")
    print(f"Search 100: {tree.search(100)}")

    print("\nDeleting 20...")
    tree.delete(20)

    print("\nLevel-Order Traversal After Delete:")
    tree.display()


if __name__ == "__main__":
    main()