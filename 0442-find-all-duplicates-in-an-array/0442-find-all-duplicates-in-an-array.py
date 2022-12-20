class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = dict(Counter(nums).most_common())
        return [num for num, count in c.items() if count == 2]