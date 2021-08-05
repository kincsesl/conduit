from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class Nyitolap(object):
    def setup(self):
        self.options = Options()
        # self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("http://localhost:1667/#/")

    def test_cookies(self, a):  # 1: nem fogad el, 2: elfogad cookie-t
        try:
            self.kuki = self.driver.find_elements_by_xpath(
                "/html/body/div/footer/div/div/div/div[2]/button[" + str(a) + "]/div")
            if len(self.kuki) > 0:
                self.kuki[0].click()
            return True
        except:
            return False

    def test_nincs_cookigomb(self):
        self.kuki1 = self.driver.find_elements_by_xpath("/html/body/div/footer/div/div/div/div[2]/button[1]/div")
        self.kuki2 = self.driver.find_elements_by_xpath("/html/body/div/footer/div/div/div/div[2]/button[2]/div")
        return len(self.kuki1) + len(self.kuki2) == 0

    def test_ide_oda_kattint(self):  # Vizsgálja a Home, a Sign in és a Sign up linkek működését.
        try:
            self.navlinkek = self.driver.find_elements_by_class_name("nav-link")
            self.navlinkek[2].click()
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            self.navlinkek[1].click()
            time.sleep(2)
            self.driver.back()
            return True
        except:
            return False

nyitolap = Nyitolap()


def test_1():
    nyitolap.setup()
    assert nyitolap.test_cookies(2)  # Elfogadja a Cookie-kat.
    assert nyitolap.test_nincs_cookigomb()  # Ha elfogadtam, már nincs Cookie-gomb.
    nyitolap.driver.close()

def test_3():
    nyitolap.setup()
    assert nyitolap.test_ide_oda_kattint()
    nyitolap.driver.close()



