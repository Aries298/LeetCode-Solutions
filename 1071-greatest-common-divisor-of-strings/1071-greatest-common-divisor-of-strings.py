class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            longer, shorter = str1, str2
        else:
            longer, shorter = str2, str1
        if shorter not in longer:
            return ""
        for i in range(len(longer)):
            if not longer.replace(shorter[:len(shorter)-i],"") and not shorter.replace(shorter[:len(shorter)-i],""):
                return shorter[:len(shorter)-i]
        return ""