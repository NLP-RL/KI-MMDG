# -*- coding: utf-8 -*-
"""DII_Symptom.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-1YgAAYmPKTSI9px8jMivvh1ZFeH50iY
"""

from google.colab import drive
drive.mount('/content/drive')

"""# Data

# Train Data
"""

import pickle

with open('/content/drive/MyDrive/goal_set.p','rb') as f:
    train_data = pickle.load(f)

s_list = ['Swollen eye',  'Mouth ulcer',  'Skin dryness, peeling, scaliness, or roughness',  'Neck swelling',  'Skin irritation', 'Swollen or red tonsils', 'Knee swelling', 'Redness in ear', 'Dry or flaky scalp', 'Skin rash', 'Itchy eyelid', 'Hand or finger lump or mass', 'Skin growth', 'Eye redness', 'Foot or toe swelling', 'Lip swelling',  'Eyelid lesion or rash']

l = []
temp = []
sno = []
sno_dict = {}
for symptom in s_list:
  for i in range(24000):
    traind = train_data['train'][i]['goal']
    
    try:
      traind.pop("request_slots")
    except:
      pass
    for key in traind:
      x = traind[key]
      
      for key2 in x:
        
        if key2 == symptom:
          sno.append(i)
          break
  if len(sno)>0:
    sno_dict[symptom] = sno[:100]
  sno = []

for i in sno_dict:
  
  print(i, len(sno_dict[i]))

fs = {}
cnt = 0
for symptom in sno_dict:
  
  for i in sno_dict[symptom]:
    td = train_data['train'][i]['goal']
    
    for key in traind:
      x = td[key]
      
      for key2 in x:
        
        if key2==symptom:
          break
        temp.append(key2)

    l.append([temp, symptom, cnt])
    temp = []
  cnt = cnt + 1
  fs[symptom] = l
  l = []

for i in fs:
  
  for j in fs[i]:
    if j[0] == []:
      fs[i].remove(j)
      

for i in fs:
  
  print(i, len(fs[i]))

import matplotlib.pyplot as plt
import os
import tensorflow as tf
import matplotlib
matplotlib.style.use('ggplot')

IMAGE_SHAPE = (224, 224)
TRAINING_DATA_DIR = '/content/drive/MyDrive/final_ee_data2/train'
VALID_DATA_DIR = '/content/drive/MyDrive/final_ee_data2/test'

import copy 
final_data  = copy.deepcopy(fs)

print(len(final_data))

import os
import re

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

bd = {'Swollen eye': 'S1',  'Mouth ulcer': 'S108',  'Skin dryness, peeling, scaliness, or roughness':'S11',  'Neck swelling': 'S159',  'Skin irritation': 'S177', 'Swollen or red tonsils': 'S181', 'Knee swelling' : 'S205', 'Redness in ear' : 'S22', 'Dry or flaky scalp': 'S251', 'Skin rash': 'S31', 'Itchy eyelid' : 'S37', 'Hand or finger lump or mass':'S39', 'Skin growth':'S4', 'Eye redness':'S5', 'Foot or toe swelling':'S50', 'Lip swelling': 'S51',  'Eyelid lesion or rash':'S74'}
for index in final_data:
  path = "/content/drive/MyDrive/final_ee_data2/train/" + bd[index]
  dirlist = sorted_alphanumeric(os.listdir(path))
  fdirlist = dirlist + dirlist
  symptom = index
  for i in range(len(final_data[symptom])):
    temp_list = final_data[symptom][i]
    temp_list[1] = bd[index]+'/'+fdirlist[i]
    final_data[symptom][i] = temp_list

print(len(final_data))

for i in final_data:
  print(final_data[i])
pickle.dump(final_data, open('/content/drive/MyDrive/train_ca_v3.p', 'wb'))

"""# Test_data"""

import pickle

with open('/content/drive/MyDrive/goal_set.p','rb') as f:
    train_data = pickle.load(f)

