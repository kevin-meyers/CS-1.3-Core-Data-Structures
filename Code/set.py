from hashtable import HashTable
from binarytree import BinarySearchTree


class HashSet:
    def __init__(self):
        self.table = HashTable()

    @property
    def size(self):
        return len(self.table)

    def __contains__(self, item):
        ''' Special method allowing use of `in` '''
        return item in self.table

    def __iter__(self):
        ''' Special method allowing use of looping. '''
        for item in self.table.items():
            yield item

    def add(self, item):
        self.table.set(item, None)

    def remove(self, item):
        self.table.delete(item)

    def __len__(self):
        ''' Special method allowing use of `len()`. '''
        return self.size

    def _smaller_larger_pair(self, set_1, set_2):
        ''' Helper to return the ordering of smaller, larger. '''
        if len(set_1) < len(set_2):
            return set_1, set_2

        return set_2, set_1

    def intersection(self, other_set):
        ''' Find items that are present in both sets. '''
        # Get the smaller, larger pair
        smaller, larger = self._smaller_larger_pair(self, other_set)
        new_set = HashSet()
        for item in smaller:
            if item in larger:
                new_set.add(item)

        return new_set

    def intersection_(self, other_set):
        ''' Find items that are present in both sets. '''
        # Getting the smaller set to reduce
        # The number of loops
        if self.size < other_set.size:
            smaller = self
            larger = other_set

        else:
            smaller = other_set
            larger = self

        new_set = HashSet()
        for item in smaller.table.items():
            if larger.contains(item):
                new_set.add(item)

        return new_set

    def union(self, other_set):
        new_set = HashSet()
        for item in self.table.items():
            new_set.add(item)

        for item in other_set.table.items():
            new_set.add(item)

        return new_set

    def difference(self, other_set):
        new_set = HashSet()
        for item in self.table.items():
            if not other_set.contains(item):
                new_set.add(item)

        return new_set

    def is_subset(self, other_set):
        if len(self) > len(other_set):
            return False

        for item in self:
            if item not in other_set:
                return False

        return True


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
        for item in self.tree

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





if __name__ == '__main__':
    hs = HashSet()
    items = [1, 2, 3, 4, 3, 2, 5]
    print(f'items: {items}')
    for item in items:
        hs.add(item)

    print(f'1 in set: {hs.contains(1)}')
    print('removing 4')
    hs.remove(4)
    print(f'4 in set: {hs.contains(4)}')
    print(hs.table)
