from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
import glob2
import os
from datetime import date, timedelta
import datetime

ford_html = glob2.glob('/data/mail/*.html') 
ago_date = datetime.date.today() - timedelta(days=30)
down_dir = "/data/mail/" ## pvc 경로
binary = FirefoxBinary('/opt/firefox/firefox')

def file_open_craw():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.set_preference("browser.download.folderList", 2)
    opts.set_preference("browser.download.manager.showWhenStarting", False)
    opts.set_preference("browser.download.dir", down_dir)
    fox = webdriver.Firefox(options=opts,executable_path='/usr/local/bin/geckodriver',firefox_binary=binary)
    for i in ford_html:
        if int((os.path.basename(i).split("_")[-1]).split(".")[-2]) < int(str(ago_date.strftime("%Y%m%d"))):
            print(int((os.path.basename(i).split("_")[-1]).split(".")[-2]))
            continue
        else:
            fox.get('file://'+i)
            fox.find_element(by=By.XPATH, value="//*[@id=\"accountInfo01\"]/div[1]/div/div/ul/li[2]").click()
            fox.find_element(by=By.XPATH, value="//*[@id=\"div_카드이용내역\"]/div/div[1]/ul/li[3]/a").click()
            fox.execute_script("save2Xls_new('usage')")
    fox.close()

if __name__ == "__main__":
    file_open_craw()