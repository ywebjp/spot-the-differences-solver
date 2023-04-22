# Title: "Spot The Differences" solver (spot_the_differences_1.00.py)
# Author: @ywebjp (edited by ChatGPT)
# Date: 2023/04/22
# ver: 1.00

import cv2
import numpy as np

# Load the input image
input_image = cv2.imread("sample.PNG")

# Define the coordinates of the regions of interest (ROIs) in the input image
left_roi_top_left = (63, 250) # (x, y) depending on coordinate system
right_roi_top_left = (723, 250)
left_roi_bottom_right = (662, 852)

# Compute the width and height of the ROIs
roi_width = left_roi_bottom_right[0] - left_roi_top_left[0]
roi_height = left_roi_bottom_right[1] - left_roi_top_left[1]

# Crop the left and right ROIs from the input image
left_roi = input_image[left_roi_top_left[1]:left_roi_top_left[1] + roi_height, left_roi_top_left[0]:left_roi_top_left[0] + roi_width, :]
right_roi = input_image[right_roi_top_left[1]:right_roi_top_left[1] + roi_height, right_roi_top_left[0]:right_roi_top_left[0] + roi_width, :]

# Define a filter kernel
filter_kernel = np.ones((3, 3), np.float32) / 9

# Apply the filter kernel to the left and right ROIs
left_roi_filtered = cv2.filter2D(left_roi, -1, filter_kernel)
right_roi_filtered = cv2.filter2D(right_roi, -1, filter_kernel)

# Compute the absolute difference between the filtered left and right ROIs
abs_diff = cv2.absdiff(left_roi_filtered, right_roi_filtered)

# Convert the absolute difference image to grayscale
gray_diff = cv2.cvtColor(abs_diff, cv2.COLOR_BGR2GRAY)

# Set a threshold value and create a binary image based on the grayscale difference image
threshold = 40
binary_diff = gray_diff < threshold

# Convert the left ROI to grayscale and create a red image
left_roi_gray = cv2.cvtColor(left_roi, cv2.COLOR_BGR2GRAY)
red_image = np.zeros(left_roi.shape, dtype=np.uint8)
red_image[:, :, 2] = 255

# Combine the left grayscale image and the red image based on the binary difference image
result_image = np.where(np.expand_dims(binary_diff, axis=2), np.expand_dims(left_roi_gray, axis=2), red_image)

# Display the result
cv2.imshow("Result", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()