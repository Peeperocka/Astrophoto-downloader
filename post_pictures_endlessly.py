import os
import time
import random
import argparse

from post_image import post_image

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='This program posts images to telegram chat from directory'
    )
    parser.add_argument('-d', '--delay', help='Delay (hours)', default=4)
    args = parser.parse_args()
    delay = int(args.delay)*3600

    images = os.walk('images')
    for directory_images_list in images:
        images_list = []
        images_list += directory_images_list[-1]

    while 1:
        random.shuffle(images_list)

        for image in images_list:
            post_image(image)
            time.sleep(int(delay))
