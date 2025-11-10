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
hist3, bins3 = np.histogram(img3.flatten(), 256, [0,256])
cdf3 = hist3.cumsum()
cdf3_normalized = (cdf3 - cdf3.min()) * 255 / (cdf3.max() - cdf3.min())
img3_equalized = np.interp(img3.flatten(), bins3[:-1], cdf3_normalized)

img_write(img3_equalized.astype(np.uint8).reshape(img3.shape), "img3_equalized.tif")

# ----------------------------------------------------------------
# apply histogram specialization on img4
# ----------------------------------------------------------------
# hist4, bins4 = np.histogram(img4.flatten(), 256, [0,256])
# hist5, bins5 = np.histogram(img5.flatten(), 256, [0,256])

# cdf4 = hist4.cumsum()
# cdf5 = hist5.cumsum()

# cdf4_normalized = (cdf4 - cdf4.min()) * 255 / (cdf4.max() - cdf4.min())
# cdf5_normalized = (cdf5 - cdf5.min()) * 255 / (cdf5.max() - cdf5.min())





