import os
import requests

from pathlib import Path
from dotenv import load_dotenv
from supporting_scripts import download_img

PATH = 'images'


def get_epics_nasa(api_key):
    params = {
        'api_key': api_key,
    }
    url = 'https://api.nasa.gov/EPIC/api/natural/images'

    responses = requests.get(url, params=params)
    responses.raise_for_status()
    responses = responses.json()

    for num, reply in enumerate(responses):
        date = reply['date'].split()
        date = date[0].split(sep='-')
        image = reply['image']

        url = f'https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{image}.png?api_key={api_key}'
        filepath = f'{PATH}/nasa_epic_{num}.png'

        download_img(url, filepath)


if __name__ == '__main__':
    load_dotenv()
    api_key_nasa = os.environ['API_KEY_NASA']

    Path(PATH).mkdir(parents=True, exist_ok=True)

    get_epics_nasa(api_key_nasa)
