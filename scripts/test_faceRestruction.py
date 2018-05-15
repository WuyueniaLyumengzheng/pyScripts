#-*- coding: utf-8 -*-
"""
Author: Chaoqun
Time: 2018-05-15

"""

import sys
import os
import time
import operator
import argparse

FLAGS = None

def faceRec( filename, outputPath ):
    log = os.popen("cfaceRec -i {0} -s {1}".format(filename, outputPath), 'r', 1)

def main():
    """ main function
    """
    current_dir = os.getcwd()       # 记录当前文件

    if not os.path.exists(FLAGS.path):
        print("Floder {0} seems to be not existed.".format(FLAGS.path))
        return
    if not os.path.exists(FLAGS.outputPath):
        os.mkdir(FLAGS.outputPath)
    os.chdir(FLAGS.outputPath)
    output_dir = os.getcwd()         # 记录当前文件夹
    os.chdir(current_dir)
    os.chdir(FLAGS.path)             # 切换到输入文件夹
    path_dir=os.getcwd()

    print("path:{0}, outpath:{1}".format(path_dir, output_dir))

    dirs = os.listdir('./')         # 先建立队列，防止保存路径与图片路径是统一路径

    count_image = 0
    start_time = time.time()
    for image_file in dirs:
        # 遍历文件
        if os.path.isfile(dirs):
            faceRec(os.path.join(current_dir, image_file), output_dir)
            count_image += 1
    print("Cost time {0} Sec, process {1} images.".format(
        time.time() - start_time, count_image))
    os.chdir(current_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        dest = "path",
        default = "./",
        type = str,
        help ="the floder you want your scripts worked!" )

    parser.add_argument(
        "-o",
        "--outputPath",
        dest = "outputPath",
        default = "./",
        type = str,
        help ="the floder to output the model" )

    FLAGS, unparsed = parser.parse_known_args()

    print( FLAGS )      # print the arguments
    main()
