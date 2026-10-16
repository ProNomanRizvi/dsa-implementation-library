"""
# Data Structure: Binary Search Tree (BST)
# Methods: insert, delete, search, display (inorder)
"""

from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.left: Optional["Node[T]"] = None
        self.right: Optional["Node[T]"] = None


class BST(Generic[T]):
    def __init__(self) -> None:
        self.root: Optional[Node[T]] = None

    def insert(self, data: T) -> None:
        """
        Insert a value into the BST.
        Time Complexity: O(log n) average, O(n) worst
        """

        new_node: Node[T] = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current: Node[T] = self.root

        while True:
            # Added type: ignore because mypy doesn't inherently know that generic 'T' is comparable
            if data < current.data:  # type: ignore
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif data > current.data:  # type: ignore
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

            else:
                # Ignore duplicate values
                return

    def search(self, data: T) -> bool:
        """
        Search for a value in the BST.
        Time Complexity: O(log n) average, O(n) worst
        """

        current: Optional[Node[T]] = self.root

        while current:
            if data == current.data:
                return True
            elif data < current.data:  # type: ignore
                current = current.left
            else:
                current = current.right

        return False

    def delete(self, data: T) -> None:
        """
        Delete a value from the BST while maintaining BST properties.
        """
        parent: Optional[Node[T]] = None
        current = self.root
        while current is not None and current.data != data:
            parent = current
            if data < current.data:  # type: ignore
                current = current.left
            else:
                current = current.right

        if current is None:
            return

        if current.left is not None and current.right is not None:
            successor_parent = current
            successor = current.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            current.data = successor.data
            parent = successor_parent
            current = successor

        child = current.left if current.left is not None else current.right
        if parent is None:
            self.root = child
        elif parent.left is current:
            parent.left = child
        else:
            parent.right = child

    # -----------------------------
    # Traversals
    # -----------------------------
    def inorder(self) -> list[T]:
        result: list[T] = []
        stack: list[Node[T]] = []
        current = self.root
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.data)
            current = current.right
        return result

    def preorder(self) -> list[T]:
        result: list[T] = []
        if self.root is None:
            return result
        stack = [self.root]
        while stack:
            current = stack.pop()
            result.append(current.data)
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)
        return result

    def postorder(self) -> list[T]:
        result: list[T] = []
        if self.root is None:
            return result
        stack = [(self.root, False)]
        while stack:
            current, visited = stack.pop()
            if visited:
                result.append(current.data)
                continue
            stack.append((current, True))
            if current.right is not None:
                stack.append((current.right, False))
            if current.left is not None:
                stack.append((current.left, False))
        return result

    def display(self) -> None:
        """
        Display BST in sorted order (Inorder Traversal).
        """
        print(" -> ".join(map(str, self.inorder())))


def main() -> None:
    print("=" * 45)
    print("BINARY SEARCH TREE")
    print("=" * 45)

    bst: BST[int] = BST()

    values: list[int] = [50, 30, 70, 20, 40, 60, 80]

    print("\nInserting values:", values)
    for value in values:
        bst.insert(value)

    print("\nBST (Inorder):")
    bst.display()

    print("\nDeleting node with two children (70)...")
    bst.delete(70)
    bst.display()

    print("\nDeleting leaf node (20)...")
    bst.delete(20)
    bst.display()

    print("\nSearch Results:")
    print(f"Search 60: {bst.search(60)}")
    print(f"Search 70: {bst.search(70)}")


if __name__ == "__main__":
    main()
