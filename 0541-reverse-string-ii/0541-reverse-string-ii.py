from math import ceil
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans, size = '', 2 * k
        for i in range(ceil(len(s)/size)):
            curr = s[i*size:i*size+size]
            s1, s2 = curr[:k], curr[k:] 
            ans += ''.join(list(reversed(s1)))+s2
        return ans