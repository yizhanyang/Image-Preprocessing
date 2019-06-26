import os, sys, glob
from os import listdir
import numpy as np

PATH_TO_SAMPLES = '/opt/data/yizhan/rd10'
NEW_PATH = '/opt/data/yizhan/textures10'
NEW_LOG = 'logger.csv'
RENDER_TYPE = ['images', 'depths', 'affordances']


def list_all_sample_folders():
    arr = listdir(PATH_TO_SAMPLES)
    #arr.remove('..-')
    return arr

def list_image_types(folder):
    return listdir(os.path.join(PATH_TO_SAMPLES, folder))

def list_all_images(folder, render_type):
    path = os.path.join(PATH_TO_SAMPLES, folder, render_type)
    return listdir(path)

def name_value(name):
    idx = name.find('_')
    return int(name[:idx])


def sort_list(list_names):
    return sorted(list_names, key=lambda file_name: name_value(file_name))

FILE_LIMIT = '0000000'

def name_file(file_index):

    file_index = str(file_index)
    diff = len(FILE_LIMIT) -  len(file_index)
    return FILE_LIMIT[:diff] + file_index

def correct_number_of_files(list_images, list_depths, list_affordances):
    max_values = [len(list_images), len(list_depths), len(list_affordances)]
    min_value = min(max_values)
    return min_value


from shutil import copyfile

def copy_file_with_new_path(old_path, new_path):
    copyfile(old_path, new_path)


def main(copy_files):

    list_folders = list_all_sample_folders()
    # list_folders = sort_list(list_folders)

    file_index = 0
    num_files_in_each_folder = []


    for folder_name in list_folders:
        print(folder_name)

        list_images = list_all_images(folder_name, RENDER_TYPE[0])
        list_images = sort_list(list_images)

        list_depths = list_all_images(folder_name, RENDER_TYPE[1])
        list_depths = sort_list(list_depths)

        list_affordances = list_all_images(folder_name, RENDER_TYPE[2])
        list_affordances = sort_list(list_affordances)


        nums =  [len(list_images), len(list_depths), len(list_affordances)]

#        if min(nums) != max(nums):
#            print('fail')
#            print(list_images[-1], list_depths[-1], list_affordances[-1])

        # ensure lists are equal size
        min_value = correct_number_of_files(list_images, list_depths, list_affordances)

        list_images = list_images[:min_value]
        list_depths = list_depths[:min_value]
        list_affordances = list_affordances[:min_value]



        num_files_in_each_folder.append(min_value)

        if (copy_files):

            for idx in range(len(list_images)):

                file_index += 1

                file_id = name_file(file_index)
                print(file_id)

                image_name = name_file(file_index) + '_image.png'
                image_new_path = os.path.join(NEW_PATH, 'images', image_name)
                image_old_path = os.path.join(PATH_TO_SAMPLES, folder_name, RENDER_TYPE[0], list_images[idx])
                print('image_new_path')
                copy_file_with_new_path(image_old_path, image_new_path)

                depth_name = name_file(file_index) + '_depth.png'
                depth_new_path = os.path.join(NEW_PATH, 'depths', depth_name)
                depth_old_path = os.path.join(PATH_TO_SAMPLES, folder_name, RENDER_TYPE[1], list_depths[idx])
                print('depth_new_path')
                copy_file_with_new_path(depth_old_path, depth_new_path)

                affordance_name = name_file(file_index) + '_affordance.png'
                affordance_new_path = os.path.join(NEW_PATH, 'affordances', affordance_name)
                affordance_old_path = os.path.join(PATH_TO_SAMPLES, folder_name, RENDER_TYPE[2], list_affordances[idx])

                print('affordance_new_path')
                copy_file_with_new_path(affordance_old_path, affordance_new_path)

#    new_log = open(os.path.join(NEW_PATH, NEW_LOG), 'a')
#    # first file
#    f = open(os.path.join(PATH_TO_SAMPLES, list_folders[0], 'logger.csv'))
#    new_log.write(f.readline()) # header
#
#    for idx in range(num_files_in_each_folder[0]):
#        new_log.write(f.readline())
#
#    f.close()
#
#    # rest of the files
#    for folder_idx in range(1, len(num_files_in_each_folder)):
#
#        folder_name = list_folders[folder_idx]
#
#        f = open(os.path.join(PATH_TO_SAMPLES, folder_name, 'logger.csv'))
#        f.readline() # skip the header
#        #import ipdb; ipdb.set_trace()
#
#        for idx in range(num_files_in_each_folder[folder_idx]):
#            new_log.write(f.readline())
#
#        f.close()
#
#    new_log.close()

if __name__ == '__main__':

    main(True)
