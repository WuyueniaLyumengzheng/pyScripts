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
cfaceRecPath = "/mnt/e/Qt_projects/linux_FaceReconstruction_Release/bin"

def faceRec( filename, outputPath ):
    current_dir = os.getcwd()       # 记录当前文件
    os.chdir(cfaceRecPath)
    cfaceRec = os.path.join(cfaceRecPath, "cfaceRec")
    command = "{0} -i {1} -s {2}".format(cfaceRec, filename, outputPath)
    print(command)
    #log = os.popen(command, 'r', 1)
    os.system(command)
    os.chdir(current_dir)

def main():
    """ main function
    """
    current_dir = os.getcwd()       # 记录当前文件

    if not os.path.exists(FLAGS.path):
        print("Floder {0} seems to be not existed.".format(FLAGS.path))
        return
    if not os.path.exists(FLAGS.outputPath):
        os.mkdir(FLAGS.outputPath)
    # os.chdir(FLAGS.outputPath)
    # output_dir = os.getcwd()         # 记录当前文件夹
    # os.chdir(current_dir)
    # os.chdir(FLAGS.path)             # 切换到输入文件夹
    # path_dir=os.getcwd()
    output_dir = os.path.abspath(FLAGS.outputPath)
    path_dir = os.path.abspath(FLAGS.path)

    print("path:{0}, outpath:{1}".format(path_dir, output_dir))

    dirs = os.listdir(path_dir)         # 先建立队列，防止保存路径与图片路径是统一路径
    #os.chdir(current_dir)

    count_image = 0
    start_time = time.time()
    for image_file in dirs:
        # 遍历文件
        if os.path.isfile(os.path.join(path_dir, image_file)):
            faceRec(os.path.join(path_dir, image_file), output_dir)
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
