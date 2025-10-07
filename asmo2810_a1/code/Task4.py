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
# 4. Image Filtering
# ----------------------------------------------------------------
# read image
img6 = img_read("img6.tif")