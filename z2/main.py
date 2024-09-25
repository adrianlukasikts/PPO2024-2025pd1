print("Zadanie 2")

ksiazki = [
    Potop(1),
    Potop(2),
    Dziady(3),
    Balladyna(4),
    Lalka(5)
]

potop1 = ksiazki[0]
assert potop1.get_id() == 1
assert potop1.get_autor() == "Henryk Sienkiewicz"

potop2 = ksiazki[1]
assert potop2.get_id() == 2
assert potop2.get_autor() == "Henryk Sienkiewicz"

dziady = ksiazki[2]
assert dziady.get_id() == 3
assert dziady.get_autor() == "Adam Mickiewicz"

balladyna = ksiazki[3]
assert balladyna.get_id() == 4
assert balladyna.get_autor() == "Juliusz Slowacki"

lalka = ksiazki[4]
assert lalka.get_id() == 5
assert lalka.get_autor() == "Boleslaw Prus"

uzytkownicy = [Uzytkownik(0), Uzytkownik(1)]

assert uzytkownicy[0].get_id() == 0
assert uzytkownicy[0].get_id_wypozyczonych_ksiazek() == []
assert uzytkownicy[1].get_id() == 1
assert uzytkownicy[1].get_id_wypozyczonych_ksiazek() == []

biblioteka = Biblioteka(uzytkownicy, ksiazki)

biblioteka.get_uzytkownik(0).wypozycz(1)
biblioteka.get_uzytkownik(0).wypozycz(4)
assert biblioteka.get_uzytkownik(0).get_id_wypozyczonych_ksiazek() == [1, 4]

biblioteka.get_uzytkownik(0).oddaj(4)
assert biblioteka.get_uzytkownik(0).get_id_wypozyczonych_ksiazek() == [1]

biblioteka.get_uzytkownik(1).wypozycz(4)
assert biblioteka.get_uzytkownik(1).get_id_wypozyczonych_ksiazek() == [4]

biblioteka.get_uzytkownik(1).wypozycz(2)
biblioteka.get_uzytkownik(1).wypozycz(3)
biblioteka.get_uzytkownik(1).wypozycz(5)
assert biblioteka.get_uzytkownik(1).get_id_wypozyczonych_ksiazek() == [4, 2, 3, 5]

biblioteka.get_uzytkownik(1).oddaj(2)
assert biblioteka.get_uzytkownik(1).get_id_wypozyczonych_ksiazek() == [4, 3, 5]
