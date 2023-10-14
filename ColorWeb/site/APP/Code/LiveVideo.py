import cv2 as cv
import datetime
import cv2
import os

frame = ""


def stream():
    global frame
    cap = cv2.VideoCapture(1)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: failed to capture image")
            break

        # Convert the frame to bytes without saving it as an image
        _, buffer = cv2.imencode('.jpg', frame)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')


def save_image():
    global frame
    current_time = datetime.datetime.now()
    # Định dạng thời gian thành chuỗi
    timestamp = current_time.strftime("%Y%m%d%H%M%S")
    directory = f'APP/static/IMGXL/{timestamp}/'
    os.makedirs(directory, exist_ok=True)
    saved_image = f'{directory}{timestamp}.jpg'
    cv2.imwrite(saved_image, frame)
    return saved_image


def create_color_variations(image_path, num_variations=6):

    img = cv2.imread(image_path, cv.IMREAD_GRAYSCALE)

    if img is None:
        return None

    imgList = []

    imgList.append(image_path)

    image_directory = os.path.dirname(image_path)

    for i in [cv.THRESH_BINARY, cv.THRESH_BINARY_INV, cv.THRESH_TRUNC, cv.THRESH_TOZERO, cv.THRESH_TOZERO_INV]:

        ret, variation = cv.threshold(img, 127, 255, i)
        variation_path = os.path.join(image_directory, f'variation_{i}.jpg')
        cv2.imwrite(variation_path, variation)

        imgList.append(variation_path)

    return imgList
