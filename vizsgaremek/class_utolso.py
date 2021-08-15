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


class TestSign_upLap(object):  # A regisztráció teszteléséhez.
    def setup(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.signuplap)
        cookies(self.driver)

    def teardown(self):  # Lerombolás.
        self.driver.close()

    def regisztral(self, a, b, c):
        self.driver.get(lokatorok.signuplap)
        self.username = self.driver.find_element_by_xpath(lokatorok.username)
        self.emil = self.driver.find_element_by_xpath(lokatorok.emil)
        self.password = self.driver.find_element_by_xpath(lokatorok.password)
        self.submit = self.driver.find_element_by_xpath(lokatorok.submit)  # Sign up gomb a felpattanóban.
        self.username.send_keys(a)
        self.emil.send_keys(b)
        self.password.send_keys(c)
        self.submit.click()
        time.sleep(5)
        self.driver.refresh()  # Újratöltöm az ablakot (nem tudom, miért, de így megy).
        time.sleep(2)
        if vanlogout(self.driver):  # Kiléptet, ha van Logout.
            fejlecobjektumok(self.driver)["Logout"].click()
        self.driver.get(lokatorok.signinlap)
        time.sleep(2)
        self.emil = self.driver.find_element_by_xpath(lokatorok.signin_emil)
        self.password = self.driver.find_element_by_xpath(lokatorok.signin_password)
        self.submit = self.driver.find_element_by_xpath(lokatorok.signin_gomb)  # Sign up gomb a felpattanóban
        self.emil.send_keys(b)
        self.password.send_keys(c)
        self.submit.click()
        time.sleep(3)
        self.driver.refresh()
        log = vanlogout(self.driver)
        if log:  # Kiléptet, ha van Logout.
            fejlecobjektumok(self.driver)["Logout"].click()
        return log
