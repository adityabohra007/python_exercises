#!/usr/bin/env python3

from bs4 import BeautifulSoup
import getopt
import os
import re
import requests
import sys
import urllib.request


def parse_article(text):
    soup = BeautifulSoup(text, 'html.parser')

    # scraping article title
    h1 = soup.body.find('h1')

    root = h1

    if not root:
        return None

    while root.name != 'body' and len(root.find_all('p')) < 5:
        root = root.parent

    # scraping article body
    paragraphs = root.find_all(['h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre'])
    content = [p.text for p in paragraphs]

    # scraping images
    imgs = root.find_all(['img'])
    images = []
    for img in imgs:
        if img.get('src').startswith('http') or img.get('src').startswith('www'):
            images.append(img.get('src'))

    return {'title': h1.text.strip(), 'content': ''.join(content).strip(), 'images': images}


def save_data(data, url):
    data_dir = 'scraped_sites'
    if not os.path.exists(os.path.join('.', data_dir)) \
            or not os.path.isdir(os.path.join('.', data_dir)):
        os.mkdir(os.path.join('.', data_dir))

    dir_name = re.sub(r'^(https?://)?(www.)?', '', url)
    dir_name = re.sub(r'/', '_', dir_name)

    dir_index = 1
    while os.path.exists('./{}/{}_{}'.format(data_dir, dir_name, dir_index)):
        dir_index += 1

    dir_path = './{}/{}_{}'.format(data_dir, dir_name, dir_index)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    with open(os.path.join(dir_path, 'data.txt'), 'w') as file:
        file.write('Title: {}\n\n'.format(data['title']))
        file.write('Content:\n{}\n\n'.format(data['content']))

    if data['images']:
        image_index = 0
        for image_url in data['images']:
            image_index += 1
            image_format = image_url[-3:]

            image_filename = 'image_{}.{}'.format(image_index, image_format)
            urllib.request.urlretrieve(image_url, os.path.join(dir_path, image_filename))


def main(argv):
    url = None

    try:
        options = getopt.getopt(argv, '', ['url='])

        for option, argument in options[0]:
            if option == '--url' and argument:
                url = argument
    except getopt.GetoptError as e:
        print(e)

    if url:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = parse_article(response.content)
                if data:
                    save_data(data, url)
                else:
                    print("Can't scrape provided URL: {}".format(url))
        except Exception as e:
            print(e)
    else:
        print('No URL provided')


if __name__ == '__main__':
    main(sys.argv[1:])
