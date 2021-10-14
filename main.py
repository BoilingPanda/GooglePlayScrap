import GooglePlayStoreLogoScrap as Logo
import GooglePlayStoreLinkScrap as Search
import GooglePlayStoreDetailScrap as Data
import anything as Misc
import imageProcess as img
import os

keywords = []
search_filename = ""


def keyword_ekleme(key_input):
    global keywords
    keywords = key_input.split(",")


while True:
    deger = input("""
    Yapmak istediğiniz işlemi seçiniz:
    1.Keyword ekleme
    2.Oyun araması başlatma
    3.Oyun logosu indirme
    4.Oyun detay bilgileri indirme
    5.Kullanılmayan logoları silme
    6.Logolara ait renk işleme verilerini alma
    Çıkmak için q tuşuna basabilirsiniz.
    """)
    if deger == "q":
        break

    if deger == "1":
        kyw = input("Eklemek istediğiniz arama sözcüklerini aralarında virgül(,) bırakarak yazınız.")
        keyword_ekleme(kyw)
    elif deger == "2":
        search_filename = Search.main(keywords)
    elif deger == "3":
        if search_filename is not None:
            ans=""
            while ans.lower() not in ["y", "n"]:
                ans = input("{} dosyası içerisinde bulunan logoları indirmek ister misiniz? (y/n)".format(search_filename))
                if ans.lower() == "y":
                    Logo.main(search_filename)
                else:
                    new_file_name = ""
                    while not os.path.isfile(new_file_name):
                        new_file_name = input("""Kullanmak istediğiniz dosya adını giriniz:
                        Farklı bir klasördeki dosyayı kullanacaksanız dosyanın tam yolu girilmelidir!
                        """)
                    Logo.main(new_file_name)
    elif deger == "4":
        if search_filename is not None:
            ans=""
            while ans.lower() not in ["y", "n"]:
                ans = input("{} dosyası içerisinde bulunan oyun bilgierini indirmek ister misiniz? (y/n)".format(search_filename))
                if ans.lower() == "y":
                    Data.main(search_filename)
                else:
                    new_file_name = ""
                    while not os.path.isfile(new_file_name):
                        new_file_name = input("""Kullanmak istediğiniz dosya adını giriniz:
                        Farklı bir klasördeki dosyayı kullanacaksanız dosyanın tam yolu girilmelidir!
                        """)
                    Data.main(new_file_name)
    elif deger == "5":
        print("""Dikkat!!!!
        Yapacağınız işlem girdiğiniz dosyada bulunan oyun linkleri dışındaki tüm logo dosyalarını silecektir.
        Silme işlemi {}\logos yolu altındaki dosyalarda gerçekleşecektir. Devam etmeden önce yedekleme yapmanız önerilir.
        """.format(os.getcwd()))
        file_name = ""
        while not os.path.isfile(file_name):
            file_name = input("""Kullanmak istediğiniz dosya adını giriniz:
            Farklı bir klasördeki dosyayı kullanacaksanız dosyanın tam yolu girilmelidir!
            """)
        Misc.logo_sil(file_name)
    elif deger == "6":
        file_name = ""
        while not os.path.isfile(file_name):
            file_name = input("""Kullanmak istediğiniz dosya adını giriniz:
            Farklı bir klasördeki dosyayı kullanacaksanız dosyanın tam yolu girilmelidir!
            """)
        img.main(file_name)









