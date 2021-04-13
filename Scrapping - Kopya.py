import time
import datetime
import openpyxl
import urllib.request
import xlsxwriter
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#devId = ["6715068722362591614"]
#, "7891990035506213180"

keywords = ["arcade games", "sport games", "race games", "strategy games", "puzzle games", "action games",
            "board games", "role play games", "survival games", "simulation games", "music games", "adventure games",
            "casino games", "classic games", "casual games", "trivia games", "word games", "educational games"]
list_all_elements = []
PATTERN = "\(₺(.*?)\)"
"""
"""
d = datetime.datetime.now()
filename = "total_{}{}{}_copy.xlsx".format(d.strftime("%d"), d.strftime("%m"), d.strftime("%y"))
workbook = xlsxwriter.Workbook(filename)
worksheet = workbook.add_worksheet()

#for id in devId:
for keyword in keywords:
    for prc in range(1, 3):
        #option = Options()
        #option.add_argument('--headless')
        #option.add_argument('--disable-gpu')
        driver = webdriver.Chrome(ChromeDriverManager().install())#, chrome_options=option)
        #driver.get('https://play.google.com/store/apps/dev?id={}'.format(id))
        driver.get('https://play.google.com/store/search?q={}&c=apps&hl=tr&gl=tr&price={}'.format(keyword,prc))
        time.sleep(2)
        #driver.find_element_by_css_selector("a.LkLjZd.ScJHi.U8Ww7d.xjAeve.nMZKrb.id-track-click ").click()

        SCROLL_PAUSE_TIME = 3

        # Scroll Yüksekliği
        last_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(SCROLL_PAUSE_TIME)
        i = 0
        while True:
            #aşağı scroll
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

            time.sleep(SCROLL_PAUSE_TIME)

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        links_games = []
        elems = driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            if "details?id" in elem.get_attribute("href"):
                links_games.append((elem.get_attribute("href")))

        links_games = list(dict.fromkeys(links_games))

        for iteration in links_games:
            try:
                i += 1
                driver.get(iteration)
                print(iteration)
                time.sleep(2)
                company = driver.find_element_by_css_selector(".qQKdcc span:nth-child(1)")
                genre = driver.find_element_by_css_selector(".qQKdcc span:nth-child(2)")
                header1 = driver.find_element_by_tag_name("h1")
                star = driver.find_element_by_class_name("BHMmbe")
                logo = driver.find_element_by_css_selector(".xSyT2c img")
                logo_src = logo.get_attribute("src")
                urllib.request.urlretrieve(logo_src, "{}_logo.png".format(company.text))
                logo_main = openpyxl.drawing.image.Image("{}_logo.png".format(company.text))
                logo_main.anchor(worksheet.cell('A'+str(i+1)))
                worksheet.add_image(logo_main)



                priceTag = driver.find_element_by_css_selector("button.LkLjZd.ScJHi.HPiPcc.IfEcue meta:nth-child(2)")
                price = priceTag.get_attribute("content")
                pORf = "paid"
                if price == "0":
                    pORf = "free"
                else:
                    pORf = "paid"

                others = driver.find_elements_by_class_name("htlgb")

                list_others = []
                for x in range (len(others)):
                    if x % 2 == 0:
                        list_others.append(others[x].text)

                titles = driver.find_elements_by_class_name("BgcNfc")
                #comments = driver.find_element_by_class_name("EymY4b")
                comments = driver.find_element_by_css_selector(".EymY4b span:nth-child(2)")

                list_elements = [logo_main, header1.text,company.text, genre.text, float(star.text.replace(",", ".")),
                                 pORf, price,comments.text.split()[0]]
                for x in range(len(titles)):
                    if titles[x].text == "Yükleme sayısı":
                        list_elements.append(list_others[x])
                    elif titles[x].text == "İçerik Derecelendirmesi":
                        for y in list_others[x].split("\n"):
                            if "PEGI" in y:
                                list_elements.append(y)
                                break
                    elif titles[x].text == "Güncellendi":
                        list_elements.append(list_others[x])
                    elif titles[x].text == "Boyut":
                        list_elements.append(list_others[x])
                    elif titles[x].text == "Mevcut Sürüm":
                        list_elements.append(list_others[x])
                    elif titles[x].text == "Gereken Android sürümü":
                        list_elements.append(list_others[x])
                    elif titles[x].text == "Uygulama İçi Ürünler":
                        list_elements.append(list_others[x])

                worksheet.write(list_elements)
                #list_all_elements.append(list_elements)
            except Exception as e:
                print(e)

        print("{} - {} session completed".format(keyword, prc))

    driver.quit()


d = datetime.datetime.now()
filename = "total_{}{}{}.xlsx".format(d.strftime("%d"), d.strftime("%m"), d.strftime("%y"))
df = pd.DataFrame(list_all_elements, columns=['Logo', 'Name', 'Company', 'Genre', 'Stars', 'Free/Paid', 'Price', 'Comments','Last Update', 'Size', 'Installs', 'Current Version','Required Min Version','Ingame Prices', 'PEGI'])
df.to_excel(r'outputs/{}'.format(filename), header=True, index=False)


"soccer games", "basketball games", "fairy games", "öğretici oyunlar", "historical games", "science games", "competitive games", "color games", "animal games", "story games"

