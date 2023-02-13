class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if not low % 2: low += 1
        if not high % 2: high -= 1
        return int((high-low)/2) + 1