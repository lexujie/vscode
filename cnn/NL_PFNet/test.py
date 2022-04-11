import torch.nn as nn
import torch
y = nn.ConvTranspose2d(64, 64, kernel_size=3, stride=2,padding=1,output_padding=1)
x = torch.randn([1, 64, 128, 128])

y1 = y(x)
print(y1.shape)

a = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(a)