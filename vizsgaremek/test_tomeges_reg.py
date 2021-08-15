import time
import class_utolso


def beolvas():
    lista = []
    with open("veletlen_adatok.csv", "r") as file:  # Beolvassa az első sort
        for sor in file:
            sor = sor[0:len(sor) - 1]
            allista = sor.split(";")
            lista.append(allista)
    return lista


def test_reg_mezok01():  # Érvényes regisztráció + bejelentkezés.
    adatsorok = beolvas()
    lap = class_utolso.TestSign_upLap()
    lap.setup()
    time.sleep(2)
    log = True
    for adatsor in adatsorok:
        a = adatsor[0]
        b = adatsor[1]
        c = adatsor[2]
        log = log and lap.regisztral(a, b, c)  # Regisztrál
        time.sleep(2)
    lap.teardown()
    assert log  # Működik a bejelentkezés.

