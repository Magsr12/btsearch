#coding: utf-8
import os
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
if int(PAGE_RANGE) > 6:
    exit('[*] Numero maximo de paginas excedido, valor maximo: 6')

init()






			




			


