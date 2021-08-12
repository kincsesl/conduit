import classok
import time

uj_name = "Én vagyok"
uj_bio = "Vagyok, aki vagyok."
uj_password = "Asdfghj1"


def beolvas():
    with open("veletlen_adatok.csv", "r") as file:  # Beolvassa az első sort
        sor = file.readline()
        return sor.split(";")


def test_settings_mindenfele():
    lista = beolvas()
    a = lista[0]
    b = lista[1]
    c = lista[2]
    lap = classok.Test_signup_settings()
    lap.setup()
    time.sleep(2)
    lap.regisztral(a, b, c)  # Regisztrál, kilépteti magát.
    log = lap.bejelentkezik(b, c)  # Belép a fenti adatokkal.
    log = log and lap.settingek(uj_name, uj_bio, uj_password)  # Átírja a mezőket.
    log = log and lap.bejelentkezik(b, uj_password)  # Belép az új adatokkal.
    log = log and lap.settingek(a, uj_bio, c)  # Visszaírja a régi adatokat, a biót hagyja.
    log = log and lap.bejelentkezik(b, c)  # Belép a régi adatokkal.
    assert log


