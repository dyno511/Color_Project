# ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from rembg import remove
import matplotlib.pyplot as plt
from threading import Thread, Lock
from joblib import load
import time
import os
from collections import Counter
import numpy as np

import re
import pandas as pd
from PIL import Image
import warnings

import json
import colorsys
import cv2


# Ignore scikit-learn warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")





def hsl_to_rgb(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)




def bgr_to_hsl(b, g, r):
    h, s, l = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    return h, s, l

# Hàm để tìm mã màu gần giống


def find_closest_color(pixel):
    h, s, l = bgr_to_hsl(pixel[0], pixel[1], pixel[2])
    hue_degrees = int(h * 360)
    return hue_degrees


def LoadNewGetColor(path):
    output_path = 'xyLy.png'

    # Đọc tệp ảnh
    image = Image.open(path)
    image = image.resize((600, 600))
    # Sử dụng rembg để xoá nền ảnh


    # Sử dụng rembg để xoá nền ảnh
    output = remove(image)

    # Lưu ảnh đã xử lý
    output.save(output_path)

    image = cv2.imread(output_path)


    # Hàm chuyển đổi BGR sang HSL
    # Khởi tạo từ điển color_counts với tất cả các khóa hue
    color_counts = {hue: 0 for hue in range(360)}


    # Count the number of pixels for each hue
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i, j]
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                continue
   
            hue = find_closest_color(pixel)
            color_counts[hue] += 1
        
    arrColor = [0] * 360  # Khai báo một danh sách arrColor

    for hue, count in color_counts.items():
        arrColor[hue] = count

    return arrColor


def callListColor(image):

    # print(arrColor)
    # arr = main(image)  # Assign the result to arrColor
    arr = LoadNewGetColor(image)

    arrLists = TaoBieuDo(getClassesFromCSV(arr))
  
    return [arr, arrLists[0], arrLists[1]]


def TaoBieuDo(listColor):

    translation_dict = {
        0: 'RED',
        1: 'ORANGE',
        2: 'YELLOW',
        3: 'GREEN',
        4: 'BLUE',
        5: 'INDIGO',
        6: 'PURPLE'
    }

    color_list = [
        ['RED', (255, 0, 0)],
        ['ORANGE', (255, 102, 0)],
        ['YELLOW', (255, 208, 0)],
        ['GREEN', (0, 255, 0)],
        ['BLUE', (0, 237, 255)],
        ['INDIGO', (75, 0, 130)],
        ['PURPLE', (187, 0, 255)]
    ]

    values = [list(item.values())[0] for item in listColor]


    listColor = [{translation_dict.get(color, color): value}
                 for color_dict in listColor for color, value in color_dict.items()]

    colors = [list(item.keys())[0] for item in listColor]



    bar_colors = []
    for color in colors:
        for index, item in enumerate(color_list):
            if item[0] == color:
                normalized_color = (
                    item[1][0] / 255, item[1][1] / 255, item[1][2] / 255)
                bar_colors.append(normalized_color)

    plt.clf()  # Xóa biểu đồ cũ
    
    plt.bar(colors, values, color=bar_colors)

    for i, v in enumerate(values):
        plt.text(i, v, str(v), ha='center', va='bottom')

    timestamp = time.strftime("%Y%m%d%H%M%S")

    image_dir = os.path.join(os.getcwd(), 'APP', 'static', 'IMGBieuDo')
    os.makedirs(image_dir, exist_ok=True)
    image_path = os.path.join(image_dir, f'BieuDo_{timestamp}.png')

    plt.savefig(image_path)

    del values

    return image_path, listColor


def GetNameCode(code):
    df = pd.read_csv('colors.csv', encoding="utf-8")
    for index, row in df.iterrows():
        name = row['name']
        class_ = row['class']
        if code == name:
            return class_


def process_class_range(start, end, predicted_classes, result_list):
    class_results = []
    for i in range(start, end):
        index = predicted_classes[i]
        if index > 0:
            for j in range(index):
                class_results.append(GetNameCode(i))
    result_list.extend(class_results)


def getClassesFromCSV(predicted_classes):
    print(predicted_classes)

    arrColor = [0] * 7
    for index, val in enumerate(predicted_classes):
        
        class_ = GetNameCode(index+1)
        if 'None' not in str(class_):
            arrColor[int(class_)] += val
    arrSUM = []
    for i, index in enumerate(arrColor):
        arrSUM.append({i: index})

    return arrSUM
