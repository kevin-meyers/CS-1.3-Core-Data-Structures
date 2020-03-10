import unittest

from hash_set import HashSet


class TestHashSet(unittest.TestCase):
    def test_init(self):
        hs = HashSet()
        assert hs.size == 0
        assert str(hs) == '{}'

    def test_init_with_list(self):
        items = [1, 2, 3, 4]
        hs = HashSet(items)
        assert hs.size == len(items)
        for item in items:
            assert item in hs

    def test_size(self):
        hs = HashSet()
        assert hs.size == 0
        hs.add('A')
        assert hs.size == 1
        hs.add('B')
        assert hs.size == 2
        hs.remove('A')
        assert hs.size == 1
        hs.remove('B')
        assert hs.size == 0

    def test_add(self):
        items = ['A', 'B', 'C']
        hs = HashSet()
        for item in items:
            hs.add(item)

        for item in items:
            assert item in hs

        assert len(hs) == len(items)

    def test_remove(self):
        items = ['A', 'B', 'C']
        hs = HashSet(items)
        for item in items:
            # For each item, make sure can only remove once
            hs.remove(item)
            with self.assertRaises(KeyError):
                hs.remove(item)

        assert hs.size == 0

    def test_contains(self):
        items = ['A', 'B', 'C']
        hs = HashSet(items)
        for item in items:
            assert item in hs

        assert 'D' not in hs
        assert 'E' not in hs

    def test_union(self):
        set_1 = HashSet([1, 2, 3, 4])
        set_2 = HashSet([1, 5, 6])

        union = set_1 + set_2

        assert len(union) == 6
        assert 5 in union
        assert 7 not in union
        union.remove(1)
        assert 1 not in union
        assert len(union) == 5

    def test_intersection(self):
        set_1 = HashSet([1, 2, 3, 4])
        set_2 = HashSet([1, 2, 5, 6])

        intersection = set_1 & set_2

        assert 1 in intersection
        assert len(intersection) == 2
        assert 2 in intersection
        assert 3 not in intersection

    def test_difference(self):
        set_1 = HashSet([1, 2, 3, 4])
        set_2 = HashSet([1, 2, 5, 6])

        diff = set_1 - set_2

        assert len(diff) == 2
        assert 3 in diff
        assert 1 not in diff
        assert 2 not in diff


    def test_is_subset(self):
        hs = HashSet([1, 2, 3, 4, 5, 6, 7, 8])

        assert HashSet([1, 2, 3]).is_subset(hs)
        assert not HashSet([11]).is_subset(hs)

        assert not hs.is_subset([11])
