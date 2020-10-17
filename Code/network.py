import torch
import numpy as np 

class net(torch.nn.Module):
  def  __init__(self,input_size,output_classes):
    # input:  torch.Size([batch_size, input_size])
    super().__init__()
    self.fc1=torch.nn.Linear(input_size,1024) 
    self.fc2=torch.nn.Linear(1024,1024)
    self.fc3=torch.nn.Linear(1024,512)
    self.fc4=torch.nn.Linear(512,output_classes)
    self.relu=torch.nn.ReLU()    

  def forward(self,x):
    out=self.fc1(x)
    out=self.relu(out)

    out=self.fc2(out)
    out=self.relu(out)

    out=self.fc3(out)
    out=self.relu(out)

    out=self.fc4(out)

    return out
