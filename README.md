# MVC

Model View Controller

- De **Model**-classes worden geïmplementeerd met `dataclass` en staan in een aparte module
    - Ze dienen enkel om de (opgeslagen) gegevens (`Leerling` en `Klas`) de juiste structuur te geven
    - Ze weten niets over de **Views** of de **Controllers**
- De **View**-class (`KlasView`) gebruikt de models om op de console een (configureerbaar) weergave (view) te tonen
    - **Views** kennen enkel de bijpassende **Models** omdat ze deze moeten kunnen weergeven
    - **Views** houden zelf enkel tijdelijk **Model**-classes bij (soms zelfs enkel **ViewModels**)
    - Het **View** kent zelf niets v.d. **Controller**
- Er is nog geen echte Controller-klas (zie experiments) maar:
    - De **Controller** handelt de *events* v.d. gebruiker af
    - De **Controller** kent de **Model**-classes en kan deze opvragen, filteren, ...
    - De **Controller** kent de **View**-classes en stuurt een gepast **Model**-object naar een gepast **View**-object

# Experimenten

De experimenten zijn telkens op zichzelf staande bestanden om een concept uit te proberen:

- `pickle_try`: Met de `pickle`-module van Python kunnen objecten (en zelfs object-hiërarchieën) in een bestand worden opgeslagen
- `cli`: Wissen v.h. console-scherm kan op de meeste OS'n met het commando `clear`
- `klas_controller`: Hoe een `KlasController`-class er uit zou kunnen zien

# TODO

- Refactor de applicatie zodat gebruik wordt gemaakt van een `KlasController`.
- In `main.py` kan daarna een interactief menu getoond worden met b.v. volgende opties:
    - Voeg leerling toe
    - Wijzig bestaande leerling
    - Sla wijzigingen op (pickle)
    - Laad de gegevens van schijf (pickle)
    - ...
- Denk telkens na waar welke functionaliteit thuishoort en/of hoe ze opgesplitst kan worden, b.v.
    - De gebruiker geeft aan de Controller de instructie om de huidige gegevens op te slaan 
      maar de controller kan dit gedeeltelijk uitbesteden aan andere classes, b.v. de Model-classes
    - Het weergeven van een menu is eigenlijk geen taak van de `KlasController`.
      
# Inzichtvragen

- Hoe dikwijls wordt een nieuw `KlasController`-object geïnstantieerd en wanneer wordt dit objecten vernietigd?
- Hoe dikwijls wordt een `KlasView`-object geïnstantieerd en wanneer wordt dit object weer vernietigd?
- Welke toestand houdt een `KlasView` bij?
- Welk gedrag heeft een `KlasView`? (Op welke manier moet het dus gebruikt worden?)
- Is er in Python een manier om duidelijk te maken dat van een `KlasView`-object de `sorteerveld`-property nog mag veranderd worden
  maar dat het misschien beter is om de `klas`-property niet te veranderen en in de plaats een nieuw object te maken? 
  (TIP: `@property`, zie https://docs.python.org/3/library/functions.html#property)



