"""
# Data Structure: Doubly Linked List
# Methods: insert (at end), delete (by value), search (by value), display
"""

from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Optional["Node[T]"] = None
        self.prev: Optional["Node[T]"] = None


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None

    def insert(self, data: T) -> None:
        """
        Insert a new node at the end of the linked list.
        Time Complexity: O(1)
        """

        new_node: Node[T] = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node

    def delete(self, data: T) -> bool:
        """
        Delete the first node containing the given value.
        Time Complexity: O(n)
        """

        current: Optional[Node[T]] = self.head

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

    def search(self, data: T) -> bool:
        """
        Search for a value in the linked list.
        Time Complexity: O(n)
        """

        current: Optional[Node[T]] = self.head

        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def display(self) -> None:
        """
        Display all elements from head to tail.
        """

        current: Optional[Node[T]] = self.head
        nodes: list[str] = []

        while current:
            nodes.append(str(current.data))
            current = current.next

        nodes.append("None")
        print(" <-> ".join(nodes))


def main() -> None:
    print("=" * 45)
    print("DOUBLY LINKED LIST")
    print("=" * 45)

    # Ab hum mypy ko explicitly batayenge ke ye LinkedList integers store karegi
    linked_list: LinkedList[int] = LinkedList()

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