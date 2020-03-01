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
    