s_list = ['Swollen eye',  'Mouth ulcer',  'Skin dryness, peeling, scaliness, or roughness',  'Neck swelling',  'Skin irritation', 'Swollen or red tonsils', 'Knee swelling', 'Redness in ear', 'Dry or flaky scalp', 'Skin rash', 'Itchy eyelid', 'Hand or finger lump or mass', 'Skin growth', 'Eye redness', 'Foot or toe swelling', 'Lip swelling',  'Eyelid lesion or rash']

l = []
temp = []
sno = []
sno_dict = {}
for symptom in s_list:
  for i in range(6000):
    traind = train_data['test'][i]['goal']
    
    try:
      traind.pop("request_slots")
    except:
      pass
    for key in traind:
      x = traind[key]
      
      for key2 in x:
        
        if key2 == symptom:
          sno.append(i)
          break
  if len(sno)>0:
    sno_dict[symptom] = sno[:5]
  sno = []

for i in sno_dict:
  
  print(i, len(sno_dict[i]))

fs = {}
cnt = 0
for symptom in sno_dict:
  
  for i in sno_dict[symptom]:
    td = train_data['test'][i]['goal']
    
    for key in traind:
      x = td[key]
      
      for key2 in x:
        
        if key2==symptom:
          break
        temp.append(key2)

    l.append([temp, symptom, cnt])
    temp = []
  cnt = cnt + 1
  fs[symptom] = l
  l = []

for i in fs:
  for j in fs[i]:
    if j[0] == []:
      fs[i].remove(j)
      
big_list = []
fdict = {}
for i in fs:
  fdict[i] = len(fs[i])
  big_list.append(i)

import matplotlib.pyplot as plt
import os
import tensorflow as tf
import matplotlib
matplotlib.style.use('ggplot')

import copy 
final_data  = copy.deepcopy(fs)

import os
import re

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

bd = {'Swollen eye': 'S1',  'Mouth ulcer': 'S108',  'Skin dryness, peeling, scaliness, or roughness':'S11',  'Neck swelling': 'S159',  'Skin irritation': 'S177', 'Swollen or red tonsils': 'S181', 'Knee swelling' : 'S205', 'Redness in ear' : 'S22', 'Dry or flaky scalp': 'S251', 'Skin rash': 'S31', 'Itchy eyelid' : 'S37', 'Hand or finger lump or mass':'S39', 'Skin growth':'S4', 'Eye redness':'S5', 'Foot or toe swelling':'S50', 'Lip swelling': 'S51',  'Eyelid lesion or rash':'S74'}
for index in final_data:
  path = "/content/drive/MyDrive/final_ee_data2/test/" + bd[index]
  dirlist = sorted_alphanumeric(os.listdir(path))
  fdirlist = dirlist + dirlist
  symptom = index
  for i in range(len(final_data[symptom])):
    temp_list = final_data[symptom][i]
    temp_list[1] = bd[index]+'/'+fdirlist[i]
    final_data[symptom][i] = temp_list

for i in final_data:
  print(final_data[i])
pickle.dump(final_data, open('/content/drive/MyDrive/test_ca_v4.p', 'wb'))

"""# Model"""

# !pip install transformers

import io
import re
from transformers import AutoTokenizer
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import pandas as pd
from tensorflow import keras
import matplotlib.pyplot as plt
from transformers import pipeline

#Bert
model_name = "emilyalsentzer/Bio_ClinicalBERT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline('feature-extraction',model=model_name, tokenizer=tokenizer)

def lambda_func(row):
    tokens = tokenizer(row[0],padding=True,truncation=True,return_tensors="pt")
    if len(tokens['input_ids'])>512:
        tokens = re.split(r'\b', row[0])
        tokens= [t for t in tokens if len(t) > 0 ]
        row[0] = ''.join(tokens[:512])
    row['vectors'] = classifier(row[0])[0][0]        
    return row

def process(progress_notes):     
    progress_notes = progress_notes.apply(lambda_func, axis=1)
    return progress_notes

