class Codec:
    def __init__(self):
        self.code_dict = dict()
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        code = ''
        for _ in range(10):
            code += random.choice(string.ascii_lowercase)
        self.code_dict[code] = longUrl
        return '''http://tinyurl.com/''' + code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code_dict[shortUrl[-10:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))