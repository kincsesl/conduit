import time
import randomstring
import classok

a = randomstring.nev()
b = randomstring.emil()
c = randomstring.passw()


def test_reg_mezok01():  # Érvényes regisztráció + bejelentkezés.
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
    lap.kijelentkezik()
    lap.teardown()
    assert log  # Működik a bejelentkezés.
