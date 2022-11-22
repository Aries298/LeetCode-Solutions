class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter(nums).most_common()
        c = [t for t in c if not t[0] % 2]
        c = [t for t in c if t[1] == c[0][1]]
        if c: 
            return sorted(c)[0][0]
        else:
            return -1
        