import torch
import torch.nn as nn  # All neural network modules, nn.Linear, nn.Conv2d, BatchNorm, Loss functions
import torch.optim as optim  # For all Optimization algorithms, SGD, Adam, etc.
import torchvision.transforms as transforms  # Transformations we can perform on our dataset
import torchvision
import os
import pandas as pd
from skimage import io
from torch.utils.data import (
    Dataset,
    DataLoader,
)  # Gives easier dataset managment and creates mini batches
import albumentations as A
from PIL import Image

import pickle
with open('/content/drive/MyDrive/train_ca_v3.p','rb') as f:
    train_data = pickle.load(f)
with open('/content/drive/MyDrive/test_ca_v4.p','rb') as f:
    test_data = pickle.load(f)
print(len(train_data))
print(len(test_data))
train_list = []
test_list = []
for i in train_data:
  for j in train_data[i]:
    train_list.append(j)
for i in test_data:
  for j in test_data[i]:
    test_list.append(j)

def embedding(emb): 
  pn=pd.DataFrame([emb])
  pn = process(pn)
  pn = pn['vectors'][0]
  pn = np.array(pn)
  return pn

class Symptoms(Dataset):
    def __init__(self, data_list, root_dir,context_no, transform=None):
        self.annotations = data_list
        self.context_no = context_no
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.annotations)

    def embedding(emb): 
        pn=pd.DataFrame([emb])
        pn = process(pn)
        pn = pn['vectors'][0]
        pn = np.array(pn)
        return pn

    def __getitem__(self, index):
        img_path = os.path.join(self.root_dir, self.annotations[index][1])
        
        image = np.array(Image.open(img_path).convert('RGB'))
        y_label = torch.tensor(int(self.annotations[index][2]))
        emb_list = self.annotations[index][0]
        x = self.context_no
        temp_list = emb_list[-x:]
        change_dic = {'Skin dryness, peeling, scaliness, or roughness': 'Skin dryness',  
                        'Swollen or red tonsils':'Swollen tonsils',  'Dry or flaky scalp': 'Dry scalp', 
                        'Hand or finger lump or mass': 'Hand lump', 
                       'Foot or toe swelling': 'Foot swelling',  'Eyelid lesion or rash': 'Eyelid rash'}
        for i in range(len(temp_list)):
          if temp_list[i] in change_dic:
            temp_list[i] = change_dic[temp_list[i]]
        seperator = '$'
        final_embedding_string = seperator.join(temp_list)
        emb_array = embedding(final_embedding_string)
        emb_array = torch.tensor(emb_array)
        ls1 = []
        ls1.append(self.annotations[index][1])
        transform = A.Compose(
        [A.Resize(width=224, height=224)],
        )
        augmentations = transform(image=image)
        image = augmentations["image"]
        

        if self.transform:
            image = self.transform(image)

        return (image, y_label, emb_array,ls1)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hyperparameters
in_channel = 3
num_classes = 17

batch_size = 32


# Load Data
train_dataset = Symptoms(
    data_list = train_list,
    root_dir='/content/drive/MyDrive/final_ee_data2/train',
    context_no = 3,
    transform=transforms.ToTensor(),
)
test_dataset = Symptoms(
    data_list = test_list,
    root_dir='/content/drive/MyDrive/final_ee_data2/test',
    context_no = 3,
    transform=transforms.ToTensor(),
)

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

import sys
from tqdm import tqdm
import time
import copy

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device

import torchvision.models as models
model = torch.hub.load('pytorch/vision:v0.10.0','vgg19',pretrained = True)
for param in model.parameters():
    param.requires_grad = False
model = model.to(device)

