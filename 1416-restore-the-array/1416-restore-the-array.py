class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp=dict()
        mod=10**9+7
        def rec(ind,k):
            if ind==len(s):
                return 1
            if s[ind]=="0":
                return 0
            if ind not in dp:    
                val=0 
                ans=0   
                for i in range(ind,len(s)):
                    val*=10
                    val+=int(s[i])
                    if val>0 and val<=k:
                        ans+=rec(i+1,k)
                    else:
                        break    
                dp[ind]=ans%mod        
            return dp[ind]
        return rec(0,k)           