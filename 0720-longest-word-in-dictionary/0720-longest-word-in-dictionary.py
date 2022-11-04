class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = []
        for word in words:
            curr = word
            found = True
            for i in range(len(word)-1):
                #print(word[:len(word)-1-i])
                if word[:len(word)-1-i] in words:
                    continue
                else:
                    found = False
                    break
            if found:
                ans.append(word)
        ans = [x for x in ans if len(x) == len(max(ans,key=len))]
        if ans:
            return sorted(ans)[0]
        else:
            return ''