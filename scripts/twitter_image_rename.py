#-*- coding: utf-8 -*-
"""
Author: Chaoqun
Time: 2018-04-17

根据字典中所记录的文件原后缀名和新后缀名的对应，
批量修改指定文件夹下的所有图片的后缀名
也可以通过修改字典来将批量修改的文件名应用于其他场景

"""

import sys
import os
import time
import operator
import argparse

FLAGS = None

# 用来记录文件后缀名修改的字典
FILE_SUFFIX_DICT = {'jpg_large':'jpg', 'png_large':'png'}

def rename(floder_name):
    """ rename function 递归函数
    思路：将本文件夹内的符合要求的文件名先全部改掉
        如果递归属性是打开的，则深入之后的每个文件夹。
    """
    current_dir = os.getcwd()    # 记录当前文件夹
    if not os.path.exists(floder_name):
        print("Floder {0} seems to be not existed.".format(floder_name))
        return
    os.chdir(floder_name)       # 切入工作路径到新的文件夹
    #-------------------------------------------------------------------------#
    for image_file in os.listdir('./') :
        # 遍历文件
        if os.path.isfile(image_file) :
            for file_suffix in FILE_SUFFIX_DICT.keys() :
                if image_file.count(file_suffix) >= 1 :
                    index = image_file.rfind(file_suffix)
                    image_new_file = \
                        image_file[0:index] + FILE_SUFFIX_DICT[file_suffix]
                    os.rename(image_file, image_new_file)

                    print("Rename file {0} to {1}".format(
                        os.path.join(current_dir, image_file), image_new_file))
        elif FLAGS.recursive :
            if os.path.isdir(image_file) :
                rename(image_file)
    #-------------------------------------------------------------------------#
    os.chdir(current_dir)
    pass

def main():
    """ main function
    """
    start_time = time.time()
    rename(FLAGS.path)
    print("Rename finised! Cost {0} Sec.".format(
        time.time() - start_time))
    pass

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
        "-r",
        "--recursive",
        dest = "recursive",
        default = False,
        action = "store_true",
        help = "if you want the script worked on your subDirs")

    FLAGS, unparsed = parser.parse_known_args()

    print( FLAGS )      # print the arguments
    main()
