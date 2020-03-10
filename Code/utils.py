from hashtable import HashTable


class DefaultTable(HashTable):
    def __init__(self, default):
        self.default = default
        super().__init__()

    def __str__(self):
        return f'(DefaultTable, (value={self.default})' + super().__str__() + ')'

    def __missing__(self, key):
        self[key] = self.default()()

        return self[key]
