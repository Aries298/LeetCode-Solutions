import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted_string = []
        s = s.lower()
        for letter in s:
            if letter in string.ascii_lowercase or letter in string.digits:
                converted_string.append(letter)
        if len(converted_string) % 2:
            t1 = int(len(converted_string)/2)
            t2 = t1 + 1
            return converted_string[:t1] == converted_string[t2:][::-1]
        else:
            t1 = int(len(converted_string)/2)
            return converted_string[:t1] == converted_string[t1:][::-1]