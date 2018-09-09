import os
import requests
import shutil


def get_cat(url, download_dir, img_name):
    data = get_data_from_url(url)
    save_image(data, download_dir, img_name)


def get_data_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw


def save_image(data, download_dir, img_name):
    file_path = os.path.join(download_dir, img_name + '.jpg')

    with open(file_path, 'wb') as file:
        shutil.copyfileobj(data, file)
