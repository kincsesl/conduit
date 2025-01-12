import time

import lokatorok
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def cookies(driv):
    time.sleep(2)
    kuki = driv.find_elements_by_xpath("/html/body/div/footer/div/div/div/div[2]/button[2]/div")
    if len(kuki) > 0:
        kuki[0].click()
    time.sleep(2)


def fejlecobjektumok(driv):
    navbar = driv.find_element_by_xpath(lokatorok.navigacios)
    listam = navbar.find_elements_by_tag_name("li")
    szotar = {}
    for listaelem in listam:
        kulcs = listaelem.text.replace("&nbsp", "").replace(" ", "")
        szotar[kulcs] = listaelem.find_element_by_tag_name("a")
    return szotar


def vanlogout(driv):
    navbar = driv.find_element_by_xpath(lokatorok.navigacios)
    listam = navbar.find_elements_by_tag_name("li")
    log = False
    for listaelem in listam:
        log = log or listaelem.text.find("Log out") > 0
    return log


def vanarticle(driv):
    navbar = driv.find_element_by_xpath(lokatorok.navigacios)
    listam = navbar.find_elements_by_tag_name("li")
    log = False
    for listaelem in listam:
        log = log or listaelem.text.find("Article") > 0
    return log


class TestSign_upLap(object):  # A regisztráció teszteléséhez.
    def setup(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.signuplap)
        cookies(self.driver)
        self.username = self.driver.find_element_by_xpath(lokatorok.username)
        self.emil = self.driver.find_element_by_xpath(lokatorok.emil)
        self.password = self.driver.find_element_by_xpath(lokatorok.password)
        self.submit = self.driver.find_element_by_xpath(lokatorok.submit)  # Sign up gomb a felpattanóban.

    def teardown(self):  # Lerombolás.
        self.driver.close()

    def hibaablak(self):
        self.felirat = self.driver.find_element_by_xpath(lokatorok.failed)
        self.reszlet = self.driver.find_element_by_xpath(lokatorok.reszlet)
        self.failed_okgomb = self.driver.find_element_by_xpath(lokatorok.failed_okgomb)
        # self.userhiba = locators.userhiba  # 4 elemű lista.

    def sikerablak(self):
        self.welcome = self.driver.find_element_by_xpath(lokatorok.welcome)
        self.successful = self.driver.find_element_by_xpath(lokatorok.successful)
        self.successful_okgomb = self.driver.find_element_by_xpath(lokatorok.successful_okgomb)

    def test_01_reg_mezok(self, a, b, c, d):
        if a == "":
            self.submit.click()
        elif b == "":
            self.username.send_keys(a)
            self.submit.click()
        elif c == "":
            self.username.send_keys(a)
            self.emil.send_keys(b)
            self.submit.click()
        else:
            self.username.send_keys(a)
            self.emil.send_keys(b)
            self.password.send_keys(c)
            self.submit.click()
        time.sleep(3)
        if d != "":
            self.hibaablak()
            log = self.reszlet.text == d
            self.failed_okgomb.click()
        else:
            self.sikerablak()
            log = self.successful.text == lokatorok.sikerszoveg
            self.successful_okgomb.click()
            self.driver.refresh()  # Újratöltöm az ablakot (nem tudom, miért, de így megy).
            time.sleep(1)
            """
            Hol kiléptetne, hol nem
            self.egyiklogout = self.driver.find_elements_by_xpath(lokatorok.logout) # Logoutolok
            self.masiklogout = self.driver.find_elements_by_xpath(lokatorok.logout0) # Logoutolok
            if len(self.egyiklogout)>0:
                self.egyiklogout[0].click()
            elif len(self.egyiklogout)>0:
                self.masiklogout[0].click()
            else:
                log = False
            """
        return log


