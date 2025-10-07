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
# helper functions for imports and exports
# ----------------------------------------------------------------
def img_write(image, filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assignment_dir = os.path.dirname(script_dir)
    image_path = os.path.join(assignment_dir, "output images", filename)
    cv.imwrite(image_path, image)
    return

def img_read(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))     # get our current directory
    assignment_dir = os.path.dirname(script_dir)                # go up one level to the assignment directory
    image_path = os.path.join(assignment_dir, "images", filename)     # construct the full path to the image
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    assert image is not None, "file could not be read, check with os.path.exists()"
    return image

# ----------------------------------------------------------------
# 3. Histogram Processing
# ----------------------------------------------------------------
# read images
img3 = img_read("img3.tif")
img4 = img_read("img4.tif")
img5 = img_read("img5.tif")

# ----------------------------------------------------------------
# apply histogram equalization on img3
# ----------------------------------------------------------------
height, width = img3.shape[:2]
img3_equalized = np.zeros((height, width), dtype=np.uint8)

hist, bins = np.histogram(img3.flatten(), 256, [0,256])
cdf = hist.cumsum()
cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
img3_equalized = np.interp(img3.flatten(), bins[:-1], cdf_normalized)

img_write(img3_equalized.astype(np.uint8).reshape(img3.shape), "img3_equalized.tif")

# ----------------------------------------------------------------
# apply histogram specialization on img4
# ----------------------------------------------------------------


