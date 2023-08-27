import requests
import os

from pathlib import Path
from dotenv import load_dotenv
from supporting_scripts import download_img


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

    Path('images').mkdir(parents=True, exist_ok=True)

    api_key_nasa = os.environ['API_KEY_NASA']
    print(api_key_nasa)

    get_epics_nasa(api_key_nasa)
