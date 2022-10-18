class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(n):
            ans = []
            curr = n[0]
            count = 1
            for i in range(1, len(n)):
                if n[i] == curr:
                    count += 1
                else:
                    ans.append(str(count))
                    ans.append(str(curr))          
                    count = 1
                    curr = n[i]
            ans.append(str(count))
            ans.append(str(curr))   
            return ''.join(ans)
        i = 1
        ans = "1"
        while i < n:
            ans = helper(ans) 
            i += 1
        return ans