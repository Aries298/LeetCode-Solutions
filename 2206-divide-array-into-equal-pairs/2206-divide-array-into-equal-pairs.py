class Solution:
    def divideArray(self, nums) -> bool:
        c = list(Counter(nums).most_common())
        for count in c:
            if count[1] % 2:
                return False
        return True