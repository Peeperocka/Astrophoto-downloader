import requests
import argparse

from pathlib import Path
from supporting_scripts import download_img

PATH = 'images'


def fetch_spacex_images(id):
    url = f'https://api.spacexdata.com/v5/launches/{id}'

    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    photo_url_catalogue = response['links']['flickr']['original']
    for num, url in enumerate(photo_url_catalogue):
        filepath = f'{PATH}/spacex_{num}.jpg'
        download_img(url, filepath)


if __name__ == '__main__':
    Path(PATH).mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(
        description='This program can download photos from SpaceX lauches'
    )
    parser.add_argument('-id', help='Launch ID', default='latests')
    args = parser.parse_args()

    fetch_spacex_images(args.id)
