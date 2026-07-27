"""
# Data Structure: Queue (FIFO)
# Methods: insert (enqueue), delete (dequeue), search, display
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def insert(self, data):
        """
        Enqueue an item at the rear of the queue.
        Time Complexity: O(1)
        """
        self.items.append(data)

    def delete(self):
        """
        Dequeue and return the front item.
        Time Complexity: O(1)

        Returns:
            Front item if queue is not empty, otherwise None.
        """
        if not self.items:
            return None

        return self.items.popleft()

    def search(self, data):
        """
        Search for a value in the queue.
        Time Complexity: O(n)
        """
        return data in self.items

    def display(self):
        """
        Display queue contents from front to rear.
        """
        if not self.items:
            print("Empty")
        else:
            print(" -> ".join(str(item) for item in self.items))


def main():
    print("=" * 40)
    print("QUEUE (FIFO)")
    print("=" * 40)

    queue = Queue()

    print("\nInserting values: 10, 20, 30, 40")
    for value in [10, 20, 30, 40]:
        queue.insert(value)

    print("\nQueue:")
    queue.display()

    deleted = queue.delete()
    print(f"\nDeleted (Dequeued): {deleted}")

    print("\nQueue After Delete:")
    queue.display()

    print("\nSearch Results:")
    print(f"Search 30: {queue.search(30)}")
    print(f"Search 100: {queue.search(100)}")


if __name__ == "__main__":
    main()