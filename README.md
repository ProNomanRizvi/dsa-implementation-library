# DSA Implementation Library

A small collection of core data structures built from scratch in Python: a doubly linked list, a stack, a queue, a binary tree, and a binary search tree. No built-in structures are used for the actual logic (the queue uses `collections.deque` internally for O(1) operations at both ends, but the insert/delete/search/display interface is written by hand).

Every structure exposes the same four methods so they're easy to compare and reuse:

- `insert(data)` — add a value
- `delete(data)` (or `delete()` for stack/queue) — remove a value
- `search(data)` — check whether a value exists
- `display()` — print the current contents

This started as practice for interview-style DSA questions and turned into a reference I can pull into other projects instead of re-writing these from memory every time.

## Sample Output

Every module has a runnable `main()` for a quick look at the behavior. Running `python3 stack.py`:

```
========================================
STACK (LIFO)
========================================

Inserting values: 10, 20, 30, 40

Stack:
10 -> 20 -> 30 -> 40

Deleted (Popped): 40

Stack After Delete:
10 -> 20 -> 30

Search Results:
Search 20: True
Search 100: False
```

Each of the other four files (`linked_list.py`, `custom_queue.py`, `binary_tree.py`, `bst.py`) runs the same way and prints its own walkthrough.

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

`preorder` and `postorder` are also available (both O(n)) — useful for serializing a tree or deleting it node-by-node, respectively.

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

print(tree.inorder())   # [20, 30, 40, 50, 60, 80] — same order display() uses
print(tree.preorder())  # [50, 30, 20, 40, 60, 80]
print(tree.postorder()) # [20, 40, 30, 60, 80, 50]
```

## Key Decisions

A few choices that came up while building these:

- **Queue uses `collections.deque`, not a plain list.** Popping from index 0 of a Python list is O(n) since every remaining element shifts left. `deque` is doubly-linked under the hood, so `popleft()` stays O(1) regardless of size. The insert/delete/search/display interface is still hand-written — `deque` is only used for the underlying storage.
- **BST has no self-balancing.** Insert and delete degrade to O(n) if the tree gets skewed (e.g. inserting values that are already sorted). Fixing that means implementing rotations (AVL or Red-Black), which was left out on purpose to keep this repo focused on the base structures rather than turning into a balanced-tree library.
- **Binary tree deletion swaps in the deepest-rightmost node**, not just any leaf, to keep the tree as close to complete as it was before the deletion. Same idea BSTs use with the inorder successor, just without the ordering constraint to help find it.
- **No third-party runtime dependencies.** Everything is standard library (`collections`, `typing`). `pytest` and `mypy` are dev-only tools for testing and type checking, which is why there's no `requirements.txt` — there's nothing to pin.

## Running Tests

This project uses `pytest`. Install it and run the suite from the repo root:

```bash
pip install pytest --break-system-packages
pytest -v
```

All structures are covered: insert, delete (including edge cases like empty structures, leaf nodes, nodes with two children, and root deletion for the BST), and search.

## Why this exists

Every one of these got built the slow way first: manual array shifting, a hand-written hash function, both singly and doubly linked lists, Big O worked out case by case (best, average, worst) before moving on. This repo is the cleaned-up version of that work — one place to check "how does X work and what's its complexity" instead of digging through old practice files.

## Future Improvements

- Self-balancing BST variant (AVL or Red-Black) to fix the O(n) skew case
- A hash table / hash map implementation to round out the core structure set
- A min-heap / priority queue, since the queue here is strictly FIFO

## License

MIT — see [LICENSE](LICENSE) for details.