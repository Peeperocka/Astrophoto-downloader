import os
import time
import random
import argparse

from dotenv import load_dotenv
from post_image import post_image

PATH = 'images'

if __name__ == '__main__':
    load_dotenv()

    parser = argparse.ArgumentParser(
        description='This program posts images to telegram chat from directory'
    )
    parser.add_argument('chatid', help='Telegram chat id')
    parser.add_argument('-d', '--delay', help='Delay (hours)', default=4)
    args = parser.parse_args()
    delay = int(args.delay)*3600

    images = os.walk(PATH)
    for directory_images_list in images:
        images = []
        images += directory_images_list[-1]

    while 1:
        random.shuffle(images)

        for image in images:
            post_image(image, args.chatid)
            time.sleep(int(delay))
