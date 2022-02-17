```
from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
# python的用法 -》tensor数据类型
# 通过transforms.ToTensor解决两个问题
# 1、transform该如何使用
# 2、为什么需要Tensor数据类型

img_path = 'data/train/ants_image/0013035.jpg'
img = Image.open(img_path)

writer = SummaryWriter('logs')

tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)

writer.add_image('Tensor_img', tensor_img)
writer.close()
```

## 图片类型
- PIL：Image.open()
- tensor: ToTensor()
- narrays: cv.imread()