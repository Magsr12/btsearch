#coding: utf-8
from bs4 import *
from __strings__ import *
import lxml
import requests

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding': 'none',
'Accept-Language': 'en-US,en;q=0.8',
'Connection': 'keep-alive'}

def kickass(query):
    page = 0
    for i in range(1, int(PAGE_RANGE)):
        url = 'https://kickasstorrents.to/usearch/' + query + '/' + str(page)
        r = requests.get(url, headers=hdr)
        response = BeautifulSoup(r.content, 'lxml')
        for t in response.find_all('a', {'class':'cellMainLink'}): # GET TORRENT TITLES
            titles.append(t.get_text().strip())
        for s in response.find_all('td', {'class': 'nobr center'}): # GET SIZE FROM TORRENT FILES
            sizes.append(s.get_text().strip())
        for seeds in response.find_all('td', {'class': 'green center'}): # GET SEEDERS FROM TORRENT FILES
            kickass_seeders.append(seeds.get_text().strip())
        for html in response.find_all('a', {'class': 'cellMainLink'}, href=True):
            links.append(html['href'].encode('utf-8'))
        page += 1

def tpb(query):
    page = 0
    for i in range(1, int(PAGE_RANGE)):
        url = 'http://thepiratebay.org/search/' + query
        r = requests.get(url, headers=hdr)
        response = BeautifulSoup(r.content, 'lxml')
        for t in response.find_all('a', {'class':'detLink'}): # GET TORRENT TITLES
            titles.append(t.get_text().strip())
        for s in response.find_all('tr', {'class':'alt'}): # GET TORRENT SEEDERS, I CANT RESOLVE THIS, ESTA PUXANDO SEEDERS E LEECHERS JUNTOS.
            seeders.append(s.get_text().strip())
        for siz in response.find_all('font', {'class': 'detDesc'}):
            _siz_ = siz.get_text().strip()
            _siz_ = _siz_[21:34]
            _siz_ = _siz_.replace('Size ', '')
            if "," in _siz_:
                _siz_ = _siz_.replace(",", '')
            if "Gi" in _siz_:
                _siz_ = _siz_.replace("GiB", ' GB')
            if "Mi" in _siz_:
                _siz_ = _siz_.replace("MiB", ' MB')
            sizes.append(_siz_.encode('ascii', 'ignore')) # Convert unicode to string
        for magnet in response.find_all('a', {'title': 'Download this torrent using magnet'}):
            magnets.append(magnet['href'])
        page += 1

def retrieve_magnet(url):
    t = 0
    r = requests.get(url, headers=hdr)
    response = BeautifulSoup(r.content, 'lxml')
    for magnet in response.find_all('a', {'class': 'siteButton giantButton'}, href=True):
        t += 1
        if t == 1:
            print '\n' + magnet['href']
        else:
            pass