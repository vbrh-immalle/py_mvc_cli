import models
import operator

class KlasView:

    def __init__(self, klas_model, sorteerveld='klasnummer'):
        self.klas = klas_model
        self.sorteerveld = sorteerveld

    def print(self):
        klasnaam = self.klas.naam
        aantal_lln = len(self.klas.leerlingen)
        s = f'{self.klas.naam}: {aantal_lln} leerlingen [gesorteerd op {self.sorteerveld}]'
        print(s)
        print('='*len(s))

        leerlingen_gesorteerd = sorted(self.klas.leerlingen, key=operator.attrgetter(self.sorteerveld))

        for leerling in leerlingen_gesorteerd:
            print(leerling)

