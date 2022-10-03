class Solution:
    def longestCommonPrefix(self, strs) -> str:
        longest_prefix = strs[0]
        if len(strs) == 1:
            return longest_prefix
        for word in strs[1:]:
            if not longest_prefix:
                return ""
            for i in range(len(longest_prefix)):
                try:
                    print(i)
                    if word[i] != longest_prefix[i]:
                        longest_prefix = longest_prefix[:i]
                        break
                except:
                    longest_prefix = longest_prefix[:i]
                    break
        return longest_prefix