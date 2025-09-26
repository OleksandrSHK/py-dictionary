from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8  # initial capacity
        self.hash_table = [None] * self.capacity  # pre-selected list
        self.length = 0  # numbers of elements
        self.DELETED = object()

    def resize(self) -> None:
        old_table = self.hash_table
        self.capacity *= 2
        self.hash_table = [None] * self.capacity
        self.length = 0
        for node in old_table:
            if node is not None:
                self.__setitem__(node[0], node[2])

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.length >= int(self.capacity * 2 / 3):
            self.resize()

        key_hash = hash(key)
        index = key_hash % self.capacity
        node = [key, key_hash, value]

        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                self.hash_table[index][2] = value
                return
            index = (index + 1) % self.capacity
        self.hash_table[index] = node
        self.length += 1

    def __getitem__(self, key: Any) -> Any:
        key_hash = hash(key)
        index = key_hash % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return self.hash_table[index][2]
            index = (index + 1) % self.capacity
        raise KeyError(f"Key {key} is not found")

    def __len__(self) -> int:
        return self.length

    def clear(self) -> None:
        self.capacity = 8
        self.hash_table = [None] * self.capacity
        self.length = 0

    def __delitem__(self, key: Any) -> None:
        key_hash = hash(key)
        index = key_hash % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                self.hash_table[index] = self.DELETED
                self.length -= 1
                return
            index = (index + 1) % self.capacity
        raise KeyError(f"Key {key} is not found")

    def get(self, key: Any, default: Any = None) -> Any | None:
        key_hash = hash(key)
        index = key_hash % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return self.hash_table[index][2]
            index = (index + 1) % self.capacity
        return default

    def pop(self, key: Any, default: Any = None) -> Any:
        key_hash = hash(key)
        index = key_hash % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                result = self.hash_table[index][2]
                self.hash_table[index] = self.DELETED
                self.length -= 1
                return result
            index = (index + 1) % self.capacity
        return default

    def update(self, other: Any = None, kwargs: Any = None) -> None:
        if other is not None:
            try:
                for key in other:
                    value = other[key]
                    self.__setitem__(key, value)
            except TypeError:
                for pair in other:
                    key = pair[0]
                    value = pair[1]
                    self.__setitem__(key, value)
        if kwargs is not None:
            for key in kwargs:
                value = kwargs[key]
                self.__setitem__(key, value)

    def __iter__(self) -> None:
        for node in self.hash_table:
            if node is not None:
                yield node[0]
