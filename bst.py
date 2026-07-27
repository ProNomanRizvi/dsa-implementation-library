"""
# Data Structure: Binary Search Tree (BST)
# Methods: insert, delete, search, display (inorder)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert a value into the BST.
        Time Complexity: O(log n) average, O(n) worst
        """

        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

            else:
                # Ignore duplicate values
                return

    def search(self, data):
        """
        Search for a value in the BST.
        Time Complexity: O(log n) average, O(n) worst
        """

        current = self.root

        while current:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right

        return False

    def delete(self, data):
        """
        Delete a value from the BST while maintaining BST properties.
        """
        self.root = self._delete_helper(self.root, data)

    def _delete_helper(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete_helper(node.left, data)

        elif data > node.data:
            node.right = self._delete_helper(node.right, data)

        else:
            # Case 1 & 2: No child or one child
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            # Case 3: Two children
            successor = node.right

            while successor.left:
                successor = successor.left

            node.data = successor.data
            node.right = self._delete_helper(node.right, successor.data)

        return node

    # -----------------------------
    # Traversals
    # -----------------------------
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.data)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.data)

    def display(self):
        """
        Display BST in sorted order (Inorder Traversal).
        """
        print(" -> ".join(map(str, self.inorder())))


def main():
    print("=" * 45)
    print("BINARY SEARCH TREE")
    print("=" * 45)

    bst = BST()

    values = [50, 30, 70, 20, 40, 60, 80]

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