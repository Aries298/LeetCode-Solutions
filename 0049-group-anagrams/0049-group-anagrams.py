class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        words_dict = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in words_dict:
                words_dict[key].append(word)
            else:
                words_dict[key] = [word]
        return list(words_dict.values())