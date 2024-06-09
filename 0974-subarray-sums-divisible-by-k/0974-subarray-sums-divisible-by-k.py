class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_dict = collections.defaultdict(int)
        prefix_dict[0] = 1
        curr, count = 0, 0
        for num in nums:
            curr = (curr + num) % k
            count += prefix_dict[curr]
            prefix_dict[curr] += 1
        return count