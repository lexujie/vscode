
import torch.nn as nn
from torch.nn import functional as F
import numpy as np
import os
import tifffile as tiff
from tqdm import tqdm
import n3net
import torch
import torch.utils.data as Data


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# 图片长、宽和通道数
IMG_WIDTH = 256
IMG_HEIGHT = 256
IMG_CHANNELS = 2


# 训练集、测试集和相应的标签的位置
TRAIN_PATH = 'E:\\OneDrive\\AI\\image_label\\train_1\\'
TEST_PATH = 'E:\\OneDrive\\AI\\image_label\\test_1\\'
TRAIN_PATH_Y = 'E:\\OneDrive\\AI\\image_label\\train_real_1\\'
TEST_PATH_Y = 'E:\\OneDrive\\AI\\image_label\\test_real_1\\'

# 读取训练集、测试集和相应的标签
train_ids = os.listdir(TRAIN_PATH)
test_ids = os.listdir(TEST_PATH)
train_y_ids = os.listdir(TRAIN_PATH_Y)
test_y_ids = os.listdir(TEST_PATH_Y)

# 对训练集、测试集和相应的标签打乱顺序（用相同的随机种子）
# np.random.seed(116)
# np.random.shuffle(train_ids)
# np.random.seed(116)
# np.random.shuffle(train_y_ids)
# np.random.seed(116)
# np.random.shuffle(test_ids)
# np.random.seed(116)
# np.random.shuffle(test_y_ids)


