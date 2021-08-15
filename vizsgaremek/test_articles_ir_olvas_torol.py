import classok
import time

name = "HarryPotter"
emil = "potter@roxfort.en"
password = "Hermione1"


def test_articles_ir_olvas_torol():
    hanycikk = 10
    lap = classok.Test_articles()
    lap.setup()
    log = True
    lap.regisztral(name, emil, password) # Ha megvan már a felhasználó, úgyis átugorja ezt nemes egyszerűséggel.
    log = log and lap.bejelentkezik(emil, password)  # Belép, és a New Article oldalra lép.
    lap.article_oldal()  # Rálép az Article oldalra.
    for i in range(hanycikk):
        hanyadik = str(i + 1)
        title = hanyadik + ". title"
        about = hanyadik + ". about"
        write = hanyadik + ". write"
        tags = hanyadik + ".tag"
        comment = hanyadik + ". comment"
        log = log and lap.add_article(title, about, write, tags, comment)
        time.sleep(2)
    cikkeim_oldallal = lap.sajat_cikkek_listaja(emil, password)
    hany_volt = len(cikkeim_oldallal)
    cikkeim = []
    for cikk in cikkeim_oldallal:
        lista = []
        lista.append(cikk[1])
        lista.append(cikk[2])
        cikkeim.append(lista)
    print(cikkeim)
    for i in range(hanycikk):  # Ellenőrzi a cikkek title és about jellemzőjét.
        hanyadik = str(i + 1)
        lista = []
        title = hanyadik + ". title"
        about = hanyadik + ". about"
        lista.append(title)
        lista.append(about)
        log = log and lista in cikkeim
    oldalszamok = []
    for i in range(len(cikkeim_oldallal)):
        oldalszamok.append(cikkeim_oldallal[i][0])
    oldalszamok.sort()
    # oldalszamok[0] Az első oldal, ahol cikkem van, ezek közül az elsőt törlöm.
    lap.cikket_torol(name, int(oldalszamok[0]))
    cikkeim_oldallal = lap.sajat_cikkek_listaja(emil, password)
    hany_lett = len(cikkeim_oldallal)
    log = log and hany_lett < hany_volt  # Kevesebb lett.
    lap.kileptet()
    lap.teardown()
    assert log
