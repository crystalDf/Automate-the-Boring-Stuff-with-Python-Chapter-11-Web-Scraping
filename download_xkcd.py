#! python3
# download_xkcd.py - Downloads every single XKCD comic.

import requests
import os
import bs4

url = 'http://xkcd.com' # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

while not url.endswith('#'):
# TODO: Download the page.
# TODO: Find the URL of the comic image.
# TODO: Download the image.
# TODO: Save the image to ./xkcd.
# TODO: Get the Prev button's url.
    break

print('Done.')
