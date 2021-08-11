import time
import lokatorok
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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


class TestSign_upLap(object):  # A regisztráció teszteléséhez.
    def setup(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.signuplap)
        self.username = self.driver.find_element_by_xpath(lokatorok.username)
        self.emil = self.driver.find_element_by_xpath(lokatorok.emil)
        self.password = self.driver.find_element_by_xpath(lokatorok.password)
        self.submit = self.driver.find_element_by_xpath(lokatorok.submit)  # Sign up felirat.

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
        #self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.signinlap)
        self.emil = self.driver.find_element_by_xpath(lokatorok.signin_emil)
        self.password = self.driver.find_element_by_xpath(lokatorok.signin_password)
        self.submit = self.driver.find_element_by_xpath(lokatorok.signin_gomb)  # Sign up felirat.

    def teardown(self):  # Lerombolás.
        self.driver.close()

    def bejelentkezik(self, a, b):
        self.emil.send_keys(a)
        self.password.send_keys(b)
        self.submit.click()
        time.sleep(3)
        self.driver.refresh()
        return vanlogout(self.driver)
        fejlecobjektumok(self.driver)["Logout"].click()
        # return len(self.driver.find_elements_by_xpath(lokatorok.logout0)) > 0 or len(self.driver.find_elements_by_xpath(lokatorok.logout)) > 0
        # return vanlogout(self.driver)

    def popular_tags(self):
        self.popular = self.driver.find_element_by_xpath(lokatorok.popular_div)  # A divje
        self.lista = self.popular.find_elements_by_tag_name("a")  # A tagok.
        return len(self.lista) > 0
