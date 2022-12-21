class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def transform(x):
            ans = 0
            while x != 1:
                if not x%2: x /= 2
                else: x = 3*x+1
                ans += 1
            return ans
        
        answers_dict = dict()
        #answers_dict = {num: transform(num) for num in range(lo, hi+1)}
        for num in range(lo, hi+1):
            answers_dict[num] = transform(num)
        answers_dict = dict(sorted(answers_dict.items(), key=lambda item: item[1]))
        print(answers_dict)
        return list(answers_dict.keys())[k-1]