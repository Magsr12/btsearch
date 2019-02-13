from main import *
from __strings__ import *
import argparse


if len(sys.argv) < 2:
	exit('[*] Uso: python btsearch.py {SEARCH}')
for a in sys.argv:
	if a == sys.argv[0]:
		pass
	else:
		if int(PAGE_RANGE) > 6:
			exit('[*] Numero maximo de paginas excedido, valor maximo: 6')
		'''

		if a == '-r':
			global PAGE_RANGE
			NEW_RANGE = sys.argv[value]
			if int(NEW_RANGE) > 5:
				
			print '[*] Numero de paginas: ' + str(NEW_RANGE)
			PAGE_RANGE = int(NEW_RANGE)
		'''
init()






			




			


