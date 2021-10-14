import os.path
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
links_games = []
driver = None


def main(keywords):
    """
    :param keywords: liste tipinde veri ile çağırılmalıdır. Listede arama yapılmak istenen her anahtar sözcük string veri tipinde yer almalıdır.
    url: arama listesinden alınan anahtar sözcüğü kullanarak arama sayfasının linki oluşturulur.
    prc: Oluşturulan arama linkinde ücretli/ücretsiz uygulama aramasını ayrıştırmak için kullanılan parametredir. 1- Ücretsiz 2- Ücretli
    :return: filename: linklerin tutulduğu csv dosyasının adını döner.
    Oluşturulan dosya sonraki işlemler için dizinde tutulmalıdır. Farklı bir dizinde tutulması halinde return ifadesi
    dosyanın bulunduğu dizin olarak döndürülmelidir.
    """
    setup()
    d = datetime.datetime.now()
    filename = "game_links_{}{}{}.csv".format(d.strftime("%d"), d.strftime("%m"), d.strftime("%y"))
    if os.path.isfile("game_links_{}{}{}.csv".format(d.strftime("%d"), d.strftime("%m"), d.strftime("%y"))):
        return filename
    else:
        for keyword in keywords:
            for prc in range(1, 3):
                url = "https://play.google.com/store/search?q={}&c=apps&hl=tr&gl=tr&price={}".format(keyword, prc)
                search_keyword(url)
        write_to_csv(links_games, filename)
        driver.quit()
        return filename


def scroll_to_bottom():
    """Arama sayfasında aşağı doğru scroll yaparak arama sonucuna dönen tüm uygulamaların sayfada yüklenmesini sağlar.
    :SCROLL_PAUSE_TIME scroll sırasında yeni sonuçların yüklenmesini sağlamak amacıyla tanımlanan değişkendir.
    :return:
    """
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
    """İstenen arama sözcükleri için arama sonucu sayfalarına gider.
    Devamında scroll_to_bottom ve get_links fonksiyonları çağırılır.
    :param url:arama listesinden alınan anahtar sözcüğü kullanarak oluşturulan arama sonuçları linkidir.
    :return:
    """
    print("{} adresine gidiliyor.".format(url))
    driver.get(url)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.sv0AUd.bs3Xnd')))
    print("Arama sonuçları yüklendi.")
    scroll_to_bottom()
    get_links()


def get_links():
    """Arama sonuçları sayfasında getirilen uygulamaların sayfalarının linklerini toplar.
    Toplanan linkler links_games listesinde tutulur.
    :return:
    """
    global links_games
    elements = driver.find_elements_by_xpath("//a[@href]")
    print("{} adet sonuç bulundu.".format(len(elements)))
    for element in elements:
        if "details?id" in element.get_attribute("href") and element.get_attribute("href") not in links_games \
                and not os.path.isfile("logos/{}.png".format(element.get_attribute("href").split("=")[1])):
            links_games.append((element.get_attribute("href")))
            print("{}. {} listeye yazıldı.".format(len(links_games), element.get_attribute("href")))
    links_games = list(dict.fromkeys(links_games))



def write_to_csv(link_list, filename):
    """Uygulama linklerini dosya olarak dizine kaydeder.
    :param link_list: Toplanan uygulama linklerinin bulunduğu liste yapısıdır.
    :param filename: Toplanan linklerin kaydedileceği csv dosyasının adıdır.
    :return:
    """
    df = pd.DataFrame(link_list)
    df.to_csv(filename, header=False, index=False)
    print("Toplam {} adet link {} dosyasına yazıldı.".format(len(link_list), filename))



def setup():
    """Data scrap için browser initialize ve başlatılmasını içeren hazırlık metotudur.
    :return:
    """
    global driver
    option = Options()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
