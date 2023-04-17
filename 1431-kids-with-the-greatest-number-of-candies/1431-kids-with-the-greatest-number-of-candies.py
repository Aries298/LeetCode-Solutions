class Solution:
    def kidsWithCandies(self, a: List[int], k: int) -> List[bool]:
        return [True if(max(a)<=i+k) else False for i in a]