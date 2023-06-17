class Solution:
    mod = 10**9 + 7
    table = []

    def numOfWays(self, nums):
        n = len(nums)
        self.table = [[0] * n for _ in range(n)]

        for i in range(n):
            self.table[i][0] = self.table[i][i] = 1

        for i in range(2, n):
            for j in range(1, i):
                self.table[i][j] = (self.table[i - 1][j - 1] + self.table[i - 1][j]) % self.mod

        arrList = nums
        return (self.helper(arrList) - 1) % self.mod

    def helper(self, arr):
        n = len(arr)
        if n < 3:
            return 1

        leftNodes = []
        rightNodes = []
        for i in range(1, n):
            element = arr[i]
            if element < arr[0]:
                leftNodes.append(element)
            else:
                rightNodes.append(element)

        leftWays = self.helper(leftNodes) % self.mod
        rightWays = self.helper(rightNodes) % self.mod

        return (((leftWays * rightWays) % self.mod) * self.table[n - 1][len(leftNodes)]) % self.mod
