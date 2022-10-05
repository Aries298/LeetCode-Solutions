import numpy
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        tmp = [int(num) for num in str(n)]
        return prod(tmp)-sum(tmp)