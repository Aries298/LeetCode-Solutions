class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size1, size2 = len(word1), len(word2)
        ans = []
        ptr = 0
        while ptr < min(size1, size2):
            ans.append(word1[ptr])
            ans.append(word2[ptr])
            ptr += 1
        if size1 > size2:
            bigger = word1
        else:
            bigger = word2
            
        for i in range(ptr, len(bigger)):
            ans.append(bigger[i])
            
        return ''.join(ans)
        