import cv2
import os

cv_img = []
input_folder = 'C:/Users/ibrah/OneDrive/Desktop/outputs'


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images





