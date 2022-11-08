class Solution:
    def makeGood(self, s: str) -> str:
        while True:
            to_del = []
            if len(s) > 1:
                prev = s[0]
            else:
                return s
            for i in range(1, len(s)):
                curr = s[i]
                if curr != prev and curr.lower() == prev.lower() and i-1 not in to_del:
                    to_del.extend([i-1, i])
                prev = curr
            s = ''.join([letter for i,letter in enumerate(s) if i not in to_del])
            if not to_del:
                break
        return s