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
    lap.regisztral(name, emil, password)
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
    cikkeim = lap.sajat_cikkek_listaja(emil, password)
    for i in range(hanycikk):
        hanyadik = str(i + 1)
        lista = []
        title = hanyadik + ". title"
        about = hanyadik + ". about"
        lista.append(title)
        lista.append(about)
        log = log and lista in cikkeim
    lap.kileptet()
    lap.teardown()
    return log


assert test_articles_ir_olvas_torol()
