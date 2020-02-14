
class Codec:
    mapping = {}
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    unique = 0

    def encode(self, longUrl: str) -> str:
        id = self.unique
        self.unique += 1
        self.mapping[id] = longUrl

        if id == 0:
            return '0'

        digits = []
        while id > 0:
            remainder = id % 62
            digits.append(remainder)
            id = id // 62

        res = ''
        for digit in digits:
            res += self.chars[digit]

        return res

    def decode(self, shortUrl: str) -> str:
        res = 0

        for char in shortUrl:
            res += self.chars.index(char)

        return self.mapping[res]


c = Codec
print(c.decode(c, c.encode(c, 'http://blablabla.com')))
