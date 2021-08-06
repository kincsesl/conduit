import time
import randomstring
import classok

"""
def test_reg_mezok01():
    lap = classok.TestSign_upLap()
    lap.setup()
    time.sleep(3)
    assert lap.test_01_reg_mezok(randomstring.nev(), randomstring.emil(), randomstring.passw(), "")
    time.sleep(3)
    lap.teardown()
"""

a = randomstring.nev()
b = randomstring.emil()
c = randomstring.passw()


def test_reg_mezok01():  # Érvényes regisztráció + bejelentkezés.
    lap = classok.TestSign_upLap()
    lap.setup()
    time.sleep(3)
    log = lap.test_01_reg_mezok(a, b, c, "")
    time.sleep(3)
    lap.teardown()  # A regisztráció bezár.
    lap = classok.TestSign_inLap()  # A bejelentkezés nyit.
    lap.setup()
    time.sleep(3)
    log = log and lap.bejelentkezik(b, c)
    assert log
    lap.teardown()

