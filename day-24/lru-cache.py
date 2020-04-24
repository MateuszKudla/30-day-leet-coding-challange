class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.key = []
        self.dictionary = {}
        

    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return -1
        else:
            del self.key[self.key.index(key)]
            self.key.insert(0, key)

            return self.dictionary[key]


    def put(self, key: int, value: int) -> None:
        if self.capacity > self.count:
            if key not in self.dictionary:
                self.count += 1
            else:
                del self.key[self.key.index(key)]

            self.dictionary[key] = value
            self.key.insert(0, key)
        else:
            if key in self.dictionary:
                del self.key[self.key.index(key)]

                self.dictionary[key] = value
                self.key.insert(0, key)
                return 

            del self.dictionary[self.key.pop()]
            self.dictionary[key] = value
            self.key.insert(0, key)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))