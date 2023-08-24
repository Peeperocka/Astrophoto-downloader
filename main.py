import requests
import os
import os.path

from urllib.parse import urlparse
from dotenv import load_dotenv
from pathlib import Path


def download_img(url, filepath):
    response = requests.get(url)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)


def fetch_spacex_launch_with_id(id):
    url = f'https://api.spacexdata.com/v5/launches/{id}'

    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    photo_url_list = response['links']['flickr']['original']

    for num, url in enumerate(photo_url_list):
        filepath = f'images/spacex_{num}.jpg'
        download_img(url, filepath)


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


def get_urls_file_extension(url):
    parsed_link = urlparse(url)
    splitted_path = os.path.splitext(parsed_link.path)
    return splitted_path[-1]


def get_epics_nasa(api_key):
    params = {
        'api_key': api_key,
    }
    url = 'https://api.nasa.gov/EPIC/api/natural/images'

    responses = requests.get(url, params=params)
    responses.raise_for_status()
    responses = responses.json()

    for num, response in enumerate(responses):
        date = response['date'].split()
        date = date[0].split(sep='-')
        image = response['image']

        url = f'https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{image}.png?api_key={api_key}'
        filepath = f'images/nasa_epic_{num}.png'

        download_img(url, filepath)


if __name__ == '__main__':
    load_dotenv()
    api_key_nasa = os.environ['API_KEY_NASA']
    spacex_launch_id = os.environ['SPACEX_LAUNCH_ID']
    pictures_count = os.environ['PICTURES_COUNT']

    Path('images').mkdir(parents=True, exist_ok=True)
    print(0)
    fetch_spacex_launch_with_id(spacex_launch_id)
    print(1)
    get_apods_nasa(api_key_nasa, pictures_count)
    print(2)
    get_epics_nasa(api_key_nasa)
    print(3)
    print('Bebra')
