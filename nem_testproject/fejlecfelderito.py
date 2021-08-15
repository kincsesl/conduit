import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)
driver.get("http://localhost:1667/#/")


def fejlecobjektumok(driv):
    navbar = driv.find_element_by_xpath("/html/body/div/nav/div/ul")
    listam = navbar.find_elements_by_tag_name("li")
    szotar = {}
    for listaelem in listam:
        szotar[listaelem.text] = listaelem.find_element_by_tag_name("a")
    return szotar

def vanlogout(driv):
    navbar = driv.find_element_by_xpath("/html/body/div/nav/div/ul")
    listam = navbar.find_elements_by_tag_name("li")
    log = False
    for listaelem in listam:
        log = log or listaelem.text.find("Log out") > 0
    return log

time.sleep(15)

print(vanlogout(driver))