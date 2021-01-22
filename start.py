
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import random
import re


def main():
    vys = False
    U_ag = random.choice(list(open('user-agents.txt')))
    U_ag = U_ag[0:-1]

    # --| Setup
    if "Macintosh;" in U_ag or "Windows" in U_ag:
        prox = random.choice(list(open('http.txt')))
        sg = prox
        res = re.sub(r'\:.*', "", prox)
        res = res[0:-1]
        #sg = prox
        temp = sg.find(':')
        index = temp
        sg = sg[index:]
        sg = sg[1:]
        sg = sg[0:-1]
        print("PROXI = ", res, "port = ", sg)
        opt = Options()
        opt.headless = False
        options = webdriver.FirefoxProfile()
        options.set_preference("network.proxy.type", 1)
        options.set_preference("network.proxy.http", res)
        options.set_preference("network.proxy.http_port", int(sg))
        options.set_preference("general.useragent.override", U_ag)

        options.update_preferences()
        print(U_ag)

        browser = webdriver.Firefox(firefox_profile=options, options=opt)
        browser.get('https://2ip.ru/')
        # browser.get('https://www.youtube.com/watch?v=mNEc3MtdCuQ')
        # element = browser.find_element_by_class_name("ytp-mute-button")
        # element.click()
        # element = browser.find_element_by_class_name("ytp-play-button")
        # element.click()

        time.sleep(10)
        browser.close()


for item in range(1):
    print("# ", item)
    main()
