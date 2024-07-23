class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return [item for sublist in [[num] * count for num, count in list(reversed(Counter(sorted(nums)).most_common()))] for item in sublist]
