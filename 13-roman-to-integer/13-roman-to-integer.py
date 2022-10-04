class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        s = list(s)
        for i in range(len(s)):
            previd = max(0, i-1)
            if s[i] == 'M':
                try:
                    if s[previd] == 'C':
                        ans += 800
                        continue
                    else:
                        ans += 1000
                        continue
                except:
                    ans += 1000

            elif s[i] == 'D':
                try:
                    if s[previd] == 'C':
                        ans += 300
                        continue
                    else:
                        ans += 500
                        continue
                except:
                    ans += 500

            elif s[i] == 'C':
                try:
                    if s[previd] == 'X':
                        ans += 80
                        continue
                    else:
                        ans += 100
                        continue
                except:
                    ans += 100

            elif s[i] == 'L':
                try:
                    if s[previd] == 'X':
                        ans += 30
                        continue
                    else:
                        ans += 50
                        continue
                except:
                    ans += 50

            elif s[i] == 'X':
                try:
                    if s[previd] == 'I':
                        ans += 8
                        continue
                    else:
                        ans+=10
                except:
                    ans += 10

            elif s[i] == 'V':
                try:
                    if s[previd] == 'I':
                        ans += 3
                        continue
                    else:
                        ans += 5
                        continue
                except:
                    ans += 5

            elif s[i] == 'I':
                ans += 1
        return ans