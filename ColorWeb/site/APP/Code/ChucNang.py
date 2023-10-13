# ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from threading import Thread, Lock
from joblib import load
import time
import os
from collections import Counter
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
from PIL import Image
import warnings
from sklearn.neighbors import KNeighborsClassifier


# Ignore scikit-learn warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")


# Define arrColor as a global variable
arrColor = [0] * 360
arrColorLock = Lock()  # Add a lock for synchronization


def callListColor(image):
    arr = main(image)  # Assign the result to arrColor
    print("a")
    arrList = getClassesFromCSV(arr)
    print("b")

    # print(arrList)
    arrList = TaoBieuDo(arrList)
    print("c")

    return [arr, arrList]


def TaoBieuDo(listColor):
    print(listColor)
    translation_dict = {
        '0': 'RED',
        '1': 'ORANGE',
        '2': 'YELLOW',
        '3': 'GREEN',
        '4': 'BLUE',
        '5': 'INDIGO',
        '6': 'PURPLE'
    }

    color_list = [
        ['RED', (255, 0, 0)],
        ['ORANGE', (255, 102, 0)],
        ['YELLOW', (255, 208, 0)],
        ['GREEN', (0, 255, 0)],
        ['BLUE', (0, 237, 255)],
        ['INDIGO', (0, 0, 255)],
        ['PURPLE', (187, 0, 255)]
    ]

    values = [list(item.values())[0] for item in listColor]

    listColor = [{translation_dict[color]: value}
                 for color_dict in listColor for color, value in color_dict.items()]

    colors = [list(item.keys())[0] for item in listColor]

    bar_colors = []  # Tạo một danh sách rỗng để lưu trữ màu sau khi chuyển đổi
    for color in colors:
        # Duyệt qua danh sách color_list để tìm màu cần chuyển đổi
        for index, item in enumerate(color_list):
            if item[0] == color:  # So sánh màu trong color_list với màu trong danh sách colors
                # Khi tìm thấy màu khớp, lấy giá trị màu và chuyển đổi thành giá trị từ 0 đến 1
                normalized_color = (item[1][0] / 255, item[1]
                                    [1] / 255, item[1][2] / 255)
                # Thêm giá trị màu đã chuyển đổi vào danh sách bar_colors
                bar_colors.append(normalized_color)

    # Vẽ biểu đồ cột dọc với màu từ color_list
    plt.bar(colors, values, color=bar_colors)

    # Chú thích số vào đầu cột biểu đồ
    for i, v in enumerate(values):
        plt.text(i, v, str(v), ha='center', va='bottom')

    # Generate a timestamp to use in the image filename
    timestamp = time.strftime("%Y%m%d%H%M%S")

    image_dir = os.path.join(os.getcwd(), 'APP', 'static', 'IMGBieuDo')

    # Ensure the directory exists
    os.makedirs(image_dir, exist_ok=True)

    # Generate the image path including the timestamp
    image_path = os.path.join(image_dir, f'BieuDo_{timestamp}.png')

    # Lưu biểu đồ thành tệp hình ảnh
    plt.savefig(image_path)

    # Return the image path
    return image_path


def getCodeColor(data):
    # Load the K-nearest neighbors model
    loaded_model = load('knn_model_bwg.joblib')
    new_data = np.array([data])
    predicted_class = loaded_model.predict(new_data)[0]

    with open('data.txt', 'r', encoding="utf-8") as file:
        for i, line in enumerate(file, 1):
            if i == predicted_class:
                desired_line = line.strip()
                color = desired_line
                match = re.search(r'\((\d+), (\d+), (\d+)\)', color)
                if match:
                    r = int(match.group(1))
                    g = int(match.group(2))
                    b = int(match.group(3))
                    color = (r, g, b)
                    return predicted_class


def process_pixels_in_range(start_x, start_y, end_x, end_y, image):
    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            process_pixel(x, y, image, arrColor)


def process_pixel(x, y, image, arrColor):
    pixel = image.getpixel((x, y))
    if pixel[0] > 245 and pixel[1] > 245 and pixel[2] > 245:
        return False

    # Assuming you want the first component of the color
    point = int(getCodeColor((pixel[0], pixel[1], pixel[2])))

    with arrColorLock:
        arrColor[point - 1] = arrColor[point - 1] + 1


def main(image):
    global arrColor  # Declare arrColor as a global variable
    image = Image.open(image)
    image = image.resize((600, 600), Image.BILINEAR)
    width, height = image.size
    total_pixels = width * height
    pixels_per_thread = 601
    print("pixels_per_thread", pixels_per_thread)
    num_threads = total_pixels // pixels_per_thread
    print("num_threads", num_threads)
    threads = []

    for i in range(num_threads):
        start_pixel = i * pixels_per_thread
        end_pixel = (i + 1) * pixels_per_thread
        start_x = start_pixel % width
        start_y = start_pixel // width
        end_x = end_pixel % width
        end_y = end_pixel // width

        thread = Thread(target=process_pixels_in_range, args=(
            start_x, start_y, end_x, end_y, image))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return arrColor


def GetNameCode(code):
    df = pd.read_csv('ClassifyColor.csv', encoding="utf-8")
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
    num_threads = 300  # Số luồng bạn muốn sử dụng

    # Chia công việc thành các phần
    class_count = len(predicted_classes)
    # print(class_count)
    chunk_size = class_count // num_threads

    threads = []
    results = []

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else class_count

        thread = Thread(target=process_class_range, args=(
            start, end, predicted_classes, results))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Kết hợp kết quả từ các luồng
    final_results = []
    for result in results:
        if result != None:
            final_results.extend(str(result))
        

        
    count = Counter(final_results)

    arrSUM = []
    for key, value in count.items():
        if key is not None:
            arrSUM.append({key: value})

    return arrSUM
