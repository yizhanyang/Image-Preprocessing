import os
import numpy as np
from tqdm import tqdm

def num_common_files(images, affordances):

    image_ids = np.array([img[:7] for img in images])
    affordance_ids = np.array([aff[:7] for aff in affordances])
    good_image_indices = image_ids == affordance_ids[:image_ids.shape[0]]

    bad_affordances = affordances[:image_ids.shape[0]][good_image_indices == False]

    false_affordances = np.concatenate([
        affordances[:image_ids.shape[0]][good_image_indices == False], affordances[image_ids.shape[0]:]
        ])

    false_affordance_ids = np.concatenate([
        affordance_ids[:image_ids.shape[0]][good_image_indices == False], affordance_ids[image_ids.shape[0]:]
        ])

    false_images_ids = image_ids[good_image_indices == False]

    correct_indices = false_affordance_ids == false_images_ids[0]

    for idx in tqdm(range(1, false_images_ids.shape[0])):
        new_correct_index = (false_affordance_ids == false_images_ids[idx])
        if new_correct_index.sum() == 0:
            import ipdb; ipdb.set_trace()

        correct_indices = correct_indices + new_correct_index

    bad_affordances = false_affordances[correct_indices == False]

    return bad_affordances

def get_files(path):
    return os.listdir(path).sort()

def get_paths(path, affordances):
    return [os.path.join(path, aff) for aff in affordances]

