def test_signup_rosszak():
    import time

    import randomstring
    import lokatorok
    import classok


    def test_rossz_mezok01():
        lap = classok.TestSign_upLap()
        lap.setup()
        time.sleep(2)
        assert lap.test_01_rossz_mezok("", "", "", lokatorok.userhiba[0])
        time.sleep(2)
        lap.teardown()


    def test_rossz_mezok02():
        lap = classok.TestSign_upLap()
        lap.setup()
        time.sleep(2)
        assert lap.test_01_rossz_mezok(randomstring.nev(), "", "", lokatorok.userhiba[1])
        time.sleep(2)
        lap.teardown()


    def test_rossz_mezok03():
        lap = classok.TestSign_upLap()
        lap.setup()
        time.sleep(2)
        assert lap.test_01_rossz_mezok(randomstring.nev(), randomstring.emil(), "", lokatorok.userhiba[2])
        time.sleep(2)
        lap.teardown()


    def test_rossz_mezok04():
        lap = classok.TestSign_upLap()
        lap.setup()
        time.sleep(2)
        assert lap.test_01_rossz_mezok(randomstring.nev(), randomstring.emil(), "", lokatorok.userhiba[2])
        time.sleep(2)
        lap.teardown()


    def test_rossz_mezok05():
        lap = classok.TestSign_upLap()
        lap.setup()
        time.sleep(2)
        assert lap.test_01_rossz_mezok(randomstring.nev(), randomstring.emil(), randomstring.name(), lokatorok.userhiba[3])
        time.sleep(2)
        lap.teardown()
