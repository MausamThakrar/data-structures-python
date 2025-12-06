from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional, Iterable, List


@dataclass
class Node:
    value: Any
    next: Optional["Node"] = None


class SinglyLinkedList:
    """
    Simple implementation of a singly linked list.

    Supported operations:
    - append
    - prepend
    - insert_at(index)
    - delete_value(value)
    - find(value)
    - reverse
    - to_list
    """

    def __init__(self, values: Optional[Iterable[Any]] = None) -> None:
        self.head: Optional[Node] = None
        if values is not None:
            for v in values:
                self.append(v)

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def prepend(self, value: Any) -> None:
        new_node = Node(value, next=self.head)
        self.head = new_node

    def insert_at(self, index: int, value: Any) -> None:
        if index < 0:
            raise IndexError("index must be non-negative")

        if index == 0:
            self.prepend(value)
            return

        new_node = Node(value)
        current = self.head
        pos = 0
        while current is not None and pos < index - 1:
            current = current.next
            pos += 1

        if current is None:
            raise IndexError("index out of range")

        new_node.next = current.next
        current.next = new_node

    def delete_value(self, value: Any) -> bool:
        """
        Delete the first node with the given value.
        Returns True if deleted, False if not found.
        """
        current = self.head
        prev: Optional[Node] = None

        while current is not None:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next

        return False

    def find(self, value: Any) -> Optional[Node]:
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def reverse(self) -> None:
        prev: Optional[Node] = None
        current = self.head

        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev

    def to_list(self) -> List[Any]:
        result: List[Any] = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __repr__(self) -> str:
        return f"SinglyLinkedList({self.to_list()})"
