MORSE_DICT = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        def convert_to_morse(word):
            ans = ''
            for letter in word:
                ans += MORSE_DICT[letter]
            return ans
        
        unique = set()
        for word in words:
            unique.add(convert_to_morse(word))
        return len(unique)