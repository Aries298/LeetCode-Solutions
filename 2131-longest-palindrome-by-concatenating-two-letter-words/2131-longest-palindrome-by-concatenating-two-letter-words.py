class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        words = [[k, v] for k, v in (dict(Counter(words))).items()]
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if words[i][0] == words[j][0][::-1]:
                    count = min(words[i][1],words[j][1])
                    ans += 2 * count * len(words[i][0])
                    words[i][1] -= count
                    words[j][1] -= count
        words = [x for x in words if len(set(x[0])) == 1]
        for i in range(len(words)):
            if words[i][1]:
                count = words[i][1] // 2
                words[i][1] %= 2
                ans += 2 * count * len(words[i][0])
        max_single_length = max([len(x) for x in words if len(set(x[0])) == 1 and x[1] > 0], default=0)
        ans += max_single_length
        return ans