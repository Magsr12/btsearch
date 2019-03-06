#coding: utf-8
import os
import argparse
from __strings__ import *
try:
	from main import *
	from __colors__ import *
except ImportError:
	os.system('pip install -r requirements.txt')
	from main import *
	from __colors__ import *

usage = RED + '''
888888b. 88888888888 .d8888b.  8888888888        d8888 8888888b.   .d8888b.  888    888 
888  "88b    888    d88P  Y88b 888              d88888 888   Y88b d88P  Y88b 888    888 
888  .88P    888    Y88b.      888             d88P888 888    888 888    888 888    888 
8888888K.    888     "Y888b.   8888888        d88P 888 888   d88P 888        8888888888 
888  "Y88b   888        "Y88b. 888           d88P  888 8888888P"  888        888    888 
888    888   888          "888 888          d88P   888 888 T88b   888    888 888    888 
888   d88P   888    Y88b  d88P 888         d8888888888 888  T88b  Y88b  d88P 888    888 
8888888P"    888     "Y8888P"  8888888888 d88P     888 888   T88b  "Y8888P"  888    888
''' + YELLOW + '\nUso: python btsearch.py "SEARCH"'+ NORMAL + ' [-r 6] [-q tpb,kickass]\n' + '''
-q          Servico de pesquisa, disponiveis: tpb, kickass, 1337x.
-r          Numero maximo de paginas a serem vasculhadas, default=4.
--movies    Procura pela query em sites nao oficiais, pode levar mais tempo do que o normal.
--verbose   Habilita a depuracao, somente disponivel em --movies.
'''

if len(sys.argv) < 2:
    exit(usage)
    if '--help' in sys.argv or '-h' in sys.argv:
        exit(usage)


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











			




			


