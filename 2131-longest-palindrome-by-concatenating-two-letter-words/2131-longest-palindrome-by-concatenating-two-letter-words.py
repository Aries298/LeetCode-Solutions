class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        words = dict(Counter(words))
        words = [[k, v] for k, v in words.items()]
        print(words)
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if words[i][0] == words[j][0][::-1]:
                    count = min(words[i][1],words[j][1])
                    ans += 2 * count * len(words[i][0])
                    words[i][1] -= count
                    words[j][1] -= count

        print(words)

        words = [x for x in words if len(set(x[0])) == 1]

        print(words)

        for i in range(len(words)):
            if words[i][1]:
                count = words[i][1] // 2
                words[i][1] %= 2
                ans += 2 * count * len(words[i][0])
        print(words)

        max_single_length = max([len(x) for x in words if len(set(x[0])) == 1 and x[1] > 0], default=0)
        print(max_single_length)
        ans += max_single_length
        return ans