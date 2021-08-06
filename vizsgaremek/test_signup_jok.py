import time
import randomstring
import classok


def test_reg_mezok01():
    lap = classok.TestSign_upLap()
    lap.setup()
    time.sleep(2)
    assert lap.test_01_reg_mezok(randomstring.nev(), randomstring.emil(), randomstring.passw(), "")
    time.sleep(2)
    lap.teardown()

