class MyHashSet:

    def __init__(self):
        self.arry=[[] for _ in range(1000)]

    def add(self, key: int) -> None:
        subkey=key%1000
        if not self.contains(key):
            self.arry[subkey].append(key)
        

    def remove(self, key: int) -> None:
        subkey=key%1000
        if self.contains(key):
            self.arry[subkey].remove(key)
    def contains(self, key: int) -> bool:
        subkey=key%1000
        return key in self.arry[subkey]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)