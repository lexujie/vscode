import math
import tensorflow as tf
from osgeo import gdal
import numpy as np
import tifffile as tiff



IMG_WIDTH = 1024
IMG_HEIGHT = 1024
IMG_CHANNELS = 2

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


checkpoint_path = "E:\\OneDrive\\vscode\\fi-Net\\checkpoint\\fi_Net.ckpt"
model = fi_net(input_shape=(IMG_WIDTH, IMG_HEIGHT, IMG_CHANNELS))
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001, decay=1e-4), loss=tf.keras.losses.MeanSquaredError(), metrics=['accuracy'])
model.load_weights(checkpoint_path)


data = tiff.imread('C:\\Users\\HP\\Desktop\\新建文件夹\\check\\re_2.tif')

data1 = tiff.imread('C:\\Users\\HP\\Desktop\\新建文件夹\\check\\im_2.tif')

test_images = np.zeros((1, IMG_WIDTH, IMG_HEIGHT, IMG_CHANNELS), dtype=np.double)
test_images[:, :, :, 0] = data
test_images[:, :, :, 1] = data1

result = model.predict(test_images)
re = result[:, :, :, 0]
im = result[:, :, :, 1]
re = re.reshape(IMG_WIDTH, IMG_HEIGHT)
im = im.reshape(IMG_WIDTH, IMG_HEIGHT)
ture = np.zeros((IMG_WIDTH, IMG_HEIGHT), dtype=np.double)
for i in range(IMG_WIDTH):
    for j in range(IMG_HEIGHT):
        if im[i, j] > 0 and re[i, j] < 0:
            ture[i, j] = tf.atan(im[i, j]/re[i, j]) + math.pi
        elif im[i, j] < 0 and re[i, j] < 0:
            ture[i, j] = tf.atan(im[i, j] / re[i, j]) - math.pi
        else:
            ture[i, j] = tf.atan(im[i, j] / re[i, j])

tiff.imsave('E:\\OneDrive\\AI\\image_label\\check\\fi_2.tif', ture)