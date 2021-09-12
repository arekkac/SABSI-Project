import numpy as np
import h5py
import imageio
import cv2
import os



indexes = list()

images = list()

folder = '11'
for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if img is not None:
            size = (64,64)
            img_res = cv2.resize(img,size)
            images.append(img_res)
            indexes.append(0)

folder = '22'
for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if img is not None:
            size = (64,64)
            img_res = cv2.resize(img,size)
            images.append(img_res)
            indexes.append(1)

folder = '55'
for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if img is not None:
            size = (64,64)
            img_res = cv2.resize(img,size)
            images.append(img_res)
            indexes.append(2)

folder = '10'
for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if img is not None:
            size = (64,64)
            img_res = cv2.resize(img,size)
            images.append(img_res)
            indexes.append(3)

folder = '20'
for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if img is not None:
            size = (64,64)
            img_res = cv2.resize(img,size)
            images.append(img_res)
            indexes.append(4)

folder = '50'
for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if img is not None:
            size = (64,64)
            img_res = cv2.resize(img,size)
            images.append(img_res)
            indexes.append(5)

folder = '1'
for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if img is not None:
            size = (64,64)
            img_res = cv2.resize(img,size)
            images.append(img_res)
            indexes.append(6)

            

folder = '2'
for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if img is not None:
            size = (64,64)
            img_res = cv2.resize(img,size)
            images.append(img_res)
            indexes.append(7)

    
folder = '5'
for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if img is not None:
            size = (64,64)
            img_res = cv2.resize(img,size)
            images.append(img_res)
            indexes.append(8)


folder = 'other'
for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if img is not None:
            size = (64,64)
            img_res = cv2.resize(img,size)
            images.append(img_res)
            indexes.append(9)



hf = h5py.File('data_test.h5', 'w')


hf.create_dataset('test_set_x', data=images)
hf.create_dataset('test_set_y', data=indexes)

hf.close()


