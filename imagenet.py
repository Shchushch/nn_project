import torch
import torchvision
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms as T
from torchvision import io
from torchmetrics.classification import BinaryAccuracy
import torchutils as tu
import json
import numpy as np
#import matplotlib.pyplot as plt
import os
from PIL import Image

from torchvision.models import inception_v3,Inception_V3_Weights
model = inception_v3(pretrained=True)


with open('imagenet_classes.json', 'r') as f:
    class_labels = json.load(f)
class_labels=[value for _,value in class_labels.items()]
def img_class(img):
    transform = Inception_V3_Weights.IMAGENET1K_V1.transforms()
    
    input_image = transform(img).unsqueeze(0) # Добавьте размерность пакета (batch dimension)
    
    device = torch.device("cuda" if torch.cuda.is_available() else 'mps')
    model.to(device)
    model.eval()
    input_image = input_image.to(device)
    with torch.no_grad():
        output = model(input_image)
    return class_labels[torch.argmax(output).item()]
