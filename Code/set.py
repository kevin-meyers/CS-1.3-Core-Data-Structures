from hashtable import HashTable
from binarytree import BinarySearchTree


class HashSet:
    def __init__(self):
        self.table = HashTable()
        self.size = 0

    def contains(self, item):
        return self.table.contains(item)

    def add(self, item):
        self.table.set(item, None)
        self.size += 1

    def remove(self, item):
        self.table.delete(item)
        self.size -= 1

    def length(self):
        return self.size

    def _smaller_larger_pair(self, table_1, table_2):
        if len(table_1) < len(table_2):
            return table_1, table_2

        return table_2, table_1

    def intersection(self, other_set):
        smaller, larger = self._smaller_larger_pair(self.table, other_set.table)
        new_set = HashSet()
        for item in smaller.items():
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

        for item in self.table.items():
            if not other_set.contains(item):
                return False

        return True


class TreeSet:
    def __init__(self):
        self.tree = BinarySearchTree()
        self.size = 0

    def __len__(self):
        return self.length()

    def __contains__(self, item):
        return self.contains(item)

    def contains(self, item):
        return self.tree.contains(item)

    def add(self, item):
        if item not in self.tree:
            self.tree.insert(item)
            self.size += 1

    def remove(self, item):
        self.tree.delete(item)
        self.size -= 1

    def length(self):
        return self.size

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
