from Koer import *

class TeenistusKoer(Koer):

    def jahi(self):
        print(self.nimi, 'peab jahti')

    def haugu(self):
        print('Teenistuskoerad ei haugu')

    def __str__(self):
        return 'Objekt ' + self.nimi + ' on klassi TeenistuKoer isend'