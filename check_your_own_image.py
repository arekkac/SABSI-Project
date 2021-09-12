import math
import numpy as np
import h5py
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.python.framework import ops
from tf_utils import load_dataset, random_mini_batches, convert_to_one_hot, predict
import cv2
from matplotlib.pyplot import imshow
import scipy
from PIL import Image
from scipy import ndimage
import imageio
import scipy.misc


np.random.seed(1)



hf = h5py.File('parameters.h5', 'r')

parameters = dict()

dset = hf['W1']
parameters["W1"] = np.array(dset[:,:])

dset = hf['W2']
parameters["W2"] = np.array(dset[:,:])

dset = hf['W3']
parameters["W3"] = np.array(dset[:,:])

dset = hf['b1']
parameters["b1"] = np.array(dset[:,:])

dset = hf['b2']
parameters["b2"] = np.array(dset[:,:])

dset = hf['b3']
parameters["b3"] = np.array(dset[:,:])



def switch(x):
        if x == 0:
            return "1 grosz"
        if x == 1:
            return "2 grosze"
        if x == 2:
            return "5 groszy"
        if x == 3:
            return "10 groszy"
        if x == 4:
            return "20 groszy"
        if x == 5:
            return "50 groszy"
        if x == 6:
            return "1 zloty"
        if x == 7:
            return "2 zlote"
        if x == 8:
            return "5 zlotych"
        if x == 9:
            return "Inne"

        return "Inne"




img_path = 'my_image.jpg'                                  #put here name of your picture
my_image = cv2.imread(img_path)
my_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
size = (64,64)
my_image = cv2.resize(my_image,size)
image = my_image.reshape(1,64*64*3).T
image = image/255.
my_image_prediction = predict(image, parameters)
plt.imshow(my_image)
find = switch(np.squeeze(my_image_prediction))
print("Your algorithm predicts: y = ",find)

