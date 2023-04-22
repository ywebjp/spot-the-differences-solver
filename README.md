# Spot The Differences Solver
This is a Python script that helps to solve "Spot The Differences" questions. The script takes an input image containing two almost identical images with some differences and highlights the differences in red, making them easy to spot.

## Requirements
- Python 3.x
- OpenCV
- NumPy

## Usage
1. Clone this repository.
2. Place the input image in the same directory as the script.
3. Run the script by typing python spot_the_differences.py in the command line.
4. The result image will be displayed, showing the differences in red.

## How it works
The script uses OpenCV and NumPy to perform the following steps:

1. Load the input image.
2. Define the regions of interest (ROIs) containing the two almost identical images.
3. Crop the left and right ROIs from the input image.
4. Apply a filter kernel to the left and right ROIs.
5. Compute the absolute difference between the filtered left and right ROIs.
6. Convert the absolute difference image to grayscale.
7. Set a threshold value and create a binary image based on the grayscale difference image.
8. Convert the left ROI to grayscale and create a red image.
9. Combine the left grayscale image and the red image based on the binary difference image.
10. Display the result.

## Changelog
- 2023/04/22: released "ver 1.00" (spot_the_differences_1.00.py)

## Credits
- This script was created by @ywebjp and edited by ChatGPT.
- The sample image used in this project was borrowed from https://www.my-kaigo.com/pub/carers/otasuke/machigaisagashi/difficulty_01/#q_02 . All rights reserved by the original owner.
