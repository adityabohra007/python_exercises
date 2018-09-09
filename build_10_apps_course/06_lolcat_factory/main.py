import os
import platform
import subprocess

import cats_service

CATS_TO_DOWNLOAD = 8
DOWNLOAD_DIR_NAME = 'cats'
URL = 'http://consuming-python-services-api.azurewebsites.net/cats/random'


def main():
    print_header()
    download_dir = get_directory(DOWNLOAD_DIR_NAME)
    cats_download(URL, download_dir)
    cats_display(download_dir)


def print_header():
    print('---------------------------')
    print('     Cat Factory App')
    print('---------------------------')
    print()


def get_directory(dir_name):
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, dir_name)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        os.mkdir(full_path)

    return full_path


def cats_download(url, download_dir):
    print('Contacting cat service for cat pictures...\n')

    for i in range(1, CATS_TO_DOWNLOAD + 1):
        print('Downloading cat {} ... '.format(i), end='')
        img_name = 'lolcat_' + str(i)
        cats_service.get_cat(url, download_dir, img_name)
        print('done.')


def cats_display(download_dir):
    print('\nLaunching output directory in Finder')

    if os.path.exists(download_dir) and os.path.isdir(download_dir):
        if platform.system() == 'Linux':
            subprocess.call(['xdg-open', download_dir])
        elif platform.system() == 'Darwin':
            subprocess.call(['open', download_dir])
        elif platform.system() == 'Windows':
            subprocess.call(['explorer', download_dir])
        else:
            print('We do not support your platform')


if __name__ == '__main__':
    main()
