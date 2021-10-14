import datetime
import pandas as pd
import csv
import MobileScrap
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

list_games = []

with open("release date3.csv", newline='') as f:
    reader = csv.reader(f)
    search_keywords = list(reader)

for game in search_keywords:
    temp = []
    games = game[0].split(';')
    print("{} için çıkış tarihi aranıyor.".format(games[0]))
    release_date = MobileScrap.get_release_date(games[0], games[1], "emulator-5558")
    temp.append(games[0])
    temp.append(games[1])
    temp.append(release_date)
    print(temp)
    list_games.append(temp)


df = pd.DataFrame(list_games, columns=('Game_Id', 'Game_Name' 'Release_Date'))
writer = pd.ExcelWriter('{}.xlsx'.format("Games Release Date3"), engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
workbook = writer.book
worksheet = writer.sheets['Sheet1']
print("{}.xlsx dosyası oluşturuldu.".format("Games Release Date"))
writer.save()
