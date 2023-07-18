class LRUCache:

    def __init__(self, capacity: int):
        self.cpty = capacity
        self.data = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.data: return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data: self.data.pop(key)
        self.data[key] = value
        if len(self.data) > self.cpty: 
            self.data.popitem(last=False)