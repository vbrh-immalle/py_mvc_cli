import pickle
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


if __name__ == "__main__":
    jos = Leerling(1, 'Jos', 'Anthonissen')
    jan = Leerling(2, 'Jan', 'Van Dijck')
    klas_5itn = Klas('5ITN', [jos, jan])

    print(jos)
    print(jan)
    print(klas_5itn)

    # save
    with open('klas_5itn.pickle', 'wb') as f:
        #pickle.dump(klas_5itn, f)
        pickle.Pickler(f).dump(klas_5itn)
    
    # load
    klas = None
    with open('klas_5itn.pickle', 'rb') as f:
        #klas = pickle.load(f)
        klas = pickle.Unpickler(f).load()

    print(klas)