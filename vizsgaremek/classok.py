import time
import lokatorok
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
            time.sleep(3)
            self.sikerablak()
            log = self.successful.text == lokatorok.sikerszoveg
            self.successful_okgomb.click()
            self.driver.refresh()  # Újratöltöm az ablakot (nem tudom, miért, de így megy).
            time.sleep(2)
            self.egyiklogout = self.driver.find_elements_by_xpath(lokatorok.logout) # Logoutolok
            self.masiklogout = self.driver.find_elements_by_xpath(lokatorok.logout0) # Logoutolok
            if len(self.egyiklogout)>0:
                self.egyiklogout[0].click()
            elif len(self.egyiklogout)>0:
                self.masiklogout[0].click()
            else:
                log = False
        return log


class TestSign_inLap(object):  # A bejelentkezés teszteléséhez.
    def setup(self):
        self.options = Options()
        self.options.headless = True
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
        return len(self.driver.find_elements_by_xpath(lokatorok.logout)) > 0