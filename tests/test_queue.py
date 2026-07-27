from custom_queue import Queue


def test_insert_and_display(capsys):
    queue = Queue()

    queue.insert(10)
    queue.insert(20)
    queue.insert(30)

    queue.display()

    captured = capsys.readouterr()
    assert captured.out.strip() == "10 -> 20 -> 30"


def test_delete_returns_first_inserted():
    queue = Queue()

    queue.insert(10)
    queue.insert(20)
    queue.insert(30)

    assert queue.delete() == 10
    assert queue.search(10) is False


def test_delete_empty_queue():
    queue = Queue()

    assert queue.delete() is None


def test_search_found_and_not_found():
    queue = Queue()

    queue.insert(5)
    queue.insert(15)

    assert queue.search(5) is True
    assert queue.search(100) is False


def test_empty_queue_display(capsys):
    queue = Queue()

    queue.display()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Empty"