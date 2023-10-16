import csv
import json
import colorsys
import cv2

def hsl_to_rgb(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)

image = cv2.imread('z4789452873819_066bcbb624674f8725afc37b20a45227.jpg')
image = cv2.resize(image, (600, 600))

# Function to convert BGR to HSL
def bgr_to_hsl(b, g, r):
    h, s, l = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    return h, s, l

# Function to find closest color based on hue
def find_closest_color(pixel):
    h, s, l = bgr_to_hsl(pixel[0], pixel[1], pixel[2])
    hue_degrees = int(h * 360)
    return hue_degrees

# Initialize a dictionary to count colors
color_counts = {hue: 0 for hue in range(360)}

# Count the number of pixels for each hue
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        pixel = image[i, j]
        hue = find_closest_color(pixel)
        color_counts[hue] += 1

# Initialize a list to store color information
colors = []

# Define standard color classes
# Define standard color classes
color_classes = {
    0: '0',
    30: '1',
    60: '2',
    120: '3',
    210: '4',
    270: '5',
    320: '6'
}

# Iterate through the hue counts and assign colors to standard classes
for hue, count in color_counts.items():
    rgb = hsl_to_rgb(hue / 360, 1, 0.5)
    closest_standard_hue = min(color_classes.keys(), key=lambda x: abs(x - hue))
    color = {
        'r': rgb[0],
        'g': rgb[1],
        'b': rgb[2],
        'name': hue + 1,
        # Assign class based on the closest standard hue
        'class': color_classes[closest_standard_hue]
    }
    colors.append(color)

# Save color information to JSON file
with open('colors.json', 'w', encoding='utf-8') as file:
    json.dump(colors, file, ensure_ascii=False, indent=2)

# Create a CSV file
with open('colors.csv', 'w', newline='') as csvfile:
    fieldnames = ['r', 'g', 'b', 'name', 'class']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for color in colors:
        writer.writerow(color)