class TestSign_inLap(object):  # A bejelentkezés teszteléséhez.
    def setup(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.signinlap)
        cookies(self.driver)
        self.emil = self.driver.find_element_by_xpath(lokatorok.signin_emil)
        self.password = self.driver.find_element_by_xpath(lokatorok.signin_password)
        self.submit = self.driver.find_element_by_xpath(lokatorok.signin_gomb)  # Sign in felirat.

    def teardown(self):  # Lerombolás.
        self.driver.close()

    def bejelentkezik(self, a, b):
        self.emil.send_keys(a)
        self.password.send_keys(b)
        self.submit.click()
        time.sleep(3)
        self.driver.refresh()
        return vanlogout(self.driver)

    def kijelentkezik(self):
        return fejlecobjektumok(self.driver)["Logout"].click()
        # return len(self.driver.find_elements_by_xpath(lokatorok.logout0)) > 0 or len(self.driver.find_elements_by_xpath(lokatorok.logout)) > 0
        # return vanlogout(self.driver)

    def popular_tags(self):
        self.popular = self.driver.find_element_by_xpath(lokatorok.popular_div)  # A divje
        self.lista = self.popular.find_elements_by_tag_name("a")  # A tagok.
        self.sztring = ""
        for elem in self.lista:  # Kiíratom az elemeket.
            self.sztring += elem.text + ";"
        self.sztring = self.sztring[0:len(self.sztring) - 1]  # Törlöm az utolsó pontosvesszőt.
        with open("populars.csv", "w") as file:
            file.write(self.sztring)
        return len(self.lista) > 2


class Test_signup_settings(object):
    def setup(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)

    def regisztral(self, a, b, c):
        self.driver.get(lokatorok.signuplap)
        cookies(self.driver)
        self.username = self.driver.find_element_by_xpath(lokatorok.username)
        self.emil = self.driver.find_element_by_xpath(lokatorok.emil)
        self.password = self.driver.find_element_by_xpath(lokatorok.password)
        self.submit = self.driver.find_element_by_xpath(lokatorok.submit)  # Sign up felirat.
        self.username.send_keys(a)
        self.emil.send_keys(b)
        self.password.send_keys(c)
        self.submit.click()  # Regisztrál.
        time.sleep(2)
        van_e_ok = self.driver.find_elements_by_xpath(lokatorok.successful_okgomb)
        if len(van_e_ok) > 0:
            van_e_ok[0].click()  # Siker, OK.
        if vanlogout(self.driver):  # Kiléptet, ha van Logout.
            fejlecobjektumok(self.driver)["Logout"].click()

    def bejelentkezik(self, a, b):
        self.driver.get(lokatorok.signinlap)
        time.sleep(1)
        self.emil = self.driver.find_element_by_xpath(lokatorok.signin_emil)
        self.password = self.driver.find_element_by_xpath(lokatorok.signin_password)
        self.submit = self.driver.find_element_by_xpath(lokatorok.signin_gomb)  # Sign in felirat.
        self.emil.send_keys(a)
        self.password.send_keys(b)
        # self.submit.click()
        time.sleep(2)
        return vanlogout(self.driver)  # Ha van, akkor belépett.

    def settingek(self, w, x, z):
        fejlecobjektumok(self.driver)["Settings"].click()
        time.sleep(1)
        self.name = self.driver.find_element_by_xpath(lokatorok.settings_name)
        self.bio = self.driver.find_element_by_xpath(lokatorok.settings_bio)
        self.password = self.driver.find_element_by_xpath(lokatorok.settings_password)
        self.submitgomb = self.driver.find_element_by_xpath(lokatorok.settings_submit)
        self.name.clear()  # Kitöltöm új adatokkal.
        self.name.send_keys(w)
        self.bio.clear()
        self.bio.send_keys(x)
        self.password.clear()
        self.password.send_keys(z)
        self.submitgomb.click()
        time.sleep(3)
        self.success = self.driver.find_elements_by_xpath(lokatorok.settings_updatesuccessfull)
        # if vanlogout(self.driver):  # Kiléptet, ha van Logout.
        #   fejlecobjektumok(self.driver)["Logout"].click()
        # self.driver.refresh()
        if len(self.success) > 0:
            self.success[0].click()
            return True
        else:
            return False

    def teardown(self):  # Lerombolás.
        self.driver.close()


