import cv2
import numpy as np

# Function to change background color
def change_color(image, lower_color, upper_color, new_color):
    # Create a mask for the specified color range
    mask = cv2.inRange(image, lower_color, upper_color)
    
    # Change the color of the pixels in the mask to the new color
    image[mask > 0] = new_color
    return image


# Function to crop colored background
def crop(img, lower_color, upper_color):
    # Create a mask for the color range
    mask = cv2.inRange(img, lower_color, upper_color)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour (assumed to be the colored background)
    largest_contour = max(contours, key=cv2.contourArea)

    # Create a mask for the largest contour
    contour_mask = np.zeros_like(mask)
    cv2.drawContours(contour_mask, [largest_contour], -1, 255, thickness=cv2.FILLED)

    # Bitwise AND the original image with the contour mask to extract the colored background
    colored_area = cv2.bitwise_and(image, image, mask=contour_mask)

    # Find the bounding box of the colored background
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Crop the colored background from the original image
    cropped_area = colored_area[y:y+h, x:x+w]
    return cropped_area


# Count no of triangles of particular color in particular background
def count(img, lower_color, upper_color):
    # Create a mask for the color range
    mask = cv2.inRange(img, lower_color, upper_color)

    # Denoising the image 
    noiseless_image_bw = cv2.bilateralFilter(mask,9,75,75)

    # Finding edges of colored triangles
    edges = cv2.Canny(noiseless_image_bw, threshold1=100, threshold2=200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Counting triangles
    triangle_count = 0
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
        if len(approx) == 3:
            triangle_count += 1
    return triangle_count




# Define the color ranges for required colors in HSV
lower_green = np.array([35, 100, 20])   # Lower HSV values for green
upper_green = np.array([80, 255, 255])  # Upper HSV values for green

lower_brown = np.array([5, 100, 10])    # Lower HSV values for brown
upper_brown = np.array([30, 255, 200])  # Upper HSV values for brown

lower_blue = np.array([100, 0, 0])      # Lower HSV values for blue
upper_blue = np.array([255, 100, 100])  # Upper HSV values for blue

lower_red = np.array([0, 0, 100])       # Lower HSV valves for red
upper_red = np.array([0, 100, 255])     # Upper HSV values for red


# Define the new colors (blue and yellow)
new_blue_color = (252, 252, 102)  # Blue color in BGR format
new_yellow_color = (144, 242, 245)  # Yellow color in BGR format


n_houses = []   # Empty list to store no of houses in different regions
priority_houses = [] # Empty list to store priority of houses
priority_ratio = []
image_name = []


for i in range(1,3,1):
    
# Changing image backgroung colors
    # Path to your image file
    image_path = "C:\\Program Files\\Python\\source code\\" + str(i)+ ".png"

    # Load the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Change green color to blue and brown color to yellow
    image_with_blue = change_color(hsv_image.copy(), lower_green, upper_green, new_blue_color)
    color_changed_image = change_color(image_with_blue.copy(), lower_brown, upper_brown, new_yellow_color)

    # Save background images
    cv2.imwrite("C:\\Program Files\\Python\\source code\\Changed Images\\image"+str(i)+".png" , color_changed_image)
    

# Counting no of triangles in different regions
    # Croping images according to background colors
    crop_image_green = crop(hsv_image, lower_green, upper_green)
    crop_image_brown = crop(hsv_image, lower_brown, upper_brown)

    # Counting no of red triangles
    red_triangles_in_green_area = count(crop_image_green, lower_red, upper_red)
    red_triangles_in_brown_area = count(crop_image_brown, lower_red, upper_red)
    
    # Counting no of blue triangles
    blue_triangles_in_green_area = count(crop_image_green, lower_blue, upper_blue)
    blue_triangles_in_brown_area = count(crop_image_brown, lower_blue, upper_blue)
    

# No of houses in different regions
    n=[red_triangles_in_brown_area + blue_triangles_in_brown_area, red_triangles_in_green_area + blue_triangles_in_green_area]
    n_houses.append(n)

    
# Priority Houses
    p=[red_triangles_in_brown_area + 2*blue_triangles_in_brown_area, red_triangles_in_green_area + 2*blue_triangles_in_green_area]
    priority_houses.append(p)

    
# Priority Ratio
    a = p[0]
    b = p[1]
    ratio = round(a/b, 2)
    priority_ratio.append(ratio)

# list of image names
    name = "image" + str(i)
    image_name.append(name)

# Name of image in priority order
dic_name = dict(zip(image_name, priority_ratio))
sorted_dic = sorted(dic_name)
image_by_rescue_ratio = sorted_dic[::-1]

print("n_houses = ", n_houses)
print("priority_houses = ", priority_houses)
print("priority_ratio = ", priority_ratio)
print("image_by_rescue_ratio", image_by_rescue_ratio)
