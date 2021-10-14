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
count = 0

def save():
    global count
    global list_games
    temp2 = []
    try:
        with open("Games Release Date.csv", newline='') as n:
            reader = csv.reader(n)
            file = list(reader)
        for line in file:
            newline = line[0].strip(';')
            temp2.append(newline[0])
            temp2.append(newline[1])
            temp2.append(newline[2])
            list_games.append(temp2)
    except:
        pass

    df = pd.DataFrame(list_games, columns=('Game_Id', 'Game_Name', 'Release_Date'))
    df.to_csv("Games Release Date.csv", sep=';', index=False)
    # writer = pd.ExcelWriter('{}.xlsx'.format("Games Release Date"), engine='xlsxwriter')
    # df.to_excel(writer, sheet_name='Sheet1')
    # workbook = writer.book
    # worksheet = writer.sheets['Sheet1']
    # print("{}.xlsx dosyası oluşturuldu.".format("Games Release Date"))
    # writer.save()
    count = 0
    list_games = []


with open("release date.csv", newline='') as f:
    reader = csv.reader(f)
    search_keywords = list(reader)


for game in search_keywords:
    temp = []
    games = game[0].split(';')
    print("{} için çıkış tarihi aranıyor.".format(games[0]))
    game_link = "https://play.app.goo.gl/?link=https://play.google.com/store/apps/details?id={}&ddl=1&pcampaignid=web_ddl_1".format(games[0])
    release_date = MobileScrap.get_release_date(game_link, "eeb5d30e")
    temp.append(games[0])
    temp.append(games[1])
    temp.append(release_date)
    print(temp)
    list_games.append(temp)
    count += 1
    if count == 5:
        save()


