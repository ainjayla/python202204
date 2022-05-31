class Person:

    gender = ('M', 'F')

    def __init__(self, isikukood):
        self.isikukood = isikukood

    def getBirthYear(self):
        year = 0
        if self.isikukood[0] == '3' or self.isikukood[0] == '4':
            year = 1900
        elif self.isikukood[0] == '5' or self.isikukood[0] == '6':
            year = 2000
        return str(int(self.isikukood[1:3]) + year)

    def getBirthMonth(self):
        return self.isikukood[3:5]

    def getBirthDay(self):
        return self.isikukood[5:7]

    def getGender(self):
        if int(self.isikukood[0]) % 2 == 0:
            return self.gender[1]
        return self.gender[0]
