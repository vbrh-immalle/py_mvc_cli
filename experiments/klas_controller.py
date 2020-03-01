import operator
from dataclasses import dataclass

@dataclass
class Leerling:
    klasnummer: int
    voornaam: str
    naam: str

@dataclass
class Klas:
    naam: str
    leerlingen: [Leerling]
    # new_leerling_policy: str

    def add_leerling(self, leerling: Leerling):
        # TODO: automatische hernummering van klasnummers?
        # B.v. m.b.v. `self.new_leerling_policy`:
        #   - achteraan toevoegen
        #   - hernummeren op basis van achternaam
        pass



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



class KlasController:

    def __init__(self):
        # dummy gegevens, kan afkomstig zijn van database, pickle-file, ...
        # Dit is normaal de plaats waar de Controller aan de storage-laag de gegevens opvraagt
        jos = Leerling(1, 'Jos', 'Anthonissen')
        jan = Leerling(2, 'Jan', 'Van Dijck')
        klas_5itn = Klas('5ITN', [jos, jan])
        
        self.klas = klas_5itn

    def print_gesorteerd_klasnummer(self):
        klasview = KlasView(self.klas, 'klasnummer')
        klasview.print()

    def print_gesorteerd_voornaam(self):
        klasview = KlasView(self.klas, 'voornaam')
        klasview.print()

    def voeg_leerling_toe(self, leerling: Leerling):
        # self.klas.leerlingen.append(...)
        
        # of is voeg_leerling_toe(self, klasnummer, voornaam, achternaam) beter?
        #   dan hoeft de aanroeper niets over de Leerling-modelclass te weten!
        #   maar het maakt de Controller dan wel verantwoordelijk voor eventuele fouten op te sporen in de gegevens

        pass
        # Wat indien het systeem zelf de klasnummering moet aanpassen? 
        # Waar moeten we dit doen? Is dit de verantwoordelijkheid van de Controller?
        #   Waarschijnlijk best in Klas-modelclass: uitbreiden van een @dataclass is mogelijk!
        #   En een leerling toevoegen, wijzigt het Model dus dit zou de juiste plek kunnen zijn!


if __name__ == "__main__":
    while True:
        print("1. Toon klas gesorteerd op klasnummer")
        print("2. Toon klas gesorteerd op voornaam")
        print("3. Voeg leerling toe")
        print("4. Stop programma")
        keuze = int(input("Keuze: "))

        controller = KlasController()

        if keuze == 1:
            print()
            controller.print_gesorteerd_klasnummer()
            print()
        elif keuze == 2:
            print()
            controller.print_gesorteerd_voornaam()
            print()
        elif keuze == 3:
            pass
        elif keuze == 4:
            print()
            break

    print("Tot ziens!")
