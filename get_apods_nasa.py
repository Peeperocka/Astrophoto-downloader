import requests
import os
import argparse

from pathlib import Path
from dotenv import load_dotenv
from supporting_scripts import get_urls_file_extension, download_img


def get_apods_nasa(api_key, count):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': count
    }

    responses = requests.get(url, params=params)
    responses.raise_for_status()

    responses = responses.json()

    for num, response in enumerate(responses):
        photo_url = response['url']
        filepath = f'images/nasa_apod_{num}{get_urls_file_extension(photo_url)}'
        download_img(photo_url, filepath)


if __name__ == '__main__':
    load_dotenv()

    Path('images').mkdir(parents=True, exist_ok=True)

    api_key_nasa = os.environ['API_KEY_NASA']

    parser = argparse.ArgumentParser(
        description='This program can download APODs from NASA'
    )
    parser.add_argument('count', help='APODs count', default='1')
    args = parser.parse_args()

    get_apods_nasa(api_key_nasa, args.count)
