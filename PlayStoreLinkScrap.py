import time
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

SCROLL_PAUSE_TIME = 1
keywords = ["games"]
list_all_elements = []
PATTERN = "\(₺(.*?)\)"
links_games = []

driver = 0


def main():
    setup()
    d = datetime.datetime.now()
    filename = "game_links_{}{}{}.csv".format(d.strftime("%d"), d.strftime("%m"), d.strftime("%y"))
    for keyword in keywords:
        for prc in range(1, 3):
            url = "https://play.google.com/store/search?q={}&c=apps&hl=tr&gl=tr&price={}".format(keyword, prc)
            search_keyword(url)
    write_to_csv(links_games, filename)
    driver.quit()


def scroll_to_bottom():
    last_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(SCROLL_PAUSE_TIME)
    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def search_keyword(url):
    print("{} adresine gidiliyor.".format(url))
    driver.get(url)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.sv0AUd.bs3Xnd')))
    print("Arama sonuçları yüklendi.")
    scroll_to_bottom()
    get_links()


def get_links():
    global links_games
    elements = driver.find_elements_by_xpath("//a[@href]")
    print("{} adet sonuç bulundu.".format(len(elements)))
    for element in elements:
        if "details?id" in element.get_attribute("href") and element.get_attribute("href") not in links_games:
            links_games.append((element.get_attribute("href")))
            print("{}. {} listeye yazıldı.".format(len(links_games),element.get_attribute("href")))

    links_games = list(dict.fromkeys(links_games))


def write_to_csv(link_list, filename):
    df = pd.DataFrame(link_list)
    df.to_csv(filename)
    print("Toplam {} adet link {} dosyasına yazıldı.".format(len(link_list), filename))


def setup():
    global driver
    option = Options()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)


main()
