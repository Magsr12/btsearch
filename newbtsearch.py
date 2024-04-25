import time
import os
import argparse
import sys
import requests
import lxml
import colorama

from bs4 import *
from prettytable import PrettyTable

colorama.init()

BOLD = '\033[1m'
CYAN = BOLD + '\033[36m'
NORMAL = BOLD + '\033[37m'
YELLOW = BOLD + '\033[33m'
RED = BOLD + '\033[31m'
GREEN = BOLD + '\033[32m'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding': 'none',
'Accept-Language': 'en-US,en;q=0.8',
'Connection': 'keep-alive'}

banner = """
https://github.com/magsr12/btsearch

888888b. 88888888888 .d8888b.  8888888888        d8888 8888888b.   .d8888b.  888    888 
888  "88b    888    d88P  Y88b 888              d88888 888   Y88b d88P  Y88b 888    888 
888  .88P    888    Y88b.      888             d88P888 888    888 888    888 888    888 
8888888K.    888     "Y888b.   8888888        d88P 888 888   d88P 888        8888888888 
888  "Y88b   888        "Y88b. 888           d88P  888 8888888P"  888        888    888 
888    888   888          "888 888          d88P   888 888 T88b   888    888 888    888 
888   d88P   888    Y88b  d88P 888         d8888888888 888  T88b  Y88b  d88P 888    888 
8888888P"    888     "Y8888P"  8888888888 d88P     888 888   T88b  "Y8888P"  888    888 
                                                                                
                                                                                ver: 2.0

Usage: python btsearch.py -s 'SEARCH' (make sure to use parenthesis)"""

k_titles = []
k_sizes = []
k_seeders = []
k_links = []
k_magnets = []

def search(query, PAGE_RANGE=4, verbose=True):
    print("[*] Starting btsearch...")
    time.sleep(2)
    page = 1
    print("[*] Creating lists and setting up...")
    for i in range(1, int(PAGE_RANGE)):
        search_url = 'https://kat.am/usearch/' + query + '/' + str(page)
        only_url = "https://kat.am"
        r = requests.get(search_url, headers=hdr)
        response = BeautifulSoup(r.content, 'lxml')
        print("[*] Connecting to {}".format(search_url))
        if verbose:
            print('Page: ' + str(i), ' ', str(r))
        for t in response.find_all('a', {'class':'cellMainLink'}): # GET TORRENT TITLES
            if verbose:
                print('found:', t.get_text().strip())
            k_titles.append(t.get_text().strip())
        for s in response.find_all('td', {'class': 'nobr center'}): # GET SIZE FROM TORRENT FILES
            k_sizes.append(s.get_text().strip())
        for seeds in response.find_all('td', {'class': 'green center'}): # GET SEEDERS FROM TORRENT FILES
            k_seeders.append(seeds.get_text().strip())
        for html in response.find_all('a', {'class': 'cellMainLink'}, href=True):
            k_links.append(html['href'].strip())
        page += 1
    t = 0
    print("\n[*] {} links are found on {} for search: {}".format(len(k_links), only_url, sys.argv[1]))
    print("[*] Trying to retrieve magnet links...\n")
    time.sleep(1)
    for discover_magnet in k_links:
        print("Accessing {}{}".format(only_url.strip(), discover_magnet))
        accessed_link = only_url.strip() + discover_magnet
        r = requests.get(accessed_link, headers=hdr)
        response = BeautifulSoup(r.content, 'lxml')
        for k in response.find_all('a', {'class': 'kaGiantButton'}):
            if "magnet" in k['href']:
                # print(CYAN, k['href'], NORMAL)
                k_magnets.append(k['href'])
            else:
                pass

    print("\n[*] btsearch has found {} titles and {} possible magnets links".format(len(k_links), len(k_magnets)))
    print("[*] trying to retrieve magnet in torrents pages...\n[*] Please wait...\n")
    time.sleep(2)
    c = 0
    if len(k_titles) == "0":
        exit("[*] btsearch has not found any expressive results.")
    for x in k_titles:
        c += 1
        print("[{}] {}".format(c, x))
    ch = input("\n[*] Select one from list: ")
    ch = int(ch) - 1
    print("[*] Retrieving data from title {}".format(k_titles[int(ch)]))
    print("\n", k_titles[int(ch)])
    print("\n", GREEN, k_magnets[int(ch)], NORMAL)
    #print("\n{}\n{}\n".format(k_titles[int(ch)], k_magnets[int(ch)]))




if len(sys.argv) < 2:
    exit(banner)
if '--help' in sys.argv or '-h' in sys.argv:
    exit(banner)

parser = argparse.ArgumentParser()
parser.add_argument('-s', required=True, dest='search_query', help='Seach query, remember to use parenthesis in search. e.g: "python btsearch.py -s "life of pi"')
args = parser.parse_args()
query = args.search_query

try:
    search(query)
except IndexError:
    exit('\nUsage: python btsearch.py -q "SEARCH" (search in parenthesis!)')
except requests.exceptions.ConnectionError as connect_error:
    print("[*] Detected request error")
    time.sleep(2)
    print("[*] Maybe kat.me is refusing our connections.")
    time.sleep(2.3)
    print("[*] You should consider to use an proxy or VPN while access torrent web-sites.")
    print("[*] Cannot access kat.me due connection error.")
    r = input("[*] Show output message ? [Y/n]")
    if r.lower() == "n":
        exit()
    else:
        print("\n", connect_error)