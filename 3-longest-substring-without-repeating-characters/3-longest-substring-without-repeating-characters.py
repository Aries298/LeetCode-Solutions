class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        biggest_num = 0
        if not str:
            return 0
        for x in range(len(s)):
            stringlist = []
            for y in range(x, len(s)):
                if s[y] not in stringlist:
                    stringlist.append(s[y])
                    if biggest_num < len(stringlist):
                        biggest_num = len(stringlist)
                else:
                    break
        return biggest_num