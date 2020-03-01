from models import Leerling, Klas
from klas_view import KlasView

if __name__ == "__main__":
    jos = Leerling(1, 'Jos', 'Anthonissen')
    jan = Leerling(2, 'Jan', 'Van Dijck')
    klas_5itn = Klas('5ITN', [jos, jan])

    view = KlasView(klas_5itn)
    view.print()

    print()
    view.sorteerveld = 'voornaam'
    view.print()
