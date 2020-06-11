"""
required packages:
pip install requests==2.22.0 beautifulsoup4==4.8.1
"""
import requests
import argparse

from bs4 import BeautifulSoup

URL = 'https://sinoptik.ua/'


def parse_html():
    html_text = requests.get(URL).text
    parsed_html = BeautifulSoup(html_text, 'html.parser')

    main_elem = parsed_html.find('div', attrs={'class': 'wDescription clearfix'})
    descr_elem = main_elem.find('div', attrs={'class': 'description'})
    return descr_elem.text


if __name__ == '__main__':
    w_today = parse_html()
    print(w_today)
