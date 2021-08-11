import time
import randomstring
import classok

a = randomstring.nev()
b = randomstring.emil()
c = randomstring.passw()

def test_popular_tags():  # Népszerű tegek.
    lap = classok.TestSign_upLap()
    lap.setup()
    time.sleep(2)
    log = lap.test_01_reg_mezok(a, b, c, "")
    time.sleep(2)
    lap.teardown()  # A regisztráció bezár.
    lap = classok.TestSign_inLap()  # A bejelentkezés nyit.
    lap.setup()
    time.sleep(2)
    log = log and lap.bejelentkezik(b, c)
    log = log and lap.popular_tags()
    lap.kijelentkezik()
    lap.teardown()
    assert log  # Vannak popular tegek (legalább 2), kiírta csv-be.

