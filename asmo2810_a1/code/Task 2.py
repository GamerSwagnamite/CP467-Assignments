# ----------------------------------------------------------------
# CP467 Assignment 1
# ----------------------------------------------------------------
# Name: Jordan Asmono
# ID: 210922810
# Email: asmo2810@mylaurier.ca
# Date: 2025-10-01
# ----------------------------------------------------------------
# Imports
# ----------------------------------------------------------------
import numpy as np
import cv2 as cv
import os

# ----------------------------------------------------------------
# helper function for exports
# ----------------------------------------------------------------
def img_write(image, filename):
    image_path = os.path.join(assignment_dir, "output images", filename)
    cv.imwrite(image_path, image)

# ----------------------------------------------------------------
# 2. Point Operations
# ----------------------------------------------------------------
# read image
script_dir = os.path.dirname(os.path.abspath(__file__))     # get our current directory
assignment_dir = os.path.dirname(script_dir)                # go up one level to the assignment directory
image_path = os.path.join(assignment_dir, "images", "img2.tif")     # construct the full path to the image
img2 = cv.imread(image_path, cv.IMREAD_GRAYSCALE)    # do the read
assert img2 is not None, "file could not be read, check with os.path.exists()"

# ----------------------------------------------------------------
# find the negative of img2
# ----------------------------------------------------------------
img2_negative = cv.bitwise_not(img2)
img_write(img2_negative, "img2_negative.tif")

# ----------------------------------------------------------------
# apply power law transformation to img2
# ----------------------------------------------------------------
height, width = img2.shape[:2]
img2_power = np.zeros((height, width), dtype=np.uint8)

# change constant and gamma's values to get new power law results
constant = 2
gamma = 0.9

# test run using a double for loop to iterate over every pixel
for i in range(height):
    for j in range(width):
        value = constant * (img2[i][j] ** gamma)
        img2_power[i][j] = np.clip(value, 0, 255).astype(np.uint8)

img_write(img2_power, "img2_power.tif")

# ----------------------------------------------------------------
# apply bit-slicing on the image
# ----------------------------------------------------------------
img2_bitplane = np.zeros((height, width), dtype=np.uint8)

for i in range(8):
    bitplane = ((img2 >> i) & 1) * 255
    img_write(bitplane, f"img2_b{i+1}.tif")