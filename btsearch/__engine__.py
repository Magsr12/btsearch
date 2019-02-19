#coding: utf-8

from bs4 import *
from __strings__ import *
from __colors__ import CYAN, NORMAL
import lxml
import requests


hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding': 'none',
'Accept-Language': 'en-US,en;q=0.8',
'Connection': 'keep-alive'}

def bludv(query, PAGE_RANGE, verbose=False):
    page = 1
    for i in range(1, int(PAGE_RANGE)): 
        url = 'https://bludvcomandotorrents.com/torrent/' + query + '/{}/'.format(int(page))
        r = requests.get(url, headers=hdr)
        response = BeautifulSoup(r.content, 'lxml')
        for t in response.find_all('img', {'class':'img-responsive'}):
            if verbose:
                print CYAN + '[*] Selecionando: ' + str(t['alt'].encode('ascii', 'ignore')) + NORMAL
            bludv_titles.append(t['alt'].encode('utf-8'))
        for l in response.find_all('a', href=True):
            if 'https://bludvcomandotorrents.com/f' in l['href'] or 'https://bludvcomandotorrents.com/j' in l['href']:
                if verbose:
                    print CYAN + '[*] Adicionando: ' + str(l['href']) + NORMAL
                bludv_links.append(l['href'])
        for urls in bludv_links:
            r = requests.get(urls, headers=hdr)
            response = BeautifulSoup(r.content, 'lxml')
            for m in response.find_all('a', {'class':'text-center newdawn'}):
                if verbose:
                    print CYAN + '[*] Encontrado: '+ str(m['href']) + NORMAL
                bludv_magnets.append(m['href'])
        page += 1

def kickass(query, PAGE_RANGE, verbose=False):
    page = 1
    for i in range(1, int(PAGE_RANGE)):
        url = 'https://kickasstorrents.to/usearch/' + query + '/' + str(page)
        r = requests.get(url, headers=hdr)
        response = BeautifulSoup(r.content, 'lxml')
        if verbose:
            print CYAN + 'Pagina: ' + str(i) + ' ' + str(r) + NORMAL
        for t in response.find_all('a', {'class':'cellMainLink'}): # GET TORRENT TITLES
            if verbose:
                print CYAN + 'Encontrado: ' + t.get_text().encode('ascii', 'ignore').strip() + NORMAL
            k_titles.append(t.get_text().encode('ascii', 'ignore').strip())
        for s in response.find_all('td', {'class': 'nobr center'}): # GET SIZE FROM TORRENT FILES
            k_sizes.append(s.get_text().strip())
        for seeds in response.find_all('td', {'class': 'green center'}): # GET SEEDERS FROM TORRENT FILES
            k_seeders.append(seeds.get_text().strip())
        for html in response.find_all('a', {'class': 'cellMainLink'}, href=True):
            k_links.append(html['href'].encode('utf-8'))
        page += 1

def tpb(query, PAGE_RANGE, verbose):
    page = 0
    r_seeders = 0 
    for i in range(1, int(PAGE_RANGE)):
        url = 'http://thepiratebay.org/search/' + query + '/' + str(page)
        r = requests.get(url, headers=hdr)
        response = BeautifulSoup(r.content, 'lxml')
        for t in response.find_all('a', {'class':'detLink'}): # GET TORRENT TITLES
            if verbose:
                print CYAN + str(t.get_text().strip().encode('ascii', 'ignore')) + NORMAL
            t_titles.append(t.get_text().strip().encode('ascii', 'ignore'))
        if verbose:
            print CYAN + '[*] Limitando valores de seeds e leechers...' + NORMAL           
        for s in response.find_all('td', {'align':'right'}):
            r_seeders += 1
            if r_seeders % 2 == 1: # GET ONLY TORRENT SEEDERS.
                t_seeders.append(s.get_text().strip())

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
            t_sizes.append(_siz_.encode('ascii', 'ignore')) # Convert unicode to string
        for magnet in response.find_all('a', {'title': 'Download this torrent using magnet'}):
            if verbose:
                print CYAN + str(magnet['href'])
            t_magnets.append(magnet['href'])
        page += 1

def x1337(query, PAGE_RANGE):
    page = 1
    for i in range(1, int(PAGE_RANGE)):
        url = 'https://1337x.to/search/' + query + '/' + str(page) + '/'
        r = requests.get(url, headers=hdr)
        response = BeautifulSoup(r.content, 'lxml')
        for t in response.find_all('td', {'class':'coll-1 name'}):
            x_titles.append(t.get_text().encode('ascii', 'ignore'))
        for s in response.find_all('td', {'class': 'coll-2 seeds'}):
            x_seeders.append(s.get_text())
        for siz in response.find_all('td', {'class': 'coll-4 size mob-uploader'}):
            sep = 'GB'  #https://stackoverflow.com/questions/904746/how-to-remove-all-characters-after-a-specific-character-in-python
            sep2 = 'MB'
            _siz_ = siz.get_text()
            if 'GB' in _siz_:
                x_sizes.append(_siz_.split(sep,1)[0] + 'GB')
            elif 'MB' in _siz_:
                x_sizes.append(_siz_.split(sep2,1)[0] + 'MB')
        for html in response.find_all('a', href=True):
            if '/torrent/' in html['href']:
                x_links.append(html['href'].encode('utf-8'))
        page += 1




def retrieve_magnet(url, call='kickass'):
    t = 0
    r = requests.get(url, headers=hdr)
    response = BeautifulSoup(r.content, 'lxml')
    if '1337x' in call:
        for magnet in response.find_all('a', {'class': 'ddcbbdeb btn btn-bfafeddf'}):
            t += 1
            if t == 1:
                print '\n' + magnet['href']
                x_magnets.append(magnet['href'])
            else:
                pass
    else:
        for magnet in response.find_all('a', {'class': 'siteButton giantButton'}, href=True):
            t += 1
            if t == 1:
                print '\n' + magnet['href']
                k_magnets.append(magnet['href'])
            else:
                pass

