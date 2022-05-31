class Koer:

    nina = 'marg'

    # konstruktoriga, mis votab sisendparameetrina nime
    def __init__(self, nimi):
        self.nimi = nimi

    def haugu(self):
        print(self.nimi, 'haugub')

    def muuda_nime(self, nimi):
        self.nimi = nimi

    def tagasta_nimi(self):
        return self.nimi

    def __str__(self):
        return 'Objekt ' + self.nimi + ' on klassi Koer isend'

    def __eq__(self, other):
        if isinstance(other, Koer):
            if other.nina == self.nina:
                return True
        return False

    def __add__(self, other):
        if isinstance(other, Koer):
            return self.nimi + '_' + other.nimi
        return None