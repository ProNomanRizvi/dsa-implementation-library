from linked_list import LinkedList


def test_insert_and_display(capsys):
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.display()
    captured = capsys.readouterr()
    assert captured.out.strip() == "10 <-> 20 <-> 30 <-> None"


def test_delete_existing_value():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    assert ll.delete(20) is True
    assert ll.search(20) is False


def test_delete_nonexistent_value():
    ll = LinkedList()
    ll.insert(10)
    assert ll.delete(999) is False


def test_search_found_and_not_found():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(15)
    assert ll.search(5) is True
    assert ll.search(100) is False


def test_empty_list_display(capsys):
    ll = LinkedList()
    ll.display()
    captured = capsys.readouterr()
    assert captured.out.strip() == "None"