print("Zadanie 3")

polska = Polska()
niemcy = Niemcy()
czechy = Czechy()
slowacja = Slowacja()
ukraina = Ukraina()
bialorus = Bialorus()
litwa = Litwa()
rosja = Rosja()

assert isinstance(polska, PanstwoEuropejskie)
assert isinstance(niemcy, PanstwoEuropejskie)
assert isinstance(czechy, PanstwoEuropejskie)
assert isinstance(slowacja, PanstwoEuropejskie)
assert isinstance(ukraina, PanstwoEuropejskie)
assert isinstance(bialorus, PanstwoEuropejskie)
assert isinstance(litwa, PanstwoEuropejskie)
assert isinstance(rosja, PanstwoAzjatyckie)

assert isinstance(polska, Panstwo)
assert isinstance(niemcy, Panstwo)
assert isinstance(czechy, Panstwo)
assert isinstance(slowacja, Panstwo)
assert isinstance(ukraina, Panstwo)
assert isinstance(bialorus, Panstwo)
assert isinstance(litwa, Panstwo)
assert isinstance(rosja, Panstwo)

assert polska.get_kontynent() == Kontynent.EUROPA
assert polska.get_liczba_ludnosci() == 37750000
assert polska.get_stolica() == "Warszawa"

assert rosja.get_kontynent() == Kontynent.AZJA
assert rosja.get_liczba_ludnosci() == 143400000
assert rosja.get_stolica() == "Moskwa"

assert polska.get_sasiedzi() == []

polska.dodaj_sasiada(niemcy)
polska.dodaj_sasiada(czechy)
polska.dodaj_sasiada(slowacja)
polska.dodaj_sasiada(ukraina)
polska.dodaj_sasiada(bialorus)
polska.dodaj_sasiada(litwa)
polska.dodaj_sasiada(rosja)

assert polska.get_sasiedzi() == [niemcy, czechy, slowacja, ukraina, bialorus, litwa, rosja]

rosja.migruj(polska, 1000000)

assert rosja.get_liczba_ludnosci() == 142400000
assert polska.get_liczba_ludnosci() == 38750000
