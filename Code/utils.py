from hashtable import HashTable


class DefaultTable(HashTable):
    def __init__(self, default):
        self.default = lambda: default
        super().__init__()

    def __missing__(self, key):
        self[key] = self.default()()

        return self[key]
