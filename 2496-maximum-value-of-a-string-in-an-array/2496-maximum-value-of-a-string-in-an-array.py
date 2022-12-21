class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max([int(word) if word.isnumeric() else len(word) for word in strs])