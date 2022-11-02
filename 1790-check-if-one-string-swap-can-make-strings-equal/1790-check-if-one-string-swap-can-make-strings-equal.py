class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if set(s1) != set(s2):
            return False
        idxs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                idxs.append(i)
        if len(idxs) != 2:
            return False
        s2 = list(s2)
        s2[idxs[0]], s2[idxs[1]] = s2[idxs[1]], s2[idxs[0]]
        if ''.join(s2) == s1:
            return True
        else:
            return False
