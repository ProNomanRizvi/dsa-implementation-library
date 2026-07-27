# DSA Implementation Library

A small collection of core data structures built from scratch in Python: a doubly linked list, a stack, a queue, a binary tree, and a binary search tree. No built-in structures are used for the actual logic (the queue uses `collections.deque` internally for O(1) operations at both ends, but the insert/delete/search/display interface is written by hand).

Every structure exposes the same four methods so they're easy to compare and reuse:

- `insert(data)` — add a value
- `delete(data)` (or `delete()` for stack/queue) — remove a value
- `search(data)` — check whether a value exists
- `display()` — print the current contents

This started as practice for interview-style DSA questions and turned into a reference I can pull into other projects instead of re-writing these from memory every time.

## Structures and Big O

### Linked List (doubly linked, with head/tail pointers)

| Operation | Time Complexity | Notes |
|---|---|---|
| `insert` | O(1) | Appends at the tail, so no traversal needed |
| `delete` | O(n) | Has to walk the list to find the matching value |
| `search` | O(n) | Linear scan from head |
| `display` | O(n) | Walks the full list once |

### Stack (LIFO, list-backed)

| Operation | Time Complexity | Notes |
|---|---|---|
| `insert` (push) | O(1) | `list.append` |
| `delete` (pop) | O(1) | `list.pop` from the end |
| `search` | O(n) | Has to check every item |
| `display` | O(n) | Prints bottom to top |

### Queue (FIFO, deque-backed)

| Operation | Time Complexity | Notes |
|---|---|---|
| `insert` (enqueue) | O(1) | `deque.append` at the rear |
| `delete` (dequeue) | O(1) | `deque.popleft` — this is the whole reason to use `deque` instead of a plain list, where popping from index 0 is O(n) |
| `search` | O(n) | Linear scan |
| `display` | O(n) | Prints front to rear |

### Binary Tree (no ordering rule, level-order insert)

| Operation | Time Complexity | Notes |
|---|---|---|
| `insert` | O(n) | BFS to find the first open spot, keeps the tree complete |
| `delete` | O(n) | BFS to find the target and the deepest-rightmost node, then swaps values |
| `search` | O(n) | No ordering to rely on, so every node might need checking |
| `display` | O(n) | Level-order (BFS) traversal |

### Binary Search Tree

| Operation | Average Case | Worst Case | Notes |
|---|---|---|---|
| `insert` | O(log n) | O(n) | Worst case happens when the tree is skewed, e.g. inserting already-sorted values |
| `delete` | O(log n) | O(n) | Two-children case uses the inorder successor (smallest value in the right subtree) |
| `search` | O(log n) | O(n) | Same skew risk as insert |
| `display` | O(n) | O(n) | Inorder traversal, so it happens to print in sorted order |

The BST worst case only shows up when the tree becomes a skewed line instead of branching — that's why balanced trees (AVL, Red-Black) exist, though this library doesn't implement self-balancing.

## Usage

### Linked List

```python
from linked_list import LinkedList

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()          # 10 <-> 20 <-> 30 <-> None

ll.delete(20)
ll.display()          # 10 <-> 30 <-> None

print(ll.search(30))   # True
print(ll.search(99))   # False
```

### Stack

```python
from stack import Stack

s = Stack()
s.insert(10)
s.insert(20)
s.insert(30)
s.display()            # 10 -> 20 -> 30

print(s.delete())      # 30 (last in, first out)
s.display()            # 10 -> 20
```

### Queue

```python
from custom_queue import Queue

q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.display()            # 10 -> 20 -> 30

print(q.delete())       # 10 (first in, first out)
q.display()            # 20 -> 30
```

### Binary Tree

```python
from binary_tree import BinaryTree

bt = BinaryTree()
for value in [10, 20, 30, 40, 50]:
    bt.insert(value)

bt.display()           # 10 -> 20 -> 30 -> 40 -> 50 (level-order)
bt.delete(20)
bt.display()           # deepest-rightmost value moves into 20's spot
```

### Binary Search Tree

```python
from bst import BST

tree = BST()
for value in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(value)

tree.display()          # 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80 (sorted)

tree.delete(70)         # two children — replaced by inorder successor
tree.display()

print(tree.search(60))  # True
print(tree.search(70))  # False, just deleted
```

## Running Tests

This project uses `pytest`. Install it and run the suite from the repo root:

```bash
pip install pytest --break-system-packages
pytest -v
```

All structures are covered: insert, delete (including edge cases like empty structures, leaf nodes, nodes with two children, and root deletion for the BST), and search.

## Why this exists

Every one of these got built the slow way first: manual array shifting, a hand-written hash function, both singly and doubly linked lists, Big O worked out case by case (best, average, worst) before moving on. This repo is the cleaned-up version of that work — one place to check "how does X work and what's its complexity" instead of digging through old practice files.

## License

MIT — see [LICENSE](LICENSE) for details.