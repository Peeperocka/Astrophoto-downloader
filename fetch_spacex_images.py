import requests
import argparse

from pathlib import Path
from supporting_scripts import download_img


def fetch_spacex_launch_with_id(id):
    url = f'https://api.spacexdata.com/v5/launches/{id}'

    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    photo_url_list = response['links']['flickr']['original']
    if not photo_url_list:
        print('No files written in directory cause 0 files were given')
    else:
        for num, url in enumerate(photo_url_list):
            filepath = f'images/spacex_{num}.jpg'
            download_img(url, filepath)


if __name__ == '__main__':
    Path('images').mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(
        description='This program can download photos from SpaceX lauches'
    )
    parser.add_argument('-i', '--id', help='Launch ID', default='latests')
    args = parser.parse_args()

    fetch_spacex_launch_with_id(args.id)
