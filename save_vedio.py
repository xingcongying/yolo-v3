
import os

import argparse
from yolo import YOLO, detect_video
# 遍历文件夹
def walkFile(file):
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            print(os.path.join(root, f))
            output='/home/hyq-user/xcy/old_keras-yolo3/vedio/'
            file_name=os.path.join(root, output+f)
            detect_video(YOLO(**vars(FLAGS)),file_name,f)
        # 遍历所有的文件夹
        for d in dirs:
            print(os.path.join(root, d))


def main():
    walkFile("/home/hyq-user/xcy/old_keras-yolo3/data/eat/")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    FLAGS = parser.parse_args()
    main()