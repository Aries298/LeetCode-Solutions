class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans1=[]
        ans2=[]
        for i in s:
            if i=='#':
                if len(ans1)>0:
                    ans1.pop()
            else:
                ans1.append(i)
        for  i in t:
            if i=='#':
                if len(ans2)>0:
                    ans2.pop()
            else:
                ans2.append(i)

        return ans1==ans2