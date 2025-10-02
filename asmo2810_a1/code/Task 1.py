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

# debug
import os
# ----------------------------------------------------------------
# 1. Image Interpolation
# ----------------------------------------------------------------
# read image 1

# apparently vscode is struggling to locate the image files so we're doing this the hard way
script_dir = os.path.dirname(os.path.abspath(__file__))     # get our current directory
assignment_dir = os.path.dirname(script_dir)                # go up one level to the assignment directory
image_path = os.path.join(assignment_dir, "images", "img1.tif")     # construct the full path to the image
img1 = cv.imread(image_path)    # do the read
assert img1 is not None, "file could not be read, check with os.path.exists()"

# scale image 1 down to 1/16th its size
height, width = img1.shape[:2]
img1_small = cv.resize(img1, None, fx = 0.25, fy = 0.25)

# rescale downscaled image using different interpolations
# nearest neighbor interpolation implementation from scratch
img1_temp = np.zeros((height, width), dtype=np.uint8)

# nearest neighbor interpolation using OpenCV's built-in function
img1_nearest_cv = cv.resize(img1_small, (width, height), interpolation = cv.INTER_NEAREST)
image_path = os.path.join(assignment_dir, "output images", "img1_nearest_cv.tif")
cv.imwrite(image_path, img1_nearest_cv)

# bilinear interpolation implementation from scratch

# bilinear interpolation using OpenCV's built-in function

# bicubic interpolation using OpenCV's built-in function