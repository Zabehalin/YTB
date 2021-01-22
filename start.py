
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import random
import re


def main():
    # =============== User Agent =====================
    U_ag = random.choice(list(open('user-agents.txt')))
    U_ag = U_ag[0:-1]
    # ================================================
    # --| Setup
    if "Macintosh;" in U_ag or "Windows" in U_ag:
        # =============== PROXY ==========================
        prox = random.choice(list(open('http.txt')))
        prox = prox[0:-1]
        print(prox)

        opt = Options()
        opt.headless = False
        options = webdriver.FirefoxProfile()
        firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        firefox_capabilities["marionette"] = True

        firefox_capabilities["proxy"] = {
            "proxyType": "MANUAL",
            "httpProxy": prox,
            "ftpProxy": prox,
            "sslProxy": prox
        }
        # ===========================================================
        # =============== User Agent ==========================
        options.set_preference("general.useragent.override", U_ag)
        print(U_ag)
        # =====================================================
        # ======================================================
        browser = webdriver.Firefox(
            firefox_profile=options, options=opt, proxy=prox)
        # =======================================================
        # browser.get('https://2ip.ru/')
        # ============Configure browser=======================
        # Youtube Канал
        browser.get('https://www.youtube.com/watch?v=mNEc3MtdCuQ')
        element = browser.find_element_by_class_name(
            "ytp-mute-button")  # Натиснуть кнопку звуку (Виключить звук)
        element.click()
        element = browser.find_element_by_class_name(
            "ytp-play-button")  # Натиснуть кнопку Play
        element.click()
        # ======================================================

        time.sleep(5)  # =======Затримка
        browser.close()  # =========Закрить браузер


for item in range(1):
    print("# ", item)
    main()
