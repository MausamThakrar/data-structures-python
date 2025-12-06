from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any, List, Callable


@dataclass
class BSTNode:
    key: Any
    left: Optional["BSTNode"] = None
    right: Optional["BSTNode"] = None


class BinarySearchTree:
    """
    Classic Binary Search Tree (BST) implementation.

    Operations:
    - insert
    - search
    - delete
    - traversals: inorder, preorder, postorder
    - find_min, find_max
    """

    def __init__(self) -> None:
        self.root: Optional[BSTNode] = None

    def insert(self, key: Any) -> None:
        def _insert(node: Optional[BSTNode], key: Any) -> BSTNode:
            if node is None:
                return BSTNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            # ignore duplicates
            return node

        self.root = _insert(self.root, key)

    def search(self, key: Any) -> Optional[BSTNode]:
        node = self.root
        while node is not None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def _traverse(self, node: Optional[BSTNode], visit: Callable[[Any], None], order: str) -> None:
        if node is None:
            return
        if order == "pre":
            visit(node.key)
        self._traverse(node.left, visit, order)
        if order == "in":
            visit(node.key)
        self._traverse(node.right, visit, order)
        if order == "post":
            visit(node.key)

    def inorder(self) -> List[Any]:
        result: List[Any] = []
        self._traverse(self.root, result.append, order="in")
        return result

    def preorder(self) -> List[Any]:
        result: List[Any] = []
        self._traverse(self.root, result.append, order="pre")
        return result

    def postorder(self) -> List[Any]:
        result: List[Any] = []
        self._traverse(self.root, result.append, order="post")
        return result

    def find_min(self) -> Optional[Any]:
        node = self.root
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.key

    def find_max(self) -> Optional[Any]:
        node = self.root
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.key

    def delete(self, key: Any) -> None:
        def _delete(node: Optional[BSTNode], key: Any) -> Optional[BSTNode]:
            if node is None:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # node to delete
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                # two children: replace with inorder successor
                successor = node.right
                while successor.left is not None:
                    successor = successor.left
                node.key = successor.key
                node.right = _delete(node.right, successor.key)
            return node

        self.root = _delete(self.root, key)

    def __repr__(self) -> str:
        return f"BST(inorder={self.inorder()})"
