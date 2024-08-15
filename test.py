import os, cv2
# import numpy as np
# import pandas as pd
# import random, tqdm
# import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

import torch
# import torch.nn as nn
# from torch.utils.data import DataLoader
# import albumentations as album
from torchvision import models
import torchvision.transforms.functional as fn
import segmentation_models_pytorch as smp
import map


def visualize(image):
    plt.figure(figsize=(50, 50))
    plt.axis('off')
    plt.imshow(image)
    plt.show()

def load_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

# select_classes = ['urban_land', 'agriculture_land', 'rangeland', 'forest_land', 'water', 'barren_land', 'unknown']
# ENCODER = 'resnet50'
# ENCODER_WEIGHTS = 'imagenet'
# CLASSES = select_classes
# ACTIVATION = 'sigmoid' # could be None for logits or 'softmax2d' for multiclass segmentation

# # create segmentation model with pretrained encoder
# best_model = smp.DeepLabV3Plus(
#     encoder_name=ENCODER, 
#     encoder_weights=ENCODER_WEIGHTS, 
#     classes=len(CLASSES), 
#     activation=ACTIVATION,
# )

# preprocessing_fn = smp.encoders.get_preprocessing_fn(ENCODER, ENCODER_WEIGHTS)
map.generateTileUrl(-55.10887, -7.22997, (3,19), 256)
# image=load_image('./100877_sat.jpg')
# print(image)

# if os.path.exists('./best_model.pth'):
#     DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#     # Define the model architecture
#     best_model = smp.DeepLabV3Plus(
#         encoder_name="resnet101",  # Change encoder based on your training configuration
#         encoder_weights=None,       # Ensure to load weights from checkpoint
#         classes=1                   # Adjust number of classes based on your task
#     )
    
#     # Load pre-trained weights from the .pth file
#     checkpoint = torch.load('best_model.pth', map_location=DEVICE)
#     best_model.load_state_dict(checkpoint['model_state_dict'])
#     best_model.to(DEVICE)
#     best_model.eval()
#     print('Loaded DeepLabV3+ model from this run.')
#     #best_model = torch.load('./best_model.pth', map_location=DEVICE)
#     image=load_image('./test.jpg')
#     image = cv2.resize(image, (1024, 1024))
#     visualize(image)
#     output = best_model(torch.tensor(image).permute(2, 0, 1).unsqueeze(0).float().to(DEVICE))
#     visualize(output)

    

