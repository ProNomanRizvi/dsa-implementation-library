"""
# Data Structure: Doubly Linked List
# Methods: insert (at end), delete (by value), search (by value), display
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        """
        Insert a new node at the end of the linked list.
        Time Complexity: O(1)
        """

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def delete(self, data):
        """
        Delete the first node containing the given value.
        Time Complexity: O(n)
        """

        current = self.head

        while current:

            if current.data == data:

                # Deleting the head node
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None

                else:
                    current.prev.next = current.next

                # Deleting the tail node
                if current.next is None:
                    self.tail = current.prev

                else:
                    current.next.prev = current.prev

                return True

            current = current.next

        return False

    def search(self, data):
        """
        Search for a value in the linked list.
        Time Complexity: O(n)
        """

        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def display(self):
        """
        Display all elements from head to tail.
        """

        current = self.head
        nodes = []

        while current:
            nodes.append(str(current.data))
            current = current.next

        nodes.append("None")
        print(" <-> ".join(nodes))


def main():
    print("=" * 45)
    print("DOUBLY LINKED LIST")
    print("=" * 45)

    linked_list = LinkedList()

    print("\nInserting values: 10, 20, 30, 40")
    for value in [10, 20, 30, 40]:
        linked_list.insert(value)

    print("\nLinked List:")
    linked_list.display()

    print("\nDeleting 20...")
    linked_list.delete(20)

    print("\nLinked List:")
    linked_list.display()

    print("\nSearch Results:")
    print(f"Search 30: {linked_list.search(30)}")
    print(f"Search 100: {linked_list.search(100)}")


if __name__ == "__main__":
    main()