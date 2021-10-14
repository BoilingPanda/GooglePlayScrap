import numpy as np
import cv2
import os
import csv
import pandas as pd
import webcolors
from skimage import io

all_color_data = []


def main(file_name):
    read_logo_name(file_name)
    create_new_file("Game Logos Color Detail")


def read_logo_name(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        links_games = list(reader)

    for link in links_games:
        logo_name = link[0].split("=")[1]
        open_logo(logo_name)



def open_logo(logo_name):
    global all_color_data
    path = "logos/{}.png".format(logo_name)
    if os.path.isfile(path):
        color_data = []
        color_data.append(logo_name)
        img = io.imread(path)
        average = img.mean(axis=0).mean(axis=0)
        pixels = np.float32(img.reshape(-1, 3))

        n_colors = 5
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
        flags = cv2.KMEANS_RANDOM_CENTERS

        _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
        _, counts = np.unique(labels, return_counts=True)

        dominant = palette[np.argmax(counts)]
        rgb_color = []
        for i in dominant:
            rgb_color.append(int(i))
        named_dominant_color = xyz(logo_name)
        # if named_color_list[0] is not None:
        #     named_dominant_color = named_color_list[0]
        # else:
        #     named_dominant_color = named_color_list[1]
        color_data.append(named_dominant_color)
        color_data.append(rgb_color)
        color_data.append(rgb_color[0])
        color_data.append(rgb_color[1])
        color_data.append(rgb_color[2])
        rgb_color = []
        for i in average:
            rgb_color.append(int(i))

        named_color_list = get_color_name(rgb_color)
        if named_color_list[0] is not None:
            named_average_color = named_color_list[0]
        else:
            named_average_color = named_color_list[1]
        color_data.append(named_average_color)
        color_data.append(rgb_color)
        color_data.append(rgb_color[0])
        color_data.append(rgb_color[1])
        color_data.append(rgb_color[2])
        print("{} - dominant:{} - average:{}".format(logo_name, named_dominant_color, named_average_color))
        all_color_data.append(color_data)
    else:
        print("File not found")


def create_new_file(filename):

    df = pd.DataFrame(all_color_data, columns=('Game_id', 'Dominant_Color', 'Dominant_Color_Code', 'Dominant_Red',
                                               'Dominant_Green', 'Dominant_Blue','Average_Color', 'Average _Color_Code',
                                               'Average_Red', 'Average_Green', 'Average_Blue'))
    writer = pd.ExcelWriter('{}.xlsx'.format(filename), engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    print("{}.xlsx dosyası oluşturuldu.".format(filename))

    writer.save()


def find_closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]


def get_color_name(requested_color):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_color)
    except ValueError:
        closest_name = find_closest_color(requested_color)
        actual_name = None
    return actual_name, closest_name



# def draw_color_diversity(average, counts, img, palette):
#     avg_patch = np.ones(shape=img.shape, dtype=np.uint8)*np.uint8(average)
#
#     indices = np.argsort(counts)[::-1]
#     freqs = np.cumsum(np.hstack([[0], counts[indices]/float(counts.sum())]))
#     rows = np.int_(img.shape[0]*freqs)
#     print(freqs)
#     print(indices)

def xyz(filename):
    #Set this to the number of colors that you want to classify the images to
    number_of_colors = 8

    #Verify that the number of colors chosen is between the minimum possible and maximum possible for an RGB image.
    assert 8 <= number_of_colors <= 16777216

    #Get the cube root of the number of colors to determine how many bins to split each channel into.
    number_of_values_per_channel = number_of_colors ** ( 1 / 3 )

    #We will divide each pixel by its maximum value divided by the number of bins we want to divide the values into (minus one for the zero bin).
    divisor = 255 / (number_of_values_per_channel - 1)

    #load the image and convert it to float32 for greater precision. cv2 loads the image in BGR (as opposed to RGB) format.
    image = cv2.imread("logos/{}.png".format(filename), cv2.IMREAD_COLOR).astype(np.float32)

    #Divide each pixel by the divisor defined above, round to the nearest bin, then convert float32 back to uint8.
    image = np.round(image / divisor).astype(np.uint8)

    #Flatten the columns and rows into just one column per channel so that it will be easier to compare the columns across the channels.
    image = image.reshape(-1, image.shape[2])

    #Find and count matching rows (pixels), where each row consists of three values spread across three channels (Blue column, Red column, Green column).
    uniques = np.unique(image, axis=0, return_counts=True)

    #The first of the two arrays returned by np.unique is an array compromising all of the unique colors.
    colors = uniques[0]

    #The second of the two arrays returend by np.unique is an array compromising the counts of all of the unique colors.
    color_counts = uniques[1]

    #Get the index of the color with the greatest frequency
    most_common_color_index = np.argmax(color_counts)

    #Get the color that was the most common
    most_common_color = colors[most_common_color_index]

    #Multiply the channel values by the divisor to return the values to a range between 0 and 255
    most_common_color = most_common_color * divisor

    #If you want to name each color, you could also provide a list sorted from lowest to highest BGR values comprising of
    #the name of each possible color, and then use most_common_color_index to retrieve the name.
    print(most_common_color)
    rgb_color = []
    for i in most_common_color:
        rgb_color.append(int(i))
    return webcolors.rgb_to_name(rgb_color)



main("yenilogolink.csv")
