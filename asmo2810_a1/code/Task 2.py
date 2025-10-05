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
# 2. Point Operations
# ----------------------------------------------------------------
# read image
script_dir = os.path.dirname(os.path.abspath(__file__))     # get our current directory
assignment_dir = os.path.dirname(script_dir)                # go up one level to the assignment directory
image_path = os.path.join(assignment_dir, "images", "img2.tif")     # construct the full path to the image
img2 = cv.imread(image_path)    # do the read
assert img2 is not None, "file could not be read, check with os.path.exists()"

# find the negative of img2


# apply power law transformation to img2


# apply bit-slicing on the image
