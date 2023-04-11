class Solution:
    def removeStars(self, s: str) -> str:
        ans=''
        for i in range(len(s)):
            if s[i].isalpha():
                ans=s[i]+ans
            else:
                ans=ans.replace(ans[0],'',1)
        return ans[::-1]
