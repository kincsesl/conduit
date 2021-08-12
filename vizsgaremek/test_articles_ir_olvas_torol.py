import classok
import time

name = "Harry Potter"
emil = "potter@roxfort.en"
password = "Hermione1"


def test_articles_ir_olvas_torol():
    lap = classok.Test_articles()
    lap.setup()
    log = True
    lap.regisztral(name, emil, password)
    log = log and lap.bejelentkezik(emil, password)  # Belép, és a New Article oldalra lép.
    lap.article_oldal()  # Rálép az Article oldalra.
    for i in range(10):
        hanyadik = str(i)
        title = hanyadik + ". title"
        about = hanyadik + ". about"
        write = hanyadik + ". write"
        tags = hanyadik + ".tag"
        comment = hanyadik + ". comment"
        log = log and lap.add_article(title, about, write, tags, comment)
        time.sleep(2)
    lap.kileptet()
    lap.teardown()
    assert log

# print(test_articles_ir_olvas_torol())
