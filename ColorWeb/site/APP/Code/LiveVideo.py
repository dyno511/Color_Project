from rembg import remove
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
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        return None

    imgList = []

    image_directory = os.path.dirname(image_path)

    variation_path = os.path.join(image_directory, f'variation_removeBack.jpg')

    # Read the image data and pass it to the remove function
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        remove_result = remove(image_data)

    with open(variation_path, "wb") as output_file:
        output_file.write(remove_result)

    imgList.append(variation_path)

    for i in [cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC, cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV]:
        ret, variation = cv2.threshold(img, 127, 255, i)
        variation_path = os.path.join(image_directory, f'variation_{i}.jpg')
        cv2.imwrite(variation_path, variation)
        imgList.append(variation_path)

    return imgList
