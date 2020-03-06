
from binarytree import BinarySearchTree


class TreeSet:
    def __init__(self, items=None):
        self.tree = BinarySearchTree()
        if items is not None:
            for item in items:
                self.add(item)

    def __len__(self):
        return len(self.tree)

    def __contains__(self, item):
        return item in self.tree

    def __iter__(self):
        for item in self.tree.items_in_order():
            yield item

    def add(self, item):
        if item not in self.tree:
            self.tree.insert(item)

    def remove(self, item):
        self.tree.delete(item)

    def _smaller_larger_pair(self, tree_1, tree_2):
        if len(tree_1) < len(tree_2):
            return tree_1, tree_2

        return tree_2, tree_1

    def intersection(self, other_set):
        new_set = TreeSet()
        smaller, larger = self._smaller_larger_pair(self.tree, other_set.tree)
        for item in smaller.items_pre_order():
            if item in larger:
                new_set.add(item)

        return new_set

    def _alternating_generator(self, tree1, tree2):
        items_1 = tree1.items_pre_order()
        items_2 = tree2.items_pre_order()
        for item_1, item_2 in zip(items_1, items_2):
            yield item_1
            yield item_2

    def union(self, other_set):
        new_set = TreeSet()
        for item in self._alternating_generator(self.tree, other_set.tree):
            new_set.add(item)

        return new_set

    def difference(self, other_set):
        new_set = TreeSet()
        for item in self.tree.items_pre_order():
            if item not in other_set:
                new_set.add(item)

        return new_set

    def is_subset(self, other_set):
        if len(self) > len(other_set):
            return False

        for item in self.tree.items_pre_order():
            if not other_set.contains(item):
                return False

        return True

