import numpy as np
import datetime
import cv2, os

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
    original_image = cv2.imread(image_path)

    if original_image is None:
        return None

    color_variations = []

    # Get the directory of the original image
    image_directory = os.path.dirname(image_path)

    for i in range(num_variations):
        # Clone the original image to work on
        variation = original_image.copy()

        # Create random values to adjust the brightness, contrast, and saturation
        alpha = np.random.uniform(0.5, 1.5)  # Adjust brightness
        beta = np.random.randint(-50, 50)    # Adjust contrast
        saturation_factor = np.random.uniform(0.5, 1.5)  # Adjust saturation

        # Apply the color transformation
        variation = cv2.convertScaleAbs(variation, alpha=alpha, beta=beta)
        hsv_variation = cv2.cvtColor(variation, cv2.COLOR_BGR2HSV)
        hsv_variation[:, :, 1] = hsv_variation[:, :, 1] * saturation_factor
        variation = cv2.cvtColor(hsv_variation, cv2.COLOR_HSV2BGR)

        # Save the color variation image in the same directory as the original image
        variation_path = os.path.join(image_directory, f'variation_{i}.jpg')
        cv2.imwrite(variation_path, variation)

        color_variations.append(variation_path)

    return color_variations
