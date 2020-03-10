from hashtable import HashTable


class HashSet:
    def __init__(self, items=[]):
        self.table = HashTable()
        for item in items:
            self.add(item)

    @property
    def size(self):
        return len(self.table)

    def __contains__(self, item):
        ''' Special method allowing use of `in` '''
        return item in self.table

    def __iter__(self):
        ''' Special method allowing use of looping. '''
        for item in self.table.keys():
            yield item

    def __str__(self):
        return '{' + f'{", ".join(self)}' + '}'

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


    def __iand__(self, other_set):
        for item in self:
            if item not in other_set:
                self.remove(item)

        return self

    def __and__(self, other_set):
        return self.intersection(other_set)

    def intersection(self, other_set):
        ''' Find items that are present in both sets. '''
        # Get the smaller, larger pair
        smaller, larger = self._smaller_larger_pair(self, other_set)
        new_set = HashSet()
        for item in smaller:
            if item in larger:
                new_set.add(item)

        return new_set

    def _assert_type(self, compared, symbol):
        if not isinstance(compared, HashSet):
            raise TypeError(
                f'unsuported operand type(s) for \
                {symbol} \'{type(self)} and \'{type(compared)}\''
            )

    def __add__(self, other_set):
        self._assert_type(other_set, '+')
        return self._union(other_set)

    def __ior__(self, other_set):
        self._assert_type(other_set, '|=')

        for item in other_set:
            self.add(item)

        return self

    def __or__(self, other_set):
        self._assert_type(other_set, '|')
        return self.union(other_set)

    def _union(self, other_set):
        new_set = HashSet()
        for item in self:
            new_set.add(item)

        for item in other_set:
            new_set.add(item)

        return new_set

    def __isub__(self, other_set):
        self._assert_type(other_set, '-=')
        if len(self) < len(other_set):
            for item in self:
                if item in other_set:
                    self.remove(item)

        else:
            for item in other_set:
                if item in self:
                    self.remove(item)

        return self

    def __sub__(self, other_set):
        self._assert_type(other_set, '-')
        return self._difference(other_set)

    def _difference(self, other_set):
        new_set = HashSet()
        for item in self:
            if item not in other_set:
                new_set.add(item)

        return new_set

    def is_subset(self, other_set):
        if len(self) > len(other_set):
            return False

        for item in self:
            if item not in other_set:
                return False

        return True


if __name__ == '__main__':
    hs = HashSet()
    items = [1, 2, 3, 4, 3, 2, 5]
    print(f'items: {items}')
    for item in items:
        hs.add(item)

    print(f'1 in set: {1 in hs}')
    print('removing 4')
    hs.remove(4)
    print(f'4 in set: {4 in hs}')
    print(hs.table)
