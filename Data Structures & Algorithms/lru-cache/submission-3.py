class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.cache = []
        
    def get(self, key: int) -> int:
        if key in self.map:
            self.cache.remove(key)
            self.cache.append(key)
            return self.map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.cache.remove(key)
            self.map[key] = value
            self.cache.append(key)
        elif len(self.map) < self.capacity:
            self.map[key] = value
            self.cache.append(key)
        else:
            ele = self.cache.pop(0)
            del self.map[ele]
            self.map[key] = value
            self.cache.append(key)
