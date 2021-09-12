import numpy as np
import h5py
import imageio
import cv2

hf = h5py.File('data_test.h5', 'r')

for key in hf.keys():
    print(key)



# dset = hf['train_set_x']              # for train data
dset = hf['test_set_x']                 # for test data
data = np.array(dset[:,:,:])




for i in range(data.shape[0]):
    file = "test"+str(i)+".jpg"
    imageio.imwrite(file, data[i])
    