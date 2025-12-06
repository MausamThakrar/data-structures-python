from src.linked_list import SinglyLinkedList
from src.stack import Stack
from src.queue import Queue
from src.bst import BinarySearchTree
from src.hash_table import HashTable


def test_linked_list():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.prepend(0)
    ll.insert_at(2, 1.5)
    assert ll.to_list() == [0, 1, 1.5, 2]
    ll.delete_value(1.5)
    assert ll.to_list() == [0, 1, 2]
    ll.reverse()
    assert ll.to_list() == [2, 1, 0]


def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()


def test_queue():
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    assert q.peek() == "a"
    assert q.dequeue() == "a"
    assert q.dequeue() == "b"
    assert q.is_empty()


def test_bst():
    bst = BinarySearchTree()
    for val in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(val)
    assert bst.inorder() == [2, 3, 4, 5, 6, 7, 8]
    assert bst.find_min() == 2
    assert bst.find_max() == 8
    bst.delete(5)
    assert bst.inorder() == [2, 3, 4, 6, 7, 8]


def test_hash_table():
    ht = HashTable()
    ht.put("a", 1)
    ht.put("b", 2)
    ht.put("a", 3)
    assert ht.get("a") == 3
    assert ht.get("b") == 2
    assert ht.contains("a")
    assert ht.delete("a")
    assert not ht.contains("a")
