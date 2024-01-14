import collections

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        diff = []
        spectrum = {}
        spectrum2 = {}
        for index in range(len(word1)):
            spectrum[word1[index]] = spectrum.get(word1[index], 0) + 1
            spectrum2[word2[index]] = spectrum2.get(word2[index], 0) + 1
            if word1[index] != word2[index]:
                diff.append(index)
        if len(diff) == 2:
            if word1[diff[0]] == word2[diff[1]] and word1[diff[1]] == word2[diff[0]]:
                return True
            return False
        else:
            if set(word1) != set(word2):
                return False
            count1, count2 = collections.Counter(word1), collections.Counter(word2)
            return sorted(count1.values()) == sorted(count2.values())
        
        

        