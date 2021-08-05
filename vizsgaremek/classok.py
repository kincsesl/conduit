import time
import lokatorok
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestSign_upLap(object):
    def setup(self):
        self.options = Options()
        #self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.signuplap)
        self.username = self.driver.find_element_by_xpath(lokatorok.username)
        self.emil = self.driver.find_element_by_xpath(lokatorok.emil)
        self.password = self.driver.find_element_by_xpath(lokatorok.password)
        self.submit = self.driver.find_element_by_xpath(lokatorok.submit)  # Sign up felirat.

    def teardown(self):  # Lerombolás.
        pass
        #self.driver.close()

    def hibaablak(self):
        self.felirat = self.driver.find_element_by_xpath(lokatorok.failed)
        self.reszlet = self.driver.find_element_by_xpath(lokatorok.reszlet)
        self.failed_okgomb = self.driver.find_element_by_xpath(lokatorok.failed_okgomb)
        # self.userhiba = locators.userhiba  # 4 elemű lista.

    def sikerablak(self):
        self.welcome = self.driver.find_element_by_xpath(lokatorok.welcome)
        self.successful = self.driver.find_element_by_xpath(lokatorok.successful)
        self.successful_okgomb = self.driver.find_element_by_xpath(lokatorok.successful_okgomb)

    def test_01_rossz_mezok(self, a, b, c, d):
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
        time.sleep(1)
        self.hibaablak()
        log = self.reszlet.text == d
        self.failed_okgomb.click()
        self.driver.close()
        return log
