import os
import requests
import argparse

from pathlib import Path
from dotenv import load_dotenv
from supporting_scripts import get_urls_file_extension, download_img

PATH = 'images'


def get_apods_nasa(api_key, count):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': count
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    response = response.json()

    for num, reply in enumerate(response):
        photo_url = reply['url']
        filepath = f'{PATH}/nasa_apod_{num}{get_urls_file_extension(photo_url)}'
        download_img(photo_url, filepath)


if __name__ == '__main__':
    load_dotenv()

    Path(PATH).mkdir(parents=True, exist_ok=True)

    api_key_nasa = os.environ['API_KEY_NASA']

    parser = argparse.ArgumentParser(
        description='This program can download APODs from NASA'
    )
    parser.add_argument('-count', help='APODs count', default='1')
    args = parser.parse_args()

    get_apods_nasa(api_key_nasa, args.count)
