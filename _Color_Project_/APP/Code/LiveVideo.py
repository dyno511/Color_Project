from PIL import Image
from PIL import Image, ImageDraw
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

from PIL import Image, ImageDraw
import os

def overlay_red(image, opacity):
    return overlay_color(image, (255, 0, 0), opacity)

def overlay_green(image, opacity):
    return overlay_color(image, (0, 255, 0), opacity)

def overlay_blue(image, opacity):
    return overlay_color(image, (0, 0, 255), opacity)

def overlay_yellow(image, opacity):
    return overlay_color(image, (255, 255, 0), opacity)

def overlay_cyan(image, opacity):
    return overlay_color(image, (0, 255, 255), opacity)

def overlay_magenta(image, opacity):
    return overlay_color(image, (255, 0, 255), opacity)

def overlay_color(image, overlay_color, opacity):
    # Create a transparent layer of the same size as the image
    overlay = Image.new('RGBA', image.size, (0, 0, 0, 0))

    # Create a drawing context on the overlay
    draw = ImageDraw.Draw(overlay)

    # Draw a filled rectangle with the overlay color and opacity
    draw.rectangle([(0, 0), image.size], fill=(*overlay_color, opacity))

    # Combine the original image and the overlay
    result_image = Image.alpha_composite(image.convert('RGBA'), overlay)

    # Convert the result image to RGB mode
    result_image = result_image.convert('RGB')

    return result_image


def create_color_variations(image_path, num_variations=6):
    img = Image.open(image_path)

    if img is None:
        return None

    imgList = []

    image_directory = os.path.dirname(image_path)

    for i in range(1, num_variations + 1):
        variation_path = os.path.join(image_directory, f'variation_{i}.jpg')

        if i == 1:
            # Remove the background from the first image
            # Assuming you have the 'remove' function for background removal
            img = remove(img)
            img = img.convert('RGB')  # Convert to RGB mode
            img.save(variation_path)
        elif i == 2:
            overlay_red(img, 128).convert('RGB').save(
                variation_path)  # Convert to RGB mode
        elif i == 3:
            overlay_green(img, 128).convert('RGB').save(
                variation_path)  # Convert to RGB mode
        elif i == 4:
            overlay_blue(img, 128).convert('RGB').save(
                variation_path)  # Convert to RGB mode
        elif i == 5:
            overlay_yellow(img, 128).convert('RGB').save(
                variation_path)  # Convert to RGB mode
        elif i == 6:
            overlay_cyan(img, 128).convert('RGB').save(
                variation_path)  # Convert to RGB mode

        imgList.append(variation_path)

    return imgList