# 构造训练集和标签
X_train = np.zeros((len(train_ids)//2, 2, IMG_HEIGHT, IMG_WIDTH), dtype=np.float32)
Y_train = np.zeros((len(train_y_ids)//2, 2, IMG_HEIGHT, IMG_WIDTH), dtype=np.float32)

for n, file in tqdm(enumerate(train_ids), total=len(train_ids)):
    f = tiff.imread(TRAIN_PATH + file)
    if n % 2 == 1:
          X_train[n//2, 1, :, :] = f
    else:
          X_train[n//2, 0, :, :] = f

for n, file in tqdm(enumerate(train_y_ids), total=len(train_y_ids)):
    f = tiff.imread(TRAIN_PATH_Y + file)
    if n % 2 == 1:
        Y_train[n//2, 1, :, :] = f
    else:
        Y_train[n//2, 0, :, :] = f

# 构造测试集和标签
X_test = np.zeros((len(test_ids)//2, 2, IMG_HEIGHT, IMG_WIDTH), dtype=np.float32)
Y_test = np.zeros((len(test_y_ids)//2, 2, IMG_HEIGHT, IMG_WIDTH), dtype=np.float32)

for n, file in tqdm(enumerate(test_ids), total=len(test_ids)):
    f = tiff.imread(TEST_PATH + file)
    if n % 2 == 1:
        X_test[n // 2, 1, :, :] = f
    else:
        X_test[n // 2, 0, :, :] = f

for n, file in tqdm(enumerate(test_y_ids), total=len(test_y_ids)):
    f = tiff.imread(TEST_PATH_Y + file)
    if n % 2 == 1:
        Y_test[n // 2, 1, :, :] = f
    else:
        Y_test[n // 2, 0, :, :] = f

X_train = torch.from_numpy(X_train)
Y_train = torch.from_numpy(Y_train)
X_test = torch.from_numpy(X_test)
Y_test = torch.from_numpy(Y_test)

X_train = X_train.to(device)
Y_train = Y_train.to(device)
X_test = X_test.to(device)
Y_test = Y_test.to(device)
torch.manual_seed(116)
torch_dataset = Data.TensorDataset(X_train, Y_train)
loader = Data.DataLoader(dataset=torch_dataset, batch_size=2, shuffle=True)

torch_testset = Data.TensorDataset(X_test, Y_test)
testloader = Data.DataLoader(dataset=torch_testset, batch_size=2, shuffle=True)






class NL_PFNet(nn.Module):
    def __init__(self):
        super(NL_PFNet, self).__init__()
        self.en1_c1 = nn.Conv2d(2, 64, kernel_size=3, stride=1, padding=1)
        self.en1_c2 = nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1)
        self.en1_c3 = nn.Conv2d(64, 64, kernel_size=3, stride=2, padding=1)
        self.bn1 = nn.BatchNorm2d(64)

        self.en2_c1 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.en2_c2 = nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1)
        self.en2_c3 = nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(128)

        self.en3_c1 = nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1)
        self.en3_c2 = nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1)
        self.en3_c3 = nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1)
        self.bn3 = nn.BatchNorm2d(256)

        self.en4_c1 = nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1)
        self.en4_c2 = nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1)
        self.en4_c3 = nn.Conv2d(256, 64, kernel_size=3, stride=1, padding=1)

        self.de1_c1 = nn.Conv2d(64, 256, kernel_size=3, stride=1, padding=1)
        self.de1_c2 = nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1)
        self.de1_c3 = nn.Conv2d(512, 256, kernel_size=3, stride=1, padding=1)

        self.de2_c1 = nn.Conv2d(256, 128, kernel_size=3, stride=1, padding=1)
        self.de2_c2 = nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1)
        self.de2_c3 = nn.Conv2d(256, 128, kernel_size=3, stride=1, padding=1)

        self.de3_c1 = nn.Conv2d(128, 64, kernel_size=3, stride=1, padding=1)
        self.de3_c2 = nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1)
        self.de3_c3 = nn.Conv2d(128, 64, kernel_size=3, stride=1, padding=1)

        self.de4_c1 = nn.Conv2d(64, 8, kernel_size=3, stride=1, padding=1)
        self.de4_c2 = nn.Conv2d(8, 8, kernel_size=3, stride=1, padding=1)
        self.de4_c3 = nn.Conv2d(8, 2, kernel_size=3, stride=1, padding=1)
        self.bn4 = nn.BatchNorm2d(8)
        self.up = nn.ConvTranspose2d(64, 64, kernel_size=3, stride=2, padding=1,output_padding=1)
    
    
    def forward(self, x):
        x1 = F.relu(self.en1_c1(x))
        x2 = F.relu(self.bn1(self.en1_c2(x1)))
        x3 = F.relu(self.bn1(self.en1_c3(x2)))

        x4 = F.relu(self.bn2(self.en2_c1(x3)))
        x5 = F.relu(self.bn2(self.en2_c2(x4)))
        x6 = F.relu(self.bn2(self.en2_c3(x5)))

        x7 = F.relu(self.bn3(self.en3_c1(x6)))
        x8 = F.relu(self.bn3(self.en3_c2(x7)))
        x9 = F.relu(self.bn3(self.en3_c3(x8)))

        x10 = F.relu(self.bn3(self.en4_c1(x9)))
        x11 = F.relu(self.bn3(self.en4_c2(x10)))
        x12 = self.en4_c3(x11)

        # x13 = n3net.N3Block(8, 7)
        # y = x13(x12)

        y1 = F.relu(self.de1_c1(x12))
        y2 = F.relu(self.bn3(self.de1_c2(y1)))
        y2_1 = torch.cat((y2, x9), 1)
        y3 = F.relu(self.bn3(self.de1_c3(y2_1)))

        y4 = F.relu(self.bn2(self.de2_c1(y3)))
        y5 = F.relu(self.bn2(self.de2_c2(y4)))
        y5_1 = torch.cat((y5, x6), 1)
        y6 = F.relu(self.bn2(self.de2_c3(y5_1)))

        y7 = F.relu(self.bn1(self.de3_c1(y6)))
        y8 = F.relu(self.bn1(self.de3_c2(y7)))
        y8_1 = torch.cat((y8, x3), 1)
        y9 = F.relu(self.bn1(self.de3_c3(y8_1)))

        y11 = self.up(y9)
        y12 = F.relu(self.bn4(self.de4_c1(y11)))
        y13 = F.relu(self.bn4(self.de4_c2(y12)))
        y14 = self.de4_c3(y13)
        return y14




model = NL_PFNet()
loss = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(),lr=1e-3)


def evaluate_accuracy(data_iter, net):
  acc_sum, n = 0.0, 0
  for x, y in data_iter:
    
    
    acc_sum += (net(x).argmax(dim=1) == y).float().sum().item()
    n += y.shape[0]
  return acc_sum / n


num_epochs = 50
model=model.to(device) # 移动模型到cuda

# 训练模型


for epoch in range(num_epochs):
    train_l_sum, train_acc_sum, n = 0.0, 0.0, 0
    for i, (x, y) in tqdm(enumerate(loader),total=len(loader)):
       
      y_hat = model(x)
      l = loss(y_hat, y)  
      _, pred = torch.max(y_hat,axis=1)
      cur_acc = torch.sum(y==pred)/y_hat.shape[0]

      optimizer.zero_grad()          
      l.backward()      
      optimizer.step()      
      train_l_sum += l.item()
      train_acc_sum += cur_acc.item()
      n = n+1
      if i % 225 ==0:
        print('epoch %d, loss %.4f, train acc %.3f'% (epoch + 1, train_l_sum / n, train_acc_sum/n ))



