class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i = 0
        j = 0
        m, n = len(word1), len(word2)
        p = 0 # track elements inside word1[i]
        q = 0 # track elements inside word2[j]
        r = 0 # track max length of word1[i], word2[j]
        while i < m and j < n:
            # how max we can cover current words
            max_len = max(len(word1[i]), len(word2[j]))
            # always start with max(p, q)
            # ex: ab, c and a, bc 
            r = max(p, q)
            while r < max_len:
                if word1[i][p] != word2[j][q]:
                    return False
                p += 1
                q += 1
                r += 1
                # move to next index if curr size is reached
                if p == len(word1[i]):
                    i += 1
                    p = 0
                
                # move to next index if curr size is reached
                if q == len(word2[j]):
                    j += 1
                    q = 0
                if i == m and j == n:
                    return True
                elif i == m and p == 0:
                    # we still have elements in word2
                    return False
                elif j == n and q == 0:
                    # we still have elements in word1
                    return False