import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

import os


def loadModel():
    new_model = models.load_model('model3.h5')
    new_model.summary()
    return new_model

def showGrayImage(image):
    plt.figure(1)
    plt.imshow(image[:,:,0], cmap='gray')
    plt.show()

def openImage(url):
    img_raw = tf.io.read_file(url)

    img = tf.image.decode_image(img_raw)
    img = tf.image.resize(img, [28,28])
    img = tf.image.rgb_to_grayscale(img)
    img = img.numpy()

    return img

def predict(model, image):
    img_pre = image.reshape(-1, 28, 28, 1) / 255.0
    img_pre.shape

    pre = model.predict(img_pre)
    return pre

def plot_pre(pre):
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), pre, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(pre)
    thisplot[predicted_label].set_color('blue')
    for i in range(10):
        plt.text(i, pre[i], '%.1f %%' % (pre[i]*100), ha='center', va='bottom')

    plt.figure(1)
    plt.show()

def start(url):
    img = openImage(url)
    showGrayImage(img)
    
    model = loadModel()
    res = predict(model, img)
    plot_pre(res[0])

    print(res)
    print(np.argmax(res))

if __name__ == "__main__":
    start('number_test/2(1).jpg')