import torch.nn.functional as F
class Model(nn.Module):
    def __init__(self, original_model):
        super(Model, self).__init__()
        self.features = nn.Sequential(*list(original_model.children())[:-1])
        self.conv1 = nn.Conv2d(512, 1024,  3, 1,  bias=False, padding="valid")
        self.conv2 = nn.Conv2d(1024, 512,  3, 1, bias=False, padding="valid")
        self.conv3 = nn.Conv2d(512, 512,  3, 2, bias=False, padding="valid")
        self.linear = nn.Linear(512, 512)
        self.linear1 = nn.Linear(1280,512)
        self.output = nn.Linear(512,17)

        
    def forward(self, x, e, t):
        x = self.features(x)
        
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = F.max_pool2d(x, kernel_size=x.size()[2:])
        
        a,b,c,d = x.shape
        x = torch.reshape(x, (a, -1))
        
        x = F.relu(self.linear(x))
        x = torch.cat([x, e], dim=1)
        x = F.relu(self.linear1(x))
        x1 = x
        ls2 = []
        
        for i in t:
          for j in i:
            str1 = ''
            str1 = str1 + j
          
            ls2.append(str1)
        x1 = x
        dict1 = dict(zip(ls2,x1))
        x = self.output(x)
        return x, dict1



model_final = Model(model).to(device)

print(model_final)

print(model)

# !python --version

from tqdm import tqdm
import numpy as np
from PIL import Image
from torchvision import transforms
learning_rate = 1e-3
criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model_final.parameters(), lr=learning_rate, weight_decay = 1e-5)

num_epochs = 15

def check_accuracy(loader, model):
    num_correct = 0
    num_samples = 0
    model.eval()

    with torch.no_grad():
        dict_test = {}
        for x, y, e, p in loader:

            x = x.to(device=device)
            e = e.to(device=device)
            y = y.to(device=device)

            scores, dict_2 = model(x, e.float(),p)
            
            dict_test = Merge(dict_test, dict_2)
            _, predictions = scores.max(1)
            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)


    model.train()
    return num_correct/num_samples, dict_test

def save_checkpoint(model, optimizer, filename):
    print("=> Saving checkpoint")
    checkpoint = {
        "state_dict": model.state_dict(),
        "optimizer": optimizer.state_dict(),
    }
    torch.save(checkpoint, filename)
def Merge(dict_1, dict_2):
  dict3 = {**dict_1,**dict_2}
  return dict3


# Train Network
dict_train_test = {}
acc_list = {}
for epoch in range(num_epochs):
    print("\n\nCurrent EPOCH:", epoch)
    dict_train = {}
    for batch_idx, (data, targets, embeddings, paths) in enumerate(tqdm(train_loader)):
        data = data.to(device=device)
        embeddings = embeddings.to(device=device)
        targets = targets.to(device=device)
        scores, dict_1 = model_final(data, embeddings.float(), paths)
        dict_train = Merge(dict_train, dict_1)
        loss = criterion(scores, targets)
        if batch_idx==47:
          print(f'Loss at step {batch_idx} = ',loss)
        if batch_idx%5 ==0:
          print(f'Loss at step {batch_idx} = ',loss)

        # backward
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    accuracy, dict_test = check_accuracy(test_loader, model_final)
    
    
    # if epoch%1==0:
    #   fname  = '/content/drive/MyDrive/multimodal_AAAI_withContext/s22/'+'v1_checkpoint_'+str(epoch)+'.pth.tar'
    #   save_checkpoint(model_final, optimizer, fname)
    dict_train_test['test'+str(epoch)] = dict_test
    dict_train_test['train'+str(epoch)] = dict_train
    print(f"Accuracy at EPOCH {epoch} on test set: {accuracy*100:.2f}")

learning_rate = 1e-3
criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model_final.parameters(), lr=learning_rate, weight_decay = 1e-5)

def load_checkpoint(checkpoint_file, model, optimizer, lr):
    print("=> Loading checkpoint")
    checkpoint = torch.load(checkpoint_file, map_location=device)
    model.load_state_dict(checkpoint["state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer"])
    for param_group in optimizer.param_groups:
        param_group["lr"] = lr
path = '/content/drive/MyDrive/multimodal_aaai/ca_weights/v3/Copy of Copy of v3_checkpoint_5_88_34.pth.tar'
load_checkpoint(path, model_final,optimizer, learning_rate)

