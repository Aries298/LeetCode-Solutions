class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        for letter in s:
            if s.lower() != s.upper():
                if ans:
                    ans = [word+letter.lower() for word in ans] + [word+letter.upper() for word in ans]
                else:
                    ans = [letter.lower(), letter.upper()]
            else:
                if ans:
                    ans = [word+letter for word in ans]
                else:
                    ans = [letter]
        return list(set(ans))