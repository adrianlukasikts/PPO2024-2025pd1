print("Zadanie 4")

pasazer1 = Pasazer()
pasazer2 = Pasazer()
assert isinstance(pasazer1, Czlowiek)
assert str(pasazer1) == "Jestem pasazerem"

przystanek1 = Przystanek([pasazer1, pasazer2])
assert przystanek1.getLudzie() == [pasazer1, pasazer2]

przystanek2 = Przystanek()
assert przystanek2.getLudzie() is None

automat = Automat()
assert automat.jakiKoszt(1.70) == 20
assert automat.jakiKoszt(2.20) == 75
assert not pasazer1.czyMamBilet()
assert not pasazer2.czyMamBilet()

assert automat.sprzedajBilet(pasazer1, 2.23) == "Nie udalo sie sprzedac biletu za podana cene"
assert not pasazer1.czyMamBilet()

assert automat.sprzedajBilet(pasazer1, 2.20) == "Sprzedano bilet pasaerowi za podana cene"
assert pasazer1.czyMamBilet()

kierowca = Kierowca()
assert isinstance(kierowca, Czlowiek)
assert str(kierowca) == "Jestem kierowca"

autobus = Autobus(kierowca)
assert autobus.getKierowca() == kierowca
assert autobus.getUczestnicy() == None

konduktor = Konduktor()
assert isinstance(konduktor, Czlowiek)
assert str(konduktor) == "Jestem konduktorem"

przystanek1.doAutobusu(autobus)
assert autobus.getUczestnicy() == [pasazer1, pasazer2]
assert przystanek1.getLudzie() is None

autobus.dodajUczestnika(konduktor)
assert autobus.getUczestnicy() == [pasazer1, pasazer2, konduktor]

assert konduktor.skontroluj(pasazer1) == "Dziekuje za okazanie biletu"
assert konduktor.skontroluj(pasazer2) == "Niestety musze wystawic mandat za brak biletu"

autobus.wypuscUczestnikow(przystanek2)
assert autobus.getUczestnicy() is None
assert przystanek2.getLudzie() == [pasazer1, pasazer2, konduktor]
