import streamlit as st
import torchvision.models as models
import torch
import torchvision.transforms as transforms
from PIL import Image


img = st.file_uploader("Upload a file", type=(["png"]))
if img is not None:
    vgg16_model = models.vgg16(pretrained=True)
    
    # # Apply transformations to the image
    # transform = transforms.Compose([
    #     transforms.Resize(256),
    #     transforms.CenterCrop(224),
    #     transforms.ToTensor(),
    #     transforms.Normalize(
    #         mean=[0.485, 0.456, 0.406],
    #         std=[0.229, 0.224, 0.225]
    #     )
    # ])
    # img = transform(img)
    
    # # Add a batch dimension to the image
    # img = img.unsqueeze(0)
    
    # Set the model to evaluation mode
    vgg16_model.eval()
    
    # Pass the image through the model
    with torch.no_grad():
        output = vgg16_model(img)
    
    # Get the index of the predicted class
    pred_idx = torch.argmax(output)
    
    # Get the label for the predicted class
    labels = open("imagenet_classes.txt").read().splitlines()
    label = labels[pred_idx]
    
    st.write(label)
else:
    path_in = None
