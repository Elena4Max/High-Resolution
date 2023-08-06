import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse
import numpy
import random
  
# Argument parsing variable declared
ap = argparse.ArgumentParser()
  
ap.add_argument("-i", "--image",
                required=True,
                help="Path to folder")
                
ap.add_argument("-width", "--width",
                required=True,
                help="Resize width")
                
ap.add_argument("-hieght", "--hieght",
                required=True,
                help="Resize hieght")
  
args = vars(ap.parse_args())
  
# Find all the images in the provided images folder
mypath = args["image"]
resize_width = args["width"]
resize_hieght = args["hieght"]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
images = numpy.empty(len(onlyfiles), dtype=object)
  
# Iterate through every image
# and resize all the images.
for n in range(0, len(onlyfiles)):
  
    path = join(mypath, onlyfiles[n])
    images[n] = cv2.imread(join(mypath, onlyfiles[n]),
                           cv2.IMREAD_UNCHANGED)
  
    # Load the image in img variable
    img = cv2.imread(path, 1)
  
    # Define a resizing dimensions
    resized_dimensions = (int(resize_width), int(resize_hieght))
  
    # Create resized image using the calculated dimensions
    resized_image = cv2.resize(img, resized_dimensions,
                               interpolation=cv2.INTER_AREA)
  
    # Save the image in Output Folder
    cv2.imwrite(
      'output/' + str(random.randrange(1000000, 9999999)) + '.png', resized_image)
  
print("Images resized Successfully")
