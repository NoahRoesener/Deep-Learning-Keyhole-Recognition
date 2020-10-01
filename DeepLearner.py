# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:46:32 2020

@author: Student
"""

import tensorflow as tf
import numpy as np
import matplotlib as plt
import os


directory = 'F:\Matlab_KI\Data\keyhole\IGP-H-III-6-3'
subdir = os.listdir(directory)

pos_folder = directory + '\\' + subdir[1] + '\\' + 'frames'
neg_folder = directory + '\\' + subdir[0] + '\\' + 'frames'

pos_label = np.ones(len(os.listdir(pos_folder)))
neg_label = np.zeros(len(os.listdir(neg_folder)))

neg_files = neg_folder + '*.jpg'
pos_files = pos_folder + '*.jpg'

f_pos = dir(pos_files)
f_neg = dir(neg_files)

files_pos = {f_pos.name}

# for k in len(files_pos):
#     fullFileName_pos = fullfile(folder, files_pos{k})
#     cellImgPos{k} = imread(fullFileName_pos)
# end
    

