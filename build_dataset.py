import random
import os
from shutil import copy


def build_dataset():
    """
    Split original dataset into train and test sets.
    """

    for subdir, dirs, files in os.walk('./data'):
        file_paths = []
        folder_name = os.path.basename(subdir)

        for file in files:
            file_paths.append(os.path.join(subdir, file))

        if len(file_paths) > 0:
            file_paths.sort()  # make sure that the file_paths have a fixed order before shuffling
            random.seed(230)
            random.shuffle(file_paths)

            boundary = int(0.8 * len(file_paths))
            train = file_paths[:boundary]
            test = file_paths[boundary:]

            # create folders
            if not os.path.exists(os.path.join('./train', folder_name)):
                os.makedirs(os.path.join('./train', folder_name))

            if not os.path.exists(os.path.join('./test', folder_name)):
                os.makedirs(os.path.join('./test', folder_name))

            # copy images in created folders
            for path in train:
                copy(path, os.path.join('./train', folder_name))

            for path in test:
                copy(path, os.path.join('./test', folder_name))

    print("Done building dataset")
