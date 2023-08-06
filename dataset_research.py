import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse
import numpy
import random
from statistics import mean
from matplotlib import pyplot as plt
from collections import Counter

# Argument parsing variable declared
ap = argparse.ArgumentParser()
  
ap.add_argument("-i", "--image",
                required=True,
                help="Path to folder")
                
args = vars(ap.parse_args())
  
# Find all the images in the provided images folder
mypath = args["image"]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
images = numpy.empty(len(onlyfiles), dtype=object)

brightness = {}

# Iterate through every image
# and resize all the images.
for n in range(0, len(onlyfiles)):
  
    path = join(mypath, onlyfiles[n])
    images[n] = cv2.imread(join(mypath, onlyfiles[n]),
                           cv2.IMREAD_UNCHANGED)
  
    # Load the image in img variable
    img = cv2.imread(path, 1)
    
    # Convert image to HSV
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(img)
    
    val = mean(np.concatenate(V))
    if val not in brightness:
        brightness[val] = 1
    else:
        brightness[val] = brightness[val] + 1

hist = Counter(brightness)

plt.bar(hist.keys(), hist.values()), plt.grid(True)
plt.xlabel('Mean brightness'), plt.ylabel('Counts')

plt.show()
