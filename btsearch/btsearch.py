from prettytable import PrettyTable
from __engine__ import *
import time
import sys


def main(_engine_='tpb, kickass', repeat=False):
    table = PrettyTable(['N', 'Nome', 'Tam'])
    table.align['Nome'] = 'l'
    table.align['Tam'] = 'l'
    x = 0
    if 'kickass' in _engine_:
    	print '[*] Query: {} | PAGE_RANGE: {}'.format(sys.argv[1], PAGE_RANGE)
    	kickass(sys.argv[1])
    	if len(titles) == 0:
    		print '[*] Nenhum resultado encontrado, tentando novamente...'
    		time.sleep(1)
    		main(repeat=True)
    	else:
    		print '[*] Resultados de https://kickasstorrents.to para: ' + sys.argv[1]
    		for a, b in zip(titles, sizes):
    			x += 1
    			table.add_row([x, a, b])
    		print table
    		print '[*] {} resultados encontrados'.format(len(titles))
    		asp = raw_input('[*] Selecione: ')
    		choice = int(asp) - 1
    		print '\n' + titles[choice]
    		retrieve_magnet(url='https://kickasstorrents.to/' + links[choice])


def results():
    table = PrettyTable(['N', 'Nome', 'Tam'])
    table.align['Nome'] = 'l'
    table.align['Tam'] = 'l'
    x = 0
    for a, b in zip(titles, sizes):
        x +=1 
        table.add_row([x, a, b])
    print table

    choice = int(asp) - 1
    print '\n' + titles[choice]
    retrieve_magnet(url='https://kickasstorrents.to/' + links[choice])
     
main()