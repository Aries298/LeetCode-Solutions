from itertools import permutations
class Solution:
    def minimumSum(self, num: int) -> int:
        perms = list(permutations(str(num)))
        pairs = [(x[0]+x[1], x[2]+x[3]) for x in perms]
        lowest_sum = 1000
        for pair in pairs:
            pair_sum = int(pair[0]) + int(pair[1])
            if pair_sum < lowest_sum:
                lowest_sum = pair_sum
        return lowest_sum