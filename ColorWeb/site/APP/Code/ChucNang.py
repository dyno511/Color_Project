# ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump, load
import numpy as np
import matplotlib.pyplot as plt
import re


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from joblib import dump

arrColor = []
def TaoMang ():
    global arrColor
    arrColor = [0] * 360

def getListColorInImage(path_image):
    global arrColor
    from PIL import Image

    image = Image.open(path_image) # Mở hình ảnh sử dụng Pillow
    # Lấy kích thước của hình ảnh
    width, height = image.size
    # Lặp qua từng pixel trong hình ảnh
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))  # Lấy màu của pixel tại (x, y)
            # print(pixel)
            if pixel[0] >245 and pixel[1] >245 and pixel[2]>245:
                continue
            # if pixel[0]<10 and pixel[1]<10 and pixel[2] <10:
            #     continue
            point = int(getCodeColor(pixel))

            UpperArr(point)
    return arrColor

def getCodeColor(data):
    # Load mô hình đã được huấn luyện từ file
    loaded_model = load('knn_model_bwg.joblib')

    new_data = np.array([data])
    # new_data = np.array([[0, 0, 0]])

    predicted_class = loaded_model.predict(new_data)[0]

    # Đọc màu từ file data.txt dựa trên predicted_class
    with open('data.txt', 'r', encoding="utf-8") as file:
        for i, line in enumerate(file, 1):
            if i == predicted_class:
                desired_line = line.strip()
                # print(desired_line)
                color = desired_line
                match = re.search(r'\((\d+), (\d+), (\d+)\)', color)
                if match:
                    # Lấy giá trị R, G, B từ các nhóm trong biểu thức chính quy
                    r = int(match.group(1))
                    g = int(match.group(2))
                    b = int(match.group(3))
                    color = [r, g, b]
                    # print(f"Code Color {predicted_class} rgb {color}")
                    # print(predicted_class)
                    return predicted_class

def UpperArr(point):
    global arrColor
    print(point-1)
    arrColor[point-1] = arrColor[point-1] + 1

def callListColor(image):
    TaoMang()
    arr = getListColorInImage(image)
    print(arr)
    return arr



