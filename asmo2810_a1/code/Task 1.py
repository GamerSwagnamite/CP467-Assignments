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
# ----------------------------------------------------------------
# 1. Image Interpolation
# ----------------------------------------------------------------
# read image 1
img1 = cv.imread("img1.tif")
assert img1 is not None, "file could not be read, check with os.path.exists()"

# scale image 1 down to 1/16th its size
height, width = img1.shape[:2]
resize = cv.resize(img1, None, fx = 0.25, fy = 0.25)

# rescale downscaled image using different interpolations
# nearest neighbor interpolation implementation from scratch
img1_temp = np.zeros((height, width), dtype=np.uint8)

# nearest neighbor interpolation using OpenCV's built-in function
resize = cv.resize(img1, img1_temp, fx = 4, fy = 4, interpolation = cv.INTER_NEAREST)

# bilinear interpolation implementation from scratch

# bilinear interpolation using OpenCV's built-in function

# bicubic interpolation using OpenCV's built-in function