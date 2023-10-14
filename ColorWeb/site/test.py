# import cv2
# import os
# import re
# from threading import Thread, Lock
# import numpy as np
# from joblib import load
# import warnings
# from sklearn.neighbors import KNeighborsClassifier

# # Ignore scikit-learn warnings
# warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

# # Define arrColor as a global variable
# arrColor = [0] * 360
# arrColorLock = Lock()  # Add a lock for synchronization


# def getCodeColor(data):
#     # Load the K-nearest neighbors model
#     loaded_model = load('knn_model_bwg.joblib')
#     new_data = np.array([data])
#     predicted_class = loaded_model.predict(new_data)[0]

#     with open('data.txt', 'r', encoding="utf-8") as file:
#         for i, line in enumerate(file, 1):
#             if i == predicted_class:
#                 desired_line = line.strip()
#                 color = desired_line
#                 match = re.search(r'\((\d+), (\d+), (\d+)\)', color)
#                 if match:
#                     r = int(match.group(1))
#                     g = int(match.group(2))
#                     b = int(match.group(3))
#                     color = (r, g, b)
#                     return color


# def process_pixels_in_range(start_x, start_y, end_x, end_y, image):
#     for x in range(start_x, end_x):
#         for y in range(start_y, end_y):
#             process_pixel(x, y, image, arrColor)


# def process_pixel(x, y, image, arrColor):
#     pixel = image[y, x]
#     color = getCodeColor(pixel)
#     point = int(color[0])  # Assuming you want the first component of the color
#     with arrColorLock:
#         arrColor[point - 1] = arrColor[point - 1] + 1


# def main():
#     global arrColor  # Declare arrColor as a global variable
#     image = cv2.imread("1321313.png")
    
#     image = cv2.resize(image, (600, 600),
#                               interpolation=cv2.INTER_LINEAR)
#     height, width, _ = image.shape
#     total_pixels = width * height
#     pixels_per_thread = 601
#     print("pixels_per_thread", pixels_per_thread)
#     num_threads = total_pixels // pixels_per_thread
#     print("num_threads", num_threads)
#     threads = []

#     for i in range(num_threads):
#         start_pixel = i * pixels_per_thread
#         end_pixel = (i + 1) * pixels_per_thread
#         start_x = start_pixel % width
#         start_y = start_pixel // width
#         end_x = end_pixel % width
#         end_y = end_pixel // width

#         thread = Thread(target=process_pixels_in_range, args=(
#             start_x, start_y, end_x, end_y, image))
#         threads.append(thread)

#     for thread in threads:
#         thread.start()

#     for thread in threads:
#         thread.join()

#     return arrColor


# if __name__ == "__main__":
#     arrColor = main()  # Assign the result to arrColor
#     print("arrColor:", arrColor)


from PIL import Image
import os
import re
from threading import Thread, Lock
import numpy as np
from joblib import load
import warnings
from sklearn.neighbors import KNeighborsClassifier

# Ignore scikit-learn warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

# Define arrColor as a global variable
arrColor = [0] * 360
arrColorLock = Lock()  # Add a lock for synchronization


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


def main():
    global arrColor  # Declare arrColor as a global variable
    image = Image.open("thumbnail.png")
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


from collections import Counter
import pandas as pd

def GetNameCode(code):
    df = pd.read_csv('ClassifyColor.csv', encoding="utf-8")
    for index, row in df.iterrows():
        name = row['name']
        class_ = row['class']
        if code == name:
            return class_
        
def getClassesFromCSV(predicted_classes):
    class_results = []
    print(class_results)
    for i, index in enumerate(predicted_classes):
        # print(i, index)
        if index > 0:
            for i_ in range(index):
                class_results.append(GetNameCode(i))
            
    count = Counter(class_results)

    # In kết quả
    arrSUM = []
    for key, value in count.items():
        if key != None:
            arrSUM.append({key: value})
    # print(arrSUM)
    return arrSUM

if __name__ == "__main__":
    arr = main()  # Assign the result to arrColor
    # print("arrColor:", arrColor)
    arrList = getClassesFromCSV(arr)
    print(arrList)
        