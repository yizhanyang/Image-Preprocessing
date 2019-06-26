import os, sys, glob
from os import listdir
import numpy as np

NUM_SAMPLES = 200
PATH_TO_SAMPLES = '/opt/data/yizhan/rd10'
NEW_PATH = '/opt/data/yizhan/textures10'

RENDER_TYPES = ['images', 'depths', 'affordances']

def name_value(name):
    idx = name.find('_')
    return int(name[:idx])

def list_all_images(folder, render_type):
    path = os.path.join(PATH_TO_SAMPLES, folder, render_type)
    return listdir(path)

def sort_list(list_names):
    return sorted(list_names, key=lambda file_name: name_value(file_name))

FILE_LIMIT = '0000000'

def name_file(file_index):

    file_index = str(file_index)
    diff = len(FILE_LIMIT) -  len(file_index)
    return FILE_LIMIT[:diff] + file_index

from shutil import copyfile

def copy_file_with_new_path(old_path, new_path):
    copyfile(old_path, new_path)


list_images = list_all_images(PATH_TO_SAMPLES, RENDER_TYPES[0])
list_images = sort_list(list_images)

list_depths = list_all_images(PATH_TO_SAMPLES, RENDER_TYPES[1])
list_depths = sort_list(list_depths)

list_affordances = list_all_images(PATH_TO_SAMPLES, RENDER_TYPES[2])
list_affordances = sort_list(list_affordances)

new_images_path = os.path.join(NEW_PATH, RENDER_TYPES[0])
os.makedirs(new_images_path)
new_affordances_path = os.path.join(NEW_PATH, RENDER_TYPES[2])
os.makedirs(new_affordances_path)
new_depths_path = os.path.join(NEW_PATH, RENDER_TYPES[1])
os.makedirs(new_depths_path)

for idx in range(NUM_SAMPLES):

    image_old_path = os.path.join(PATH_TO_SAMPLES, RENDER_TYPES[0], list_images[-idx])
    image_new_path = os.path.join(new_images_path, list_images[-idx])
    copy_file_with_new_path(image_old_path, image_new_path)

    depth_old_path = os.path.join(PATH_TO_SAMPLES, RENDER_TYPES[1], list_depths[-idx])
    depth_new_path = os.path.join(new_depths_path, list_depths[-idx])
    copy_file_with_new_path(depth_old_path, depth_new_path)

    affordance_old_path = os.path.join(PATH_TO_SAMPLES, RENDER_TYPES[2], list_affordances[-idx])
    affordance_new_path = os.path.join(new_affordances_path, list_affordances[-idx])
    copy_file_with_new_path(affordance_old_path, affordance_new_path)

