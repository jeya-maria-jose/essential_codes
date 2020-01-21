import torch
import torchvision
from torch import nn
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.utils import save_image
from torchvision.datasets import MNIST
import torch.nn.functional as F
import os
import matplotlib.pyplot as plt
import torch.utils.data as data
from PIL import Image
import numpy as np
from torchvision.utils import save_image
import torch
import glob

location = '/home/jeyamariajose/Baselines/pytorch-beginner/08-AutoEncoder/sample/*.jpg'

class autoencoder(nn.Module):
    def __init__(self):
        super(autoencoder, self).__init__()
        self.encoder1 = nn.Conv2d(3, 16, 3, stride=3, padding=1)  # b, 16, 10, 10
        self.encoder2=   nn.Conv2d(16, 8, 3, stride=2, padding=1)  # b, 8, 3, 3
        self.decoder1 = nn.ConvTranspose2d(8, 16, 3, stride=2)  # b, 16, 5, 5
        self.decoder2 =   nn.ConvTranspose2d(16, 8, 5, stride=3, padding=1)  # b, 8, 15, 1
        self.decoder3 =   nn.ConvTranspose2d(8, 3, 2, stride=2, padding=1)  # b, 1, 28, 28
    

    def forward(self, x):
        out = F.relu(F.max_pool2d(self.encoder1(x),2,2))
        out = F.relu(F.max_pool2d(self.encoder2(out),1,2))        
        out = F.relu(self.decoder1(out))
        out = F.relu(self.decoder2(out))
        out = F.tanh(self.decoder3(out))
        return out



class rautoencoder(nn.Module):
    def __init__(self):
        super(rautoencoder, self).__init__()
        self.encoder1 = nn.Conv2d(64, 32, 3, stride=2, padding=1)  # b, 16, 10, 10
            
        self.encoder2 = nn.Conv2d(32, 16, 3, stride=2, padding=1)  # b, 8, 3, 3
            
        self.encoder3 = nn.Conv2d(16, 3, 3, stride=2)  # b, 8, 3, 3

        self.decoder1 = nn.ConvTranspose2d(3, 16, 3, stride=2)  # b, 16, 5, 5
            
        self.decoder2 = nn.ConvTranspose2d(16, 32, 5, stride=2, padding=1)
        self.decoder3 = nn.ConvTranspose2d(32, 64, 2, stride=2, padding=1)  # b, 1, 28, 28
            

    def forward(self, x):
        # print(x.shape)
        out = F.relu(self.decoder1(x))
        print(out.shape)
        out = F.relu(self.decoder2(out))
        print(out.shape)
        out = F.relu(self.decoder3(out))
        print(out.shape)
        out = F.relu(F.max_pool2d(self.encoder1(out),1))
        print(out.shape)
        out = F.relu(F.max_pool2d(self.encoder2(out),1,1))        
        print(out.shape)
        out = F.tanh(self.encoder3(out))        
        print(out.shape)
        return out

model = rautoencoder().cuda().load_state_dict(torch.load("/home/jeyamariajose/Baselines/pytorch-beginner/08-AutoEncoder/scripts/conv_autoencoder.pth"))

for filename in glob.iglob(location):

	img = cv2.imread(filename)
	img = torch.Tensor(img).cuda()
    model = model.eval()
    output = model(img)