from bst import BST


def test_insert_and_display(capsys):
    bst = BST()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(value)

    bst.display()

    captured = capsys.readouterr()
    assert captured.out.strip() == "20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80"


def test_search_found_and_not_found():
    bst = BST()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(value)

    assert bst.search(60) is True
    assert bst.search(100) is False


def test_delete_leaf_node():
    bst = BST()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(value)

    bst.delete(20)

    assert bst.search(20) is False
    assert bst.inorder() == [30, 40, 50, 60, 70, 80]


def test_delete_node_with_two_children():
    bst = BST()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(value)

    bst.delete(70)

    assert bst.search(70) is False
    assert bst.inorder() == [20, 30, 40, 50, 60, 80]


def test_empty_bst_display(capsys):
    bst = BST()

    bst.display()

    captured = capsys.readouterr()
    assert captured.out.strip() == ""