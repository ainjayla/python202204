class Athlete:

    muudparameetrid = {}

    def __init__(self, eesnimi, perenimi, vanus, sugu, pikkus, kaal):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.vanus = vanus
        self.sugu = sugu
        self.pikkus = pikkus
        self.kaal = kaal

    def perform(self):
        pass

    def __str__(self):
        return self.eesnimi + ' ' + self.perenimi +\
               ', vanus: ' + str(self.vanus) +\
               ', sugu: ' + self.sugu + ', pikkus: ' +\
               str(self.pikkus) + ', kaal: ' + str(self.kaal)

class Skydiver(Athlete):

    def perform(self):
        print('Olen valjaspool lennukit ja uritan ellu jaada')

class Runner(Athlete):

    def perform(self):
        print('Jooksen nii kuis jaksan')