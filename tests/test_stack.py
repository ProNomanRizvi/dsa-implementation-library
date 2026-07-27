from stack import Stack


def test_insert_and_display(capsys):
    stack = Stack()

    stack.insert(10)
    stack.insert(20)
    stack.insert(30)

    stack.display()

    captured = capsys.readouterr()
    assert captured.out.strip() == "10 -> 20 -> 30"


def test_delete_returns_last_inserted():
    stack = Stack()

    stack.insert(10)
    stack.insert(20)
    stack.insert(30)

    assert stack.delete() == 30
    assert stack.search(30) is False


def test_delete_empty_stack():
    stack = Stack()

    assert stack.delete() is None


def test_search_found_and_not_found():
    stack = Stack()

    stack.insert(5)
    stack.insert(15)

    assert stack.search(5) is True
    assert stack.search(100) is False


def test_empty_stack_display(capsys):
    stack = Stack()

    stack.display()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Empty"