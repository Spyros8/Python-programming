#detect corners using harris


import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage.io import imread

#note both work
image_new = cv2.imread('boat.tar/img1.pgm',-1) 
print(image_new.shape)
image = cv2.cvtColor(image_new, cv2.COLOR_BGR2RGB)
print(image)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(gray)
gray = np.float32(gray)


dst = cv2.cornerHarris(gray,2,3,0.04)
print(dst.shape)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
# Define your thresh hold (thresh value inversely proportional to corner visbility )
thresh = 0.01*dst.max()

# Create copy of rgb image to draw corners on it.
corner_image = np.copy(image)

# Iterate through all the corners and draw them on the image 
for j in range(0, dst.shape[0]):
    for i in range(0, dst.shape[1]):
        if(dst[j,i] > thresh):
            # image, center pt, radius, color, thickness
            cv2.circle( corner_image, (i, j), 1, (0,0,255), 1)
  
plt.imshow(corner_image)
plt.imsave("_cornerDetected_image.jpg",corner_image)


image_new = cv2.imread('boat.tar/img2.pgm',-1) 
print(image_new.shape)
image = cv2.cvtColor(image_new, cv2.COLOR_BGR2RGB)
print(image)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(gray)
gray = np.float32(gray)


dst = cv2.cornerHarris(gray,2,3,0.04)
print(dst.shape)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
# Define your thresh hold (thresh value inversely proportional to corner visbility )
thresh = 0.01*dst.max()

# Create copy of rgb image to draw corners on it.
corner_image = np.copy(image)

# Iterate through all the corners and draw them on the image 
for j in range(0, dst.shape[0]):
    for i in range(0, dst.shape[1]):
        if(dst[j,i] > thresh):
            # image, center pt, radius, color, thickness
            cv2.circle( corner_image, (i, j), 1, (0,0,255), 1)
  
plt.imshow(corner_image)
plt.imsave("_cornerDetected_image_rotated.jpg",corner_image)


"""  """