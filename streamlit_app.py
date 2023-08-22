import streamlit as st

import torchvision.models as models

vgg16 = models.vgg16(pretrained=True)

import torch
import torchvision.transforms as transforms
from PIL import Image


f = st.file_uploader("Upload a file", type=(["png"]))
if f is not None:
    # Apply transformations to the image
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    img = transform(img)
    
    # Add a batch dimension to the image
    img = img.unsqueeze(0)
    
    # Set the model to evaluation mode
    vgg16.eval()
    
    # Pass the image through the model
    with torch.no_grad():
        output = vgg16(img)
    
    # Get the index of the predicted class
    pred_idx = torch.argmax(output)
    
    # Get the label for the predicted class
    labels = open("imagenet_classes.txt").read().splitlines()
    label = labels[pred_idx]
    
    st.write(label)
else:
    path_in = None
