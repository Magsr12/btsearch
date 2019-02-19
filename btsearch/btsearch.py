#coding: utf-8
import os
import argparse
from main import *
from __strings__ import *
from __colors__ import *

try:
    import lxml
except ImportError:
    print '[*] lxml nao instalado, tentando instalar...'
    os.system('pip install lxml')

try:
    import prettytable
except ImportError:
    print '[*] prettytable nao instalado, tentando instalar...'
    os.system('pip install prettytable')

try:
    import bs4
except ImportError:
    print '[*] bs4 nao instalado, tentando instalar...'
    os.system('pip install bs4')

try:
    import colorama
except ImportError:
    print '[*] colorama nao instalado, tentando instalar...'
    os.system('pip install colorama')

if len(sys.argv) < 2:
	exit(YELLOW + '[*] Uso: python btsearch.py ' + NORMAL + '"SEARCH"')
if '--help' in sys.argv or '-h' in sys.argv:
    exit(YELLOW + '''Uso: python btsearch.py "SEARCH" [-r 6] [-q tpb,kickass]\n''' + NORMAL +
'''
-q          Servico de pesquisa, disponiveis: tpb, kickass, 1337x.
-r          Numero maximo de paginas a serem vasculhadas, default=4.
--movies    Procura pela query em sites nao oficiais, pode levar mais tempo do que o normal.
--verbose   Habilita a depuracao, somente disponivel em --movies.
''')

parser = argparse.ArgumentParser()
parser.add_argument('"SEARCH"')
parser.add_argument('-q', required=False, dest='engines', help='Servico de pesquisa, disponiveis: tpb,kickass,1337x')
parser.add_argument('-r', '--page-range', dest='range', required=False, default=False, help='Numero de paginas a serem vasculhadas nos sites principais.')
parser.add_argument('-v', '--verbose', required=False, action='store_true', default=False, help='Liga a depuracao enquanto o programa esta ativo.')
parser.add_argument('--movies', required=False, action='store_true', default=False, help='Procura em sites nao oficiais por filmes, series e jogos.')
args = parser.parse_args()
movies = args.movies
calls = args.engines
new_range = args.range
verbose = args.verbose


if movies:
    if verbose:
        if new_range:
            init(call='bludv', PAGE_RANGE=new_range, movies=True, verbose=True)
        else:
            init(call='bludv', movies=True, verbose=True)
    else:
        if new_range:
            init(call='bludv', PAGE_RANGE=new_range, movies=True, verbose=False)
        else:
            init(call='bludv', movies=True)
if calls:
    if 'tpb' in calls and 'kickass' in calls:
        if new_range:
            init(call='kickass', PAGE_RANGE=new_range)
        else:
            init(call='kickass')
    elif 'kickass' in calls:
        if new_range:
            init(call='kickass', PAGE_RANGE=new_range, verbose=verbose)
        else:
            init(call='kickass', verbose=verbose)
    elif 'tpb' in calls:
        if new_range:
            init(call='tpb', PAGE_RANGE=new_range, verbose=verbose)
        else:
            init(call='tpb', verbose=verbose)
    elif '1337x' in calls:
        if new_range:
            init(call='1337x', PAGE_RANGE=new_range)
        else:
            init(call='1337x')
if not calls and not movies:
    if new_range:
        init(call='kickass', PAGE_RANGE=int(new_range))
    else:
        init()











			




			


