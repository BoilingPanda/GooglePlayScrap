import csv
import os
import pandas as pd


logo_names = []

#
# def logo_sil(filename):
#     with open("filename", newline="") as f:
#         reader = csv.reader(f)
#         links_games = list(reader)
#
#     for i in links_games:
#         logo_name = "{}.png".format(i[0].split("=")[1])
#         logo_names.append(logo_name)
#
#     for file in os.listdir("logos"):
#         if file in logo_names:
#             continue
#         else:
#             os.remove("logos/{}".format(file))

# def merge_files():

    # df = pd.DataFrame(merged_list, columns=('Store link', 'Game', 'Developer', 'Genre', 'Rating', 'Reviews',
    #                                         'Paid or Free','Price', 'Featured', 'reklam', 'Game Description',
    #                                         'New Features', 'Updated', 'Size', 'Installs', 'Current Version',
    #                                         'Requires Android', 'Content Rating', 'Interactive Elements',
    #                                         'Description', 'Length  of Description', 'In-app Products'))
    # writer = pd.ExcelWriter('{}.xlsx'.format("merged data"), engine='xlsxwriter')
    # df.to_excel(writer, sheet_name='Sheet1')
    # workbook = writer.book
    # worksheet = writer.sheets['Sheet1']
    # print("{}.xlsx dosyası oluşturuldu.".format("merged data"))
    #
    # writer.save()

    # df = pd.read_excel("game_list_detailed_130721(1).xlsx")
    #
    # cf = pd.read_excel("Game Logos Color Detail(1).xlsx")
    #
    # for i in range(0, len(df["Store_link"])):
    #     df["Store_link"][i] = df["Store_link"][i].split("=")[1]
    #
    # dfcolumns = df.columns
    # cfcolumns = cf.columns
    # af = df[dfcolumns].merge(cf[cfcolumns], left_on='Store_link', right_on='Game_id', how = "left")
    # af.to_excel("merged_game_list_detailed_140721.xlsx", index=False)




    # df.merge(cf, how='inner', left_on='Store_link', right_on='Game_id')
    # af = pd.concat([df, cf], axis=1, join='inner')
    # #print(af["Dominant Color"].unique())
    # writer = pd.ExcelWriter("merged_game_list_detailed_140721.xlsx", engine="xlsxwriter")
    # af.to_excel(writer, sheet_name='Sheet1', index=False)
    # writer.save()

df = pd.read_excel("merged_game_list_detailed_140721.xlsx")
for i in range(0, len(df['Updated'])):

    date_list = df['Updated'][i].split(" ")

    if date_list[1] == "Ocak":
        date_list[1] = "01"
    elif date_list[1] == "Şubat":
        date_list[1] = "02"
    elif date_list[1] == "Mart":
        date_list[1] = "03"
    elif date_list[1] == "Nisan":
        date_list[1] = "04"
    elif date_list[1] == "Mayıs":
        date_list[1] = "05"
    elif date_list[1] == "Haziran":
        date_list[1] = "06"
    elif date_list[1] == "Temmuz":
        date_list[1] = "07"
    elif date_list[1] == "Ağustos":
        date_list[1] = "08"
    elif date_list[1] == "Eylül":
        date_list[1] = "09"
    elif date_list[1] == "Ekim":
        date_list[1] = "10"
    elif date_list[1] == "Kasım":
        date_list[1] = "11"
    elif date_list[1] == "Aralık":
        date_list[1] = "12"
    #print(date_list)

    df['Updated'][i] = "{}-{}-{}".format(date_list[0].replace(",", ""), date_list[1], date_list[2])
df.to_excel("merged_game_list_detailed_140721_last.xlsx", index=False)

# writer = pd.ExcelWriter("game_list_detailed_130721.xlsx", engine="xlsxwriter")
# df.to_excel(writer, sheet_name='Sheet1', index=False)
# writer.save()

# create_new_file(af)

df = pd.read_excel("merged_game_list_detailed_140721.xlsx")
for i in range(0, len(df['Updated'])):

    date_list = df['Updated'][i].split("-")
    if int(date_list[0]) < 10:
        date_list[0] = "0{}".format(date_list[0])
    df['Updated'][i] = "{}-{}-{}".format(date_list[0].replace(",", ""), date_list[1], date_list[2])
df.to_excel("merged_game_list_detailed_140721_last.xlsx", index=False)