## Dataset
提供一种方法去获取数据及其label
- 如何获取每个数据及其label
- 告诉我们总共有多少个数据
## Dataloader
为后面的网络提供不同的数据形式
## 获取图片
```
from PIL import Image
img_path = 'E:\\OneDrive\\pycharm\\dataset\\train\\ants\\0013035.jpg'
img = Image.open(img_path)
img.show()
```