import requests
import os

from urllib.parse import urlparse


def download_img(url, filepath):
    response = requests.get(url)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)


def get_urls_file_extension(url):
    parsed_link = urlparse(url)
    splitted_path = os.path.splitext(parsed_link.path)
    return splitted_path[-1]
