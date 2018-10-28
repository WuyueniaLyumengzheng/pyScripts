#-*- coding: utf-8 -*-
"""
Author: Chaoqun
Time: 2018-05-15

处理思路：
    打开指定路径下的所有的单次病患扫描的csv结果，计算出该次扫描的平均血流情况，
    将数值储存在新的统计CSV文件中。

"""

import sys
import os
import time
import csv
import operator
import argparse

FLAGS = None
csv_files = []          # a list of absolute file path of *.csv file

def main():
    """ main function
    """
    current_dir = os.getcwd()       # record current direction.
    path_dir = os.path.abspath(FLAGS.path)
    save_flie_path = os.path.abspath(FLAGS.save_file_path)
    print("path Dir: {0}".format(path_dir))
    print("Save file path: {0}".format(save_flie_path))

    # 1. Get the list of files in the path
    if not os.path.exists(path_dir):
        print("Path {0} is not exists. ".format(path_dir))
        return

    for i in os.listdir(path_dir):
        tmp_path = os.path.join(path_dir, i)
        print(tmp_path)
        csv_files.append(tmp_path)

    # 2. For each of *.csv file in the path,
    # read and calculate the average value of each column.
    # And store the value, which should be store into a new *.csv
    # file as just one row.
    values_record = []
    for tmp_csv_path in csv_files:
        tmp_return_value = calculate_csv_average_value(tmp_csv_path)
        values_record.append(tmp_return_value)

def calculate_csv_average_value( csv_filepath ):
    """
    calculate_csv_average_value
    param:
        csv_filepath: the absolute path of the csv_fileself.
        The title of the *.csv file is below:
        "Index","FileName","eyebrow-left","eyebrow-right","eye-left","eye-right",
        "face-left","face-right","lip-above-left","lip-above-right",
        "mouth-corner-left","mouth-corner-right","lip-below-left",
        "lip-below-right","nose-left","nose-right"
        We need to calculate online the part from "eyebrow-left" to "nose-right".
    return:
        a list of average values, first is Filename of *.csv file.
        e.g. ["test_data.csv", 1.5, 7.8].
    """
    with open( csv_filepath ) as csv_file:
        csv_file_reader = csv.reader(csv_file)
        title = next( csv_file_reader )     # filter the title of the csv file

        # Intialize the return list
        value = []
        value.append(csv_filepath)
        first_row = next( csv_file_reader )
        del first_row[0:2]                  # delete the first part
        for bleed_speed in first_row:
            value.append(float(bleed_speed))

        # Add all row value
        for row in csv_file_reader:
            for i in range(2,16):
                value[i-1] += float(row[i])
        # calculate the average value
        count = csv_file_reader.line_num - 1
        for i in range(1,15):
            value[i] = value[i] / count
        print(value)
        return value

def save_csv_result( csv_save_path ):
    """
    To be finished.
    """
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
        "-s",
        "--save_file_path",
        dest = "save_file_path",
        default = "./",
        type = str,
        help ="the floder to output the model" )

    FLAGS, unparsed = parser.parse_known_args()

    print( FLAGS )      # print the arguments
    main()
