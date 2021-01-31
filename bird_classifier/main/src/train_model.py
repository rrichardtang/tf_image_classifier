import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib

data_dir = pathlib.Path("/Users/rt1/projects/personal/machine_learning/bird_classifier/bird_dataset/"
                        "CUB_200_2011/CUB_200_2011/images")

batch_size = 32
img_height = 180
img_width = 180
