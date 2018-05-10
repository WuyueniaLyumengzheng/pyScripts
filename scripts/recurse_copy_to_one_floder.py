"""
Author: Chaoqun
Time: 2018-05-10

本脚本用于将某文件夹路径下的所有文件全部递归的拷贝到指定文件夹下（不拷贝文件夹，
不处理文件名重复问题，文件名重复直接覆盖）

原因，因为想使用 LFW 数据集，结果他们的数据集按人将文件分成了好多文件夹， 不便于我使用。
"""


import argparse
import os
import shutil
import sys
import time
import operator

FLAGS = None

def main():
    """function main
    """
    print("Copy files from {0} to {1}.".format(FLAGS.source, FLAGS.outputPath))

    # judge if need to create outputPath floder
    if not os.path.exists(FLAGS.outputPath):
        os.mkdir(FLAGS.outputPath)
    FLAGS.outputPath = os.path.abspath(FLAGS.outputPath)    # get absoulte path
    start_time = time.time()
    file_count = 0

    recurse_copy(FLAGS.source, file_count)

    end_time = time.time()
    print("Process finished！ cost {0} sec. Copy {1} files".format(
        end_time-start_time, file_count))

def recurse_copy( path, file_count ):
    """
        递归函数，
        思路：将本文件夹内的文件拷贝出去，然后在深入每一个文件夹。
    """
    current_dir = os.getcwd()       # 记录当前文件夹路径

    if not os.path.exists(path):
        print("Floder {0} seems to be not existed.".format(path))
        return
    os.chdir(path)       # 切入工作路径到新的文件夹

    #-------------------------------------------------------------------------#
    for image_file in os.listdir('./') :
        # 遍历文件
        if os.path.isfile(image_file) :
            shutil.copy2( image_file, FLAGS.outputPath)
            file_count += 1;
        elif os.path.isdir(image_file) :
                recurse_copy(image_file, file_count)
    os.chdir(current_dir)           # 返回当前文件夹路径


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s',
        '--source',
        dest='source',
        type = str,
        default = "./",
        help = 'The floder you want to copy from!')

    parser.add_argument(
        "-o",
        "--outputPath",
        dest = "outputPath",
        default = "../output",
        type = str,
        help ="the floder we want to save the files!" )

    FLAGS, unparsed = parser.parse_known_args()

    print( FLAGS )      # print the arguments
    main()
