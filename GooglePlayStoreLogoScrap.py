import datetime

import csv
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import urllib.request
from PIL import Image
import os

links_games = []

def main(csvfile):
    """Linklerin tutulduğu dosyayı okuyarak her bir linke gidip oyun logolarını toplar.

    :param csvfile: Linklerin tutulduğu csv dosyasının adıdır.
    :return:
    """
    with open(csvfile, newline='') as f:
        reader = csv.reader(f)
        links_games = list(reader)
    driver = setup()
    create_directory()
    d = datetime.datetime.now()
    i = 1
    y = len(links_games)
    for iteration in links_games:
        print(iteration[0])
        get_game_logo(driver, iteration[0], i, y)
        i += 1
    tear_down(driver)
    print("""
    İşin başlangıç zamanı: {}
    İşin bitiş zamanı: {}
    """.format(d, datetime.datetime.now()))


def setup():
    """Data scrap için browser initialize ve başlatılmasını içeren hazırlık metotudur.
    :return:
    """
    global driver
    option = Options()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)


def create_directory():
    """logoların tutulacağı logos klasörü henüz oluşturulmamış ise oluşturulur.
    :return:
    """
    if not os.path.exists("logos/"):
        os.mkdir("logos/")


def get_game_logo(driver, iteration, i, y):
    """Toplanan linklere tek tek giderek uygulamanın logosunu logos klasörüne kaydeder.
    Logo adı uygulama id olarak kaydedilecektir. Logo boyutu 60x60 olarak kaydedilecektir.
    Kaydedilecek logo boyutunu değiştirmek için width: ve height: değişkenleri değiştirilmelidir.
    :param driver: Tarayıcıyı kontrol etmek için tanımlanan değişkendir.
    :param iteration: Logosu indirilecek uygulamaya ait link
    :param i: konsolda işlemlerin takibi amacıyla ziyaret edilen uygulama sayfasının sıra sayısını ifade eder.
    :param y: konsolda işlemlerin takibi amacıyla toplam ziyaret edilecek uygulama sayısını ifade eder.
    :return:
    """
    try:
        logo_name = iteration.split("=")[1]
        if not os.path.isfile("logos/{}.png".format(logo_name)):
            # width = 60
            # height = 60
            driver.get(iteration)
            wait = WebDriverWait(driver,5)
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "xSyT2c")))
            img = driver.find_element_by_css_selector(".T75of.sHb2Xb")
            img_url = img.get_attribute("src")
            print("{}/{} {} logosu ekleniyor.".format(i, y, logo_name))
            urllib.request.urlretrieve(img_url, '{}.webp'.format(logo_name))
            im = Image.open("{}.webp".format(logo_name)).convert("RGB")
            # im = im.resize((width, height))
            im.save("logos/{}.png".format(logo_name), "png")
            os.remove("{}.webp".format(logo_name))
        else:
            print("{}/{} {} logosu zaten var.".format(i, y, logo_name))
    except:
        print("{}/{} {} logosu bulunamadı.".format(i, y, logo_name))

def tear_down(driver):
    driver.quit()




