from django.conf import settings
# import tensorflow as tf
# from tensorflow import keras
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2
# import shutil
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def predict_fn(path):
  base_dir = settings.MEDIA_ROOT_URL + settings.MEDIA_URL # == './media/'
  model_dir = base_dir + 'model_final.hdf5'
  model = models.load_model(model_dir, compile=False)

  img = cv2.imread(path)
  img=img*(1./255)
  img.resize(300,300,3)
  img=img.reshape(1,300,300,3)
  result = str(round(model.predict(img)[0][0]*100,2))+"% 확률로 적립금이 지급됩니다."

  return result
