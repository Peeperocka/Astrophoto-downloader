# Astrophoto downloader

This project contains scripts that help downloading photos from NASA and SpaceX sites and then to automaticly post them to telegram groop using bots.

## Installation

### How to install dependencies

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Enviroment 

You need `.env` file with this variables:

- `TELEGRAM_TOKEN={your bot token}` - You need to get your bot token from BotFather
- `API_KEY_NASA={your api key}` - get API key [there](https://api.nasa.gov/)

## Run

### Running scripts with console

To run program you must head to files' direcory and type: 

```
python script_name.py {arguments if script needs them}
```

### Scripts arguments

- `post_image.py` and `get_epics_nasa.py` do NOT require arguments
- `post_pictures_endlessly.py` 
    - has `delay(or -d)` argument that stands for delay between posts, 1 = 1 hour. Default value is 4 hours
    - has `chatid` argument that stands for telegram chat id there files should be dropped
- `fetch_spacex_images.py` takes -id argument that stands for lauch ID. If no ID was given, it'll try to get photos from last lauch, if no photos were found, program'll print about it.
- `get_apods_nasa.py` takes -count argument that stands for count of pictures to download, default value is 1

## Notes

You can change downloaded images path by changing global variable `PATH` in `post_image.py`, `get_epics_nasa.py`, `fetch_spacex_images.py`

### Scripts info

```
post_image.py
```

Simple script with only 1 fuction

1. Loads enviroment variables 
1. Sends document to chat using `send_document()`

```py
post_pictures_endlessly.py
```

1. Uses argparse to get delay and `os.walk()` to get all images from global variable `PATH` that stands for directory
1. uses `for` to get file names
1. shuffles all file names and posts them using `post_image.py` then waits to post another, another, another and another one, endlessly. 

```py
fetch_spacex_images.py
```

1. Checks if directory was already created, it not, creates it.
1. Loads `id` as console agrument
1. Creates url with `id`, gets info from url, raises_for_status.
1. Tries to get photos links and if there's no photos links, prints about it. Else downloads them to selected directory

```py
get_epics_nasa.py
```

1. Checks if directory was already created, it not, creates it. Loads enviroment varibables
1. Creates url and params, gets info from it, raises_for_status.
1. Using `for` creates download url and filepath, then downloads it.

```py
get_apods_nasa.py
```

1. Checks if directory was already created, it not, creates it. Loads enviroment varibables and console arguments
1. Creates url and params, then gets data from it, raises_for_status and converts data
1. Using `for`creates download urls and filepaths, then downloads it

```py
supporting_scripts.py
```

```py
def download_img()
```

1. Gets urls data, raises_for_status
1. Writes data to file

```py
def get_urls_file_extension()
```

1. Gets url, parses it to get filepath
1. Uses `os.path.splitext`to get splitted filepath
1. returns last part of filepath - file extension. 
