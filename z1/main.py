print("Zadanie 1")

smok = Smok()
assert smok.get_punkty_zycia() == 1000
assert isinstance(smok, Postac)

rycerz = Rycerz(500, 50)
assert rycerz.get_punkty_zycia() == 500
assert rycerz.get_sila() == 50
assert isinstance(rycerz, Postac)
assert isinstance(rycerz, Walczaca)

druid = Druid(250, 100)
assert druid.get_punkty_zycia() == 250
assert druid.get_mana() == 100
assert isinstance(druid, Postac)
assert isinstance(druid, Leczaca)

smok.atakuj(rycerz)
assert rycerz.get_punkty_zycia() == 400

smok.atakuj(rycerz)
assert rycerz.get_punkty_zycia() == 300

druid.wylecz(rycerz)
assert rycerz.get_punkty_zycia() == 500
assert druid.get_mana() == 90

druid.wylecz(rycerz)
assert rycerz.get_punkty_zycia() == 700

druid.atakuj(smok)
assert smok.get_punkty_zycia() == 999

rycerz.atakuj(smok)
assert smok.get_punkty_zycia() == 949

rycerz.atakuj(smok)
assert smok.get_punkty_zycia() == 899

rycerz.atakuj(smok)
assert smok.get_punkty_zycia() == 849
