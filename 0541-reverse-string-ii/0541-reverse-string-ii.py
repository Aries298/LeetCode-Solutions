from math import ceil
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        
        for i in range(ceil(len(s)/(2*k))):
            curr = s[i*(2*k):i*(2*k)+(2*k)]
            s1 = curr[:k]
            s2 = curr[k:]
            ans += ''.join(list(reversed(s1)))+s2
        return ans