class Test_articles(object):
    def setup(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)

    def regisztral(self, a, b, c):
        self.driver.get(lokatorok.signuplap)
        cookies(self.driver)
        self.username = self.driver.find_element_by_xpath(lokatorok.username)
        self.emil = self.driver.find_element_by_xpath(lokatorok.emil)
        self.password = self.driver.find_element_by_xpath(lokatorok.password)
        self.submit = self.driver.find_element_by_xpath(lokatorok.submit)  # Sign up felirat.
        self.username.send_keys(a)
        self.emil.send_keys(b)
        self.password.send_keys(c)
        self.submit.click()  # Regisztrál.
        time.sleep(5)
        van_e_ok = self.driver.find_elements_by_xpath(lokatorok.successful_okgomb)
        if len(van_e_ok) > 0:
            van_e_ok[0].click()  # Siker, OK.
        if vanlogout(self.driver):  # Kiléptet, ha van Logout.
            fejlecobjektumok(self.driver)["Logout"].click()

    def bejelentkezik(self, a, b):
        self.driver.get(lokatorok.signinlap)
        time.sleep(2)
        self.emil = self.driver.find_element_by_xpath(lokatorok.signin_emil)
        self.password = self.driver.find_element_by_xpath(lokatorok.signin_password)
        self.submit = self.driver.find_element_by_xpath(lokatorok.signin_gomb)  # Sign in felirat.
        self.emil.send_keys(a)
        self.password.send_keys(b)
        self.submit.click()
        time.sleep(2)
        if vanarticle(self.driver):
            return True
        else:
            return False

    def article_oldal(self):
        self.driver.get(lokatorok.article_url)

    def add_article(self, a, b, c, d, e):
        def kitolt(webobjektum, x):
            webobjektum.clear()
            webobjektum.send_keys(x)

        fejlecobjektumok(self.driver)["NewArticle"].click()
        kitolt(self.driver.find_element_by_xpath(lokatorok.article_title), a)  # Kitölti az adatokkal
        kitolt(self.driver.find_element_by_xpath(lokatorok.article_about), b)
        kitolt(self.driver.find_element_by_xpath(lokatorok.article_write), c)
        kitolt(self.driver.find_element_by_xpath(lokatorok.article_tags), d)
        time.sleep(1)
        self.driver.find_element_by_xpath(lokatorok.article_publishgomb).click()  # Publikálja
        fejlecobjektumok(self.driver)["NewArticle"].click()
        return vanarticle(self.driver)

    def sajat_cikkek_listaja(self, a, b):
        self.driver.get(lokatorok.nyitolap)
        if not vanlogout(self.driver):
            self.bejelentkezik(a, b)
        self.driver.get(lokatorok.nyitolap)
        time.sleep(2)
        self.lapozogombok = self.driver.find_elements_by_xpath(lokatorok.cikk_oldalgombok)
        self.cikkeim = []
        self.i = 0
        for gomb in self.lapozogombok:  # Végigmegy a lapokon.
            gomb.click()
            self.i += 1
            time.sleep(2)
            # Minden cikk div-je: article-preview
            self.cikkek = self.driver.find_elements_by_xpath(lokatorok.cikk_cikkek)
            for self.cikk in self.cikkek:
                self.szovege = self.cikk.text
                self.tulaj = self.szovege[0:self.szovege.find("\n")]
                self.listaelem = []
                if self.tulaj == "HarryPotter":
                    self.listaelem.append(str(self.i))
                    self.listaelem.append(self.cikk.find_element_by_tag_name("h1").text)
                    self.listaelem.append(self.cikk.find_element_by_tag_name("p").text)
                    self.cikkeim.append(self.listaelem)
        return self.cikkeim

    def cikket_torol(self, nev, n):
        self.driver.get(lokatorok.nyitolap)
        time.sleep(2)
        self.driver.find_elements_by_xpath(lokatorok.cikk_oldalgombok)[n - 1].click  # Rányom az n. oldalra.
        self.cikkek = self.driver.find_elements_by_xpath(lokatorok.cikk_cikkek)
        for self.cikk in self.cikkek:
            self.szovege = self.cikk.text
            self.tulaj = self.szovege[0:self.szovege.find("\n")]
            if self.tulaj == "HarryPotter":  # Megtalálja az első saját cikket.
                self.cikk.find_element_by_tag_name("h1").click()
                time.sleep(3)
                #Törli a cikket.
                self.driver.find_element_by_xpath("//button[@class = 'btn btn-outline-danger btn-sm']").click()
                self.driver.refresh() # A rossz üzit figyelmen kívül hagyja.
                break  # Az első után abbahagyja.

    def kileptet(self):
        if vanlogout(self.driver):  # Kiléptet, ha van Logout.
            fejlecobjektumok(self.driver)["Logout"].click()

    def teardown(self):  # Lerombolás.
        self.driver.close()