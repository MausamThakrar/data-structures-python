from __future__ import annotations
from typing import Any, List, Tuple, Optional


class HashTable:
    """
    Simple hash table with separate chaining.

    Methods:
    - put(key, value)
    - get(key)
    - delete(key)
    - contains(key)
    """

    def __init__(self, capacity: int = 16) -> None:
        self.capacity = max(4, capacity)
        self._buckets: List[List[Tuple[Any, Any]]] = [[] for _ in range(self.capacity)]
        self._size = 0

    def _bucket_index(self, key: Any) -> int:
        return hash(key) % self.capacity

    def put(self, key: Any, value: Any) -> None:
        index = self._bucket_index(key)
        bucket = self._buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

    def get(self, key: Any) -> Optional[Any]:
        index = self._bucket_index(key)
        bucket = self._buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key: Any) -> bool:
        index = self._bucket_index(key)
        bucket = self._buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return True
        return False

    def contains(self, key: Any) -> bool:
        return self.get(key) is not None

    def size(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"HashTable(size={self._size}, capacity={self.capacity})"
