digits_dict = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}




class Solution:
    def letterCombinations(self, digits: str):
        digits = reversed([digits_dict[num] for num in list(digits)])
        ans = []
        for letter_set in digits:
            new_list = []
            for letter in letter_set:
                added = False
                if ans:
                    for letter_set in ans:
                        new_list.append(letter + letter_set)
                else:
                    added = True
                    ans = list(letter_set)
                    break
            if not added:
                ans = new_list
        return ans