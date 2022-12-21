class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:        
        letters_dict = dict()
        for i, letter in enumerate(s):
            if letter in letters_dict and i - letters_dict[letter] - 1 != distance[ord(letter)-ord('a')]: return False
            else: letters_dict[letter] = i
        return True