test_ls = []
import numpy
y_pred = []
y_true = []
dict_final_pred = {}
def check_accuracy(loader, model,y_true,y_pred):
    num_correct = 0
    num_samples = 0
    model.eval()

    with torch.no_grad():
        for x, y, e, p in loader:
            x = x.to(device=device)
            e = e.to(device=device)
            y = y.to(device=device)
            for i in p:
              for j in i:
                str1 = ''
                str1 = str1 + j
            
            lis1 = numpy.array(y.cpu())
            lis1 = lis1.tolist()
            y_true = y_true + lis1
            scores,____ = model(x,e.float(),p)
            m = nn.Softmax(dim=1)
            output = m(scores)
            _, predictions = output.max(1)
            d1 = {0: 'S1', 1 :'S108', 2:'S11', 3:'S159', 4:'S177', 5:'S181', 6:'S205', 7:'S22', 8:'S251', 9:'S31', 10:'S37'
                  , 11:'S39', 12:'S4', 13: 'S5', 14:'S50', 15:'S51', 16:'S74'}
            d2 = {'S1':'Swollen eye', 'S108':'Mouth ulcer', 'S11':'Skin dryness, peeling, scaliness, or roughness', 
                  'S159':'Neck swelling', 'S177': 'Skin irritation','S181':'Swollen or red tonsils', 
                  'S205':'Knee swelling', 'S22': 'Redness in ear' , 'S251': 'Dry or flaky scalp','S31': 'Skin rash', 
                  'S37':'Itchy eyelid','S39': 'Hand or finger lump or mass','S4': 'Skin growth','S5' : 'Eye redness', 
                  'S50':'Foot or toe swelling', 'S51':'Lip swelling', 'S74':  'Eyelid lesion or rash'}
            test_ls.append((str1,d2[d1[int(predictions[0])]],output))
            lis2 = numpy.array(predictions.cpu())
            lis2 = lis2.tolist()
            y_pred = y_pred + lis2
    
              
            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)


    model.train()
    return num_correct/num_samples, y_true, y_pred

a, y_true, y_pred =check_accuracy(test_loader, model_final,y_true, y_pred)
print(f"Accuracy on test set: {a*100:.2f}")
print(y_true)
print(len(y_true))
print(y_pred)
print(len(y_pred))
for i in range(len(y_true)):
  print(y_true[i],'  ', y_pred[i],' ', i)

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import numpy as np
import sklearn
from sklearn.metrics import confusion_matrix
import seaborn as sns
k = ['Swollen eye',  'Mouth ulcer',  'Skin dryness',  'Neck swelling',  
     'Skin irritation', 'Swollen tonsils', 
     'Knee swelling', 'Redness in ear', 
     'Dry scalp', 'Skin rash', 'Itchy eyelid', 'Hand lump', 
     'Skin growth', 'Eye redness', 'Foot swelling', 'Lip swelling',  'Eyelid rash']
score = accuracy_score(y_true, y_pred)
print('Classification Report: ',classification_report(y_true,y_pred))
cm = confusion_matrix(y_true, y_pred)
f,ax= plt.subplots(figsize=(15, 15))
sns.heatmap(cm, fmt='g', ax=ax);  #annot=True to annotate cells, ftm='g' to disable scientific notation

# labels, title and ticks
ax.set_xlabel('Predicted labels',fontsize = 28);ax.set_ylabel('True labels',fontsize = 28);
ax.set_title('Confusion Matrix');
classes_rev = []

classes = k
l = len(k)
for i in range(1,l+1):
    classes_rev = classes_rev + [classes[l-i]]
ax.xaxis.set_ticklabels(classes,fontsize = 5, );ax.yaxis.set_ticklabels(classes, fontsize = 5);
ax.figure.savefig("hybrid_cnn.png")
print('Accuracy: ', score)
print('F1',sklearn.metrics.f1_score(y_true, y_pred, average='weighted'))