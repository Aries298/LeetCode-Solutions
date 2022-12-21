class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        return list({min(r) for r in matrix} & {max(c) for c in zip(*matrix)})