from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.my_dict = []

    def __setitem__(self, key: Any, value: Any) -> None:
        for member in self.my_dict:
            if member[0] == key:
                member[1] = value
                return
        self.my_dict += [[key, value]]

    def __getitem__(self, key: Any) -> Any:
        for member in self.my_dict:
            if member[0] == key:
                return member[1]
        raise KeyError(f"Key {key} is not found")

    def __len__(self) -> int:
        amount = 0
        for member in self.my_dict:
            if member:
                amount += 1
        return amount

    def __clear__(self) -> None:
        keys = []
        for k in self.my_dict:
            keys += [k]
        for key in keys:
            del self.my_dict[key]

    def __delitem__(self, key: Any) -> None | str:
        for k in self.my_dict:
            if k == key:
                del self.my_dict[key]
            else:
                return "Error: key not found"

    def get(self, key: Any) -> bool:
        for k in self.my_dict:
            if k == key:
                return True
        return False

    def pop(self, key: Any) -> Any:
        result = 0
        goal = False
        for k in self.my_dict:
            if k == key:
                result = self.my_dict[k]
                goal = True
                break
        if not goal:
            return "Error: key not found"
        del self.my_dict[key]
        return result

    def update(self, key: Any, value: Any) -> None:
        amount = 0
        count = 0
        for k in self.my_dict:
            if k == key:
                self.my_dict[k] = value
                break
            if k != key:
                amount += 1
                count += 1
        if count == amount:
            self.my_dict[key] = value

    def __iter__(self) -> Any:
        return self


class Node:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.hash = hash(key)
        self.value = value


class HashTable:
    def __init__(self) -> None:
        self.hash_table = []

    def get_insert(self, key: Any, value: Any) -> None:
        node = Node(key, value)
        self.hash_table.append(node)

    def get_find(self, key: Any) -> Any:
        key_hash = hash(key)
        for node in self.hash_table:
            if node.hash == key_hash and node.key == key:
                return node.value
            else:
                return None
