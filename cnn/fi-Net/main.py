import tensorflow as tf
import numpy as np
import os
import tifffile as tiff
from tqdm import tqdm

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
np.random.seed(116)
np.random.shuffle(train_ids)
np.random.seed(116)
np.random.shuffle(train_y_ids)
np.random.seed(116)
np.random.shuffle(test_ids)
np.random.seed(116)
np.random.shuffle(test_y_ids)
tf.random.set_seed(116)

# 构造训练集和标签
X_train = np.zeros((len(train_ids)//2, IMG_HEIGHT, IMG_WIDTH, 2), dtype=np.double)
Y_train = np.zeros((len(train_y_ids)//2, IMG_HEIGHT, IMG_WIDTH, 2), dtype=np.double)

for n, file in tqdm(enumerate(train_ids), total=len(train_ids)):
    f = tiff.imread(TRAIN_PATH + file)
    if n % 2 == 1:
          X_train[n//2, :, :, 1] = f
    else:
          X_train[n//2, :, :, 0] = f

for n, file in tqdm(enumerate(train_y_ids), total=len(train_y_ids)):
    f = tiff.imread(TRAIN_PATH_Y + file)
    if n % 2 == 1:
        Y_train[n//2, :, :, 1] = f
    else:
        Y_train[n//2, :, :, 0] = f

# 构造测试集和标签
X_test = np.zeros((len(test_ids)//2, IMG_HEIGHT, IMG_WIDTH, 2), dtype=np.double)
Y_test = np.zeros((len(test_y_ids)//2, IMG_HEIGHT, IMG_WIDTH, 2), dtype=np.double)

for n, file in tqdm(enumerate(test_ids), total=len(test_ids)):
    f = tiff.imread(TEST_PATH + file)
    if n % 2 == 1:
        X_test[n // 2, :, :, 1] = f
    else:
        X_test[n // 2, :, :, 0] = f

for n, file in tqdm(enumerate(test_y_ids), total=len(test_y_ids)):
    f = tiff.imread(TEST_PATH_Y + file)
    if n % 2 == 1:
        Y_test[n // 2, :, :, 1] = f
    else:
        Y_test[n // 2, :, :, 0] = f


def RB(input, filters): 
    c_1 = tf.keras.layers.Conv2D(filters=filters, kernel_size=1, padding='same', strides=1)(input)
    c_2 = tf.keras.layers.Conv2D(filters=filters, kernel_size=3, padding='same', strides=1)(c_1)
    b_1 = tf.keras.layers.BatchNormalization()(c_2)
    r_1 = tf.keras.layers.ReLU()(b_1)
    c_3 = tf.keras.layers.Conv2D(filters=filters, kernel_size=3, padding='same', strides=1)(r_1)
    b_2 = tf.keras.layers.BatchNormalization()(c_3)
    r_2 = tf.keras.layers.ReLU()(c_1+b_2)
    return r_2


def MP_RB(input, filters):
    p = tf.keras.layers.MaxPool2D((2,2))(input)
    return RB(p, filters)

def RB_UP(input, filters, tran_filters):
    rb = RB(input, filters)
    up = tf.keras.layers.Conv2DTranspose(filters=tran_filters, kernel_size=2, strides=2, padding='same')(rb)
    return up



def fi_net(input_shape):
    inputs = tf.keras.layers.Input((IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS))
    rb = RB(inputs, 64)
    mp_rb_1 = MP_RB(rb, 128)
    mp_rb_2 = MP_RB(mp_rb_1, 256)
    mp_rb_3 = MP_RB(mp_rb_2, 512)

    rb_up_1 = RB_UP(mp_rb_3, 256, 256)
    co_1 = tf.concat([rb_up_1, mp_rb_2], axis=3)
    rb_up_2 = RB_UP(co_1, 128, 128)
    co_2 = tf.concat([rb_up_2, mp_rb_1], axis=3)
    rb_up_3 = RB_UP(co_2, 64, 64)
    co_3 = tf.concat([rb_up_3, rb], axis=3)
    c_1 = tf.keras.layers.Conv2D(filters=2, kernel_size=1, padding='same', strides=1)(co_3)
    outputs = inputs - c_1
    return tf.keras.Model(inputs = [inputs], outputs = [outputs])

model = fi_net(input_shape=(IMG_WIDTH, IMG_HEIGHT, IMG_CHANNELS))
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001, decay=1e-6), loss=tf.keras.losses.MeanSquaredError(), metrics=['accuracy'])

checkpoint_save_path = "E:\\OneDrive\\vscode\\fi-Net\\checkpoint\\fi_Net.ckpt"
if os.path.exists(checkpoint_save_path + '.index'):
    print('-------------load the model-----------------')
    model.load_weights(checkpoint_save_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_save_path,
                                                 save_weights_only=True,
                                                 save_best_only=True)

results = model.fit(X_train, Y_train, batch_size=2, epochs=50, validation_data=(X_test, Y_test), validation_freq=1, callbacks=[cp_callback])
model.summary()