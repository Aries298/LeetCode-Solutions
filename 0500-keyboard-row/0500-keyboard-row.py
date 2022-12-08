first = 'qwertyuiop'
second = 'asdfghjkl'
third = 'zxcvbnm'

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def analyse_word(word):
            rows = [0,0,0]
            for letter in word:
                if letter in first:
                    rows[0] = 1
                elif letter in second:
                    rows[1] = 1
                elif letter in third:
                    rows[2] = 1
            return sum(rows) == 1
        
        return [word for word in words if analyse_word(word)]
            