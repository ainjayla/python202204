class Crypto:

    def __init__(self, keyfile):
        self.__key = {}
        file = open(keyfile, encoding = 'UTF-8')
        for row in file:
            chars = row.strip().split(',')
            self.__key[chars[0].strip()] = chars[1].strip()
        file.close()

    def encode(self, message):
        ret = ''
        for char in message:
            if char in self.__key:
                ret += self.__key[char]
            else:
                ret += char
        return ret

    def decode(self, message):
        ret = ''
        keys = list(self.__key.keys())
        values = list(self.__key.values())
        for char in message:
            if char in keys:
                ret += keys[values.index(char)]
            else:
                ret += char
        return ret