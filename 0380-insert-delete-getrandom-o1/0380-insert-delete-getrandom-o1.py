from random import sample
class RandomizedSet:

    def __init__(self):
        self.RandomizedSet = set()

    def insert(self, val: int) -> bool:
        if val in self.RandomizedSet:
            return False
        else:
            self.RandomizedSet.add(val)
            return True

    def remove(self, val: int) -> bool:
        try:
            self.RandomizedSet.remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        return sample(self.RandomizedSet, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()