from math import ceil
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            strings = []
            new_s = ""
            for i in range(len(s)//k):
                strings.append(s[i*k:(i+1)*k])
            if len(s)//k != len(s)/k:
                strings.append(s[-(len(s)%k):])
            for num in strings:
                new_s = new_s+str(sum([int(n) for n in num]))
            s = new_s
        return s