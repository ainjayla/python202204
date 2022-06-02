import sys

class Raamat:

    def __init__(self, filename):
        file = open(filename, encoding='UTF-8')
        self.content = file.read().splitlines()
        file.close()

    def getWordsCount(self):
        count = 0
        for row in self.content:
            words = row.strip().split()
            # variant 1
            for word in words:
                count += 1
            # variant 2
            # count += len(words)
        return count

    def getRowsCount(self):
        return len(self.content)

    def keeraYmber(self):
        ret = ''
        for row in self.content:
            ret += row + '\n'
        return ret[::-1]