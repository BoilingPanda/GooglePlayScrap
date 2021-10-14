import datetime
import pandas as pd
import csv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os


SCROLL_PAUSE_TIME = 1
list_all_elements = []
PATTERN = "\(₺(.*?)\)"


def main(csvfile):
    """Linklerin tutulduğu dosyayı okuyarak her bir linke gidip oyun detaylarını toplar.

    :param csvfile: Linklerin tutulduğu csv dosyasının adıdır.
    :return:
    """
    with open(csvfile, newline='') as f:
        reader = csv.reader(f)
        links_games = list(reader)
    driver = setup()
    d = datetime.datetime.now()
    filename = "game_list_detailed_{}{}{}".format(d.strftime("%d"), d.strftime("%m"), d.strftime("%y"))
    scrapping_main(driver, filename, links_games)
    create_new_file(filename)
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


def scrapping_main(driver, filename, links_games):
    """Uygulama sayfasında yer alan bilgileri toplayan fonksiyondur.

    :param driver: Tarayıcı kontrol etmek için tanımlanan değişkendir.
    :param filename: Toplanan uygulama detaylarının kaydedileceği excel dosyasının adıdır.
    :param links_games: Uygulama linklerinin tutulduğu liste yapısıdır.
    :return:
    """
    i = 1
    for iteration in links_games:
        try:
            driver.get(iteration[0])
            wait = WebDriverWait(driver, 5)
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "xSyT2c")))
        except TimeoutException as ex:
            print(ex)
            continue

        try:
            row_data = []
            company = driver.find_element_by_css_selector(".qQKdcc span:nth-child(1)")
            genre = driver.find_element_by_css_selector(".qQKdcc span:nth-child(2)")
            header1 = driver.find_element_by_tag_name("h1")
            print("{}. {} oyununa ait bilgiler toplanıyor.".format(i, header1.text), end="")
            if check_if_element_exists("BHMmbe", "class", driver):
                star = driver.find_element_by_class_name("BHMmbe").text
            else:
                star = "N/A"
            desc = driver.find_element_by_css_selector(".DWPxHb div:nth-child(1)")
            if check_if_element_exists(".EymY4b span:nth-child(2)", "css", driver):
                review = driver.find_element_by_css_selector(".EymY4b span:nth-child(2)").text
            else:
                review = "N/A"
            price = driver.find_element_by_css_selector("button.LkLjZd.ScJHi.HPiPcc.IfEcue "
                                                        "meta:nth-child(2)").get_attribute("content")
            print(".", end="")

            if price == "0":
                paid_or_free = 0
            else:
                paid_or_free = 1
            if check_if_element_exists("dMMEE", "class", driver):
                featured = 1
            else:
                featured = 0
            if check_if_element_exists("bSIuKf", "class", driver):
                reklam = driver.find_element_by_class_name("bSIuKf").text
            else:
                reklam = ""

            if check_if_element_exists(".TdqJUe", "class", driver):
                video = 1
            else:
                video = 0
            if check_if_element_exists("//div[@class='SgoUSc']//img[@alt='Ekran Görüntüsü Resmi']", "xpath", driver):
                screenshots = driver.find_elements_by_xpath("//div[@class='SgoUSc']//img[@alt='Ekran Görüntüsü Resmi']")
            else:
                screenshots = []

            if check_if_element_exists("(//div[@class='DWPxHb']//span)[2]", "xpath", driver):
                new_update = driver.find_element_by_xpath('(//div[@class="DWPxHb"]//span)[2]').text
            else:
                new_update = ""

            row_data = [iteration[0], header1.text, company.text, genre.text, star, review, paid_or_free, price,
                        featured, reklam, video, len(screenshots), new_update]
            print(".", end="")
            row_data = get_other_info(driver, row_data)
            row_data.append(desc.text)
            row_data.append(len(desc.text))
            print("{}/{} {} oyununa ait bilgiler excele yazılıyor.".format(i,len(links_games), header1.text), end="")
            print(".")
            i += 1
            list_all_elements.append(row_data)
            if i % 10 == 0:
                if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
                    command = 'cls'
                else:
                    command = 'clear'
                os.system(command)
        except Exception as e:
            print(e)


def check_if_element_exists(class_name, selector, driver):
    try:
        if selector == "class":
            if driver.find_element_by_class_name(class_name).is_displayed():
                return True
        elif selector == "css":
            if driver.find_element_by_css_selector(class_name).is_displayed():
                return True
        elif selector == "xpath":
            if driver.find_element_by_xpath(class_name).is_displayed():
                return True
    except NoSuchElementException:
        return False








def get_other_info(driver, row_data):
    """Oyuna ait künye bilgilerinin toplandığı fonksiyondur.

    :param driver: Tarayıcının kontrolü için tanımlanan değişkendir.
    :param row_data: Sayfası ziyaret edilen uygulamanın bilgilerinin toplandığı geçici liste yapısıdır.
    :return: Bilgilerin tutulduğu geçici listeye künye bilgilerini ekleyip listeyi geri döndürür.
    """
    others = driver.find_elements_by_class_name("htlgb")

    list_others = []
    for x in range (len(others)):
        if x % 2 == 0:
            list_others.append(others[x].text)

    titles = driver.find_elements_by_class_name("BgcNfc")
    titles_text = []
    print(".", end="")
    for x in range(len(titles)):
        titles_text.append(titles[x].text)
        if titles[x].text == "Yükleme sayısı":
            row_data.append(list_others[x])
        elif titles[x].text == "İçerik Derecelendirmesi":
            for y in list_others[x].split("\n"):
                if "PEGI" in y:
                    pegiscore = y
                    break
                else:
                    pegiscore = "Tüm yaşlar"
            row_data.append(pegiscore)
        elif titles[x].text == "Güncellendi":
            row_data.append(list_others[x])
        elif titles[x].text == "Boyut":
            row_data.append(list_others[x])
        elif titles[x].text == "Mevcut Sürüm":
            row_data.append(list_others[x])
        elif titles[x].text == "Gereken Android sürümü":
            row_data.append(list_others[x])
        elif titles[x].text == "Uygulama İçi Ürünler":
            row_data.append(list_others[x])
        elif titles[x].text == "Etkileşimli Öğeler":
            row_data.append(list_others[x])


    if "Etkileşimli Öğeler" not in titles_text:
        row_data.append("None")
    if "Uygulama İçi Ürünler" not in titles_text:
        row_data.append("None")

    print(".")
    return row_data


def create_new_file(filename):
    """Toplanan tüm bilgiler satır bazında excele yazılır. Bilgisi yazılan uygulamaya ait logo logos klasöründen
    bulunarak Excelde A sütununa eklenir.
    :param filename: Toplanan tüm bilgilerin yazılacağı excel dosyasının adıdır.
    :return:
    """
    df = pd.DataFrame(list_all_elements, columns=('Store_link', 'Game', 'Developer', 'Genre', 'Rating', 'Reviews',
                                                  'Paid', 'Price', 'Featured', 'Ads', 'Video', 'Number_of_Screenshots',
                                                  'Game_Description', 'New_Features', 'Updated', 'Size', 'Installs',
                                                  'Current_Version', 'Requires_Android', 'Content_Rating',
                                                  'Interactive_Elements', 'Length_of_Description', 'In-app_Products'))
    writer = pd.ExcelWriter('{}.xlsx'.format(filename), engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    print("{}.xlsx dosyası oluşturuldu.".format(filename))
    writer.save()


def tear_down(driver):
    driver.quit()




