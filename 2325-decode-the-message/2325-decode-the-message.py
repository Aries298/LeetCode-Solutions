class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
        keys = []
        seen = set()
        for letter in list(key.replace(' ', '')):
            if letter in seen:
                pass
            else:
                keys.append(letter)
                seen.add(letter)
        
        dic = dict(map(lambda i,j : (i,j) , keys, letters))
        dic[' '] = ' '
        ans = ''
        for letter in message:
            ans += dic[letter]
            
        return ans