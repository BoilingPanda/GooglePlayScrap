import GooglePlayStoreLogoScrap as Logo
import GooglePlayStoreLinkScrap as Search
import GooglePlayStoreDetailScrap as Data

"""
Google Play Store üzerinde anahtar kelimeler ile
arama yapılarak gelen arama sonuçlarında yer alan
uygulamaların bilgilerinin bir excel dosyasına 
kaydedilmesi prensibi ile çalışmaktadır.

keywords: Arama yapılacak anahtar kelimelerin tutulduğu liste
links_file: Arama sonucu oluşturulan link dosyasının adının tutulduğu değişkendir. 

:returns:
"""

keywords = ["action games",	"adventure games",	"arcade games",	"board games",	"card games",	"casino games",
            "casual games",	"educational games", "music games",	"puzzle games",	"racing games",	"role playing games",
            "simulation games",	"sports games",	"strategy games",	"trivia games",	"word games",	"brain games",
            "car games",	"free games",	"online games",	"shooting games",	"fighting games",	"smart games",
            "zombie games",	"new games","games for boys",	"games for girls",	"games download",	"car racing games",
            "bike games",	"multiplayer games",	"driving games","hidden object games","popular games","cool games",
            "kids games",	"play games",	"best games",	"all games",	"war games",	"games free","paid games",
            "single player games","3D games","chess games","games for kids","pool games","farmer games","captain games",
            "bowling games","online multiplayer games",	"super games",	"motorbike  games",	"mini games","mobile games",
            "awesome games",	"medical games",	"surgery games",	"dice games",	"space games",	"indie games",
            "popular games",	"2021 games",	"2020 games",	"2019 games",	"2018 games",	"2017 games",
            "games for adults",	"scientific games","math games",	"vr games",	"cartoon games","games for children",
            "turkish games",	"english games",	"most playing games",	"cooking games","cafe games","horror games",
            "warrior games",	"pet games",	"animal games",	"bingo games",	"backgammon games",	"yahtzee games",
            "craft games",	"5vs5 games","group games","download games","no internet games","offline games","sea games",
            "makeup games",	"social games",	"matching games","fairy games","story games","diy games","color games"]

links_file = "game_links_140721.csv"
#links_file = Search.main(keywords)
#Logo.main(links_file)
Data.main(links_file)








