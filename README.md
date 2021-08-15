A tesztfájlok a viszgaremek mappában vannak:

test_nyitolinkek.py:
    (Nincs a POM-ban.)
    test_1: Elfogadtatja a cookie-kat, utána már nem jelenhet meg a cookie-s gomb.
    test_2: Ide-oda kattint a Home, a SignIn és a SignUp linkekre, majd visszalép.

test_signup_rosszak.py:
    test_reg_mezok01-03: A megfelelő mező üresen hagyásával nézi, hogy megjelenik-e a várt hiba.
    (A 04 ismétlődő eset volt.)
    test_reg_mezok05: A Password mező érvénytelen kitöltése után ellenőrzi a hibaüzenetet.

test_signup_jok.py:
    test_reg_mezok01(): Érvényes adatokkal regisztrál, nézi, megjelenik-e a sikeres regisztráció üzenete,
                        belép, kiléptet.

test_popular_tags_listazasa.py:
    test_popular_tags(): Érvényes adatokkal regisztrál, nézi, megjelenik-e a
                             sikeresregisztráció üzenete, belép, ellenőrzi, van-e legalább
                             2 Popular Tags, ezeket a populars.cs-be kiírja, kiléptet.
test_settings_oda-vissza.py:
    test_settings_mindenfele():
                            Regisztrál egy adattal, amit a veletlen_adatok.csv 1. sorából vesz.
                            Belép
                            Átírja a nevet és a jelszót a Settingsben. Kilép
                            Belép az új jelszóval
                            Visszaírja a nevet és a jelszót
                            Kilép
                            Belép a régi adatokkal
test_articles_ír_olvas_töröl.py
    def test_articles_ir_olvas_torol():
                              Regisztrál, belép. 10 cikket fölrak
                              ellenőrzi a meglétüket a title és az about jellemzőikkel
                              végigjárva a cikkek több lapos listáját.
Egyéb fájlok
vizsgaremek.ppt
populars.csv: Belépés után ide listáztattam ki a Popular tags tartalmát.
classok.py, classok_utolso.py: Az objektumosztályokat tartalmazzák.
lokatorok.py: az egyes weblapelemek helyét tartalmazó változók találhatók itt.
mi-micsoda: a feljegyzéseim.
veletlen_adatok_csvbe.py veletlen_adatok.csv: saját készítésű függvénnyel véletlen adatokat írtam fájlba.
randomstring.py: saját véletlenfüggvény (magyar, angol nevek, e-mailek ill. jelszavak)

A lefedett funkciók
+Regisztráció
+Bejelentkezés
+Adatkezelési nyilatkozat használata
+Adatok listázása
+Több oldalas lista bejárása
+Új adat bevitel
+Ismételt és sorozatos adatbevitel adatforrásból
+Meglévő adat módosítása
+Adat vagy adatok törlése
+Adatok lementése felületről
+Kijelentkezés