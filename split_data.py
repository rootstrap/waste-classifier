import math
import os
import random


# DIR is the name of the directory with the data to separate, it has to be in the same directory as this file.
# TEST and VAL are the percentages of the total number of files that are going to be used
# as Test data and Validation data respectively.
TEST = 10
VAL = 10
DIR = 'dataset-resized'


class Splitter(object):
    def __init__(self, test, val, directory):
        self.test = test
        self.val = val
        self.route = f'{os.getenv("PWD")}/{directory}'
        self.subdirs = []

    # Three folders will be created inside DIR: 'test' 'val' and 'training'
    # There must not be a test folder neither a val folder in DIR, otherwise an exception will be raised
    def create_dirs(self):
        content = os.listdir(self.route)
        self.subdirs = [elem for elem in content if os.path.isdir(f'{self.route}/{elem}')]
        os.mkdir(f'{self.route}/test')
        os.mkdir(f'{self.route}/val')
        os.mkdir(f'{self.route}/training')
        for subdir in self.subdirs:
            os.mkdir(f'{self.route}/test/{subdir}')
            os.mkdir(f'{self.route}/val/{subdir}')
            os.mkdir(f'{self.route}/training/{subdir}')

    def get_percentage(self, per, num):
        return math.floor(per*num/100)

    # After this method is executed only 3 folders should remain inside DIR
    # and all the files separated according to the percentages defined in the TEST and VAL constants
    def split(self):
        for subdir in self.subdirs:
            file_list = os.listdir(f'{self.route}/{subdir}')
            num_files = len(file_list)
            test = self.get_percentage(self.test, num_files)
            val = self.get_percentage(self.val, num_files)
            to_test = [file_list.pop(random.randrange(len(file_list))) for _ in range(test)]
            for f in to_test:
                os.rename(
                    f'{self.route}/{subdir}/{f}',
                    f'{self.route}/test/{subdir}/{f}'
                )
            to_val = [file_list.pop(random.randrange(len(file_list))) for _ in range(val)]
            for f in to_val:
                os.rename(
                    f'{self.route}/{subdir}/{f}',
                    f'{self.route}/val/{subdir}/{f}'
                )
            for f in file_list:
                os.rename(
                    f'{self.route}/{subdir}/{f}',
                    f'{self.route}/training/{subdir}/{f}'
                )
            os.rmdir(f'{self.route}/{subdir}')


def split_data(test=TEST, val=VAL, directory=DIR):
    split = Splitter(test, val, directory)
    split.create_dirs()
    split.split()
