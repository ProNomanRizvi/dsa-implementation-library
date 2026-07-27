from binary_tree import BinaryTree


def test_insert_and_display(capsys):
    tree = BinaryTree()

    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)

    tree.display()

    captured = capsys.readouterr()
    assert captured.out.strip() == "10 -> 20 -> 30 -> 40 -> 50"


def test_search_found_and_not_found():
    tree = BinaryTree()

    for value in [10, 20, 30, 40, 50]:
        tree.insert(value)

    assert tree.search(30) is True
    assert tree.search(100) is False


def test_delete_existing_node(capsys):
    tree = BinaryTree()

    for value in [10, 20, 30, 40, 50]:
        tree.insert(value)

    assert tree.delete(20) is True

    tree.display()
    captured = capsys.readouterr()

    assert captured.out.strip() == "10 -> 50 -> 30 -> 40"
    assert tree.search(20) is False


def test_delete_nonexistent_node():
    tree = BinaryTree()

    for value in [10, 20, 30]:
        tree.insert(value)

    assert tree.delete(999) is False


def test_empty_tree_display(capsys):
    tree = BinaryTree()

    tree.display()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Empty"