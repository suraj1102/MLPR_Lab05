import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
import cv2

# Check if data is loading or not 
def load_image(img_path):
    img = cv2.imread(img_path)
    if img is None:
        return False
    return True

images = ["Dr_Shashi_Tharoor.jpg", "Plaksha_Faculty.jpg"]
for img_path in images:
    print(load_image(img_path))