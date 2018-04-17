#-*- coding: utf-8 -*-
"""
Author: Chaoqun
Time: 2018-04-17


"""

import sys
import os
import time
import operator

FLAGS = None

def main():
    """ main function
    """
    print("Will finished in soon!")
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
