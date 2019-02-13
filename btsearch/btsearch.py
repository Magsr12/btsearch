from prettytable import PrettyTable
from __engine__ import *
import time
import sys
import os


def main(call='kickass', repeat=False):
    x = 0
    if 'kickass' in call:
    	table = PrettyTable(['N', 'Nome', 'Tam', 'Seeders'])
    	table.align['N'], = 'l'
    	table.align['Nome'] = 'l'
    	table.align['Tam'] = 'l'
    	table.align['Seeders'] = 'l'
    	print '[*] Procurando em https://kickasstorrents.to por: ' + sys.argv[1]
    	print '[*] Query: {} | PAGE_RANGE: {}'.format(sys.argv[1], PAGE_RANGE)
    	kickass(sys.argv[1])
    	if len(k_titles) == 0:
    		print '[*] Nenhum resultado encontrado, tentando novamente...'
    		time.sleep(1)
    		main(repeat=True)
    	else:
    		print '[*] Resultados de https://kickasstorrents.to para: ' + sys.argv[1]
    		for a, b, c in zip(k_titles, k_sizes, k_seeders):
    			x += 1
    			table.add_row([x, a[:40], b, c])
    		print table
    		print '[*] {} resultados encontrados'.format(len(k_titles))
    		asp = raw_input('[*] Selecione um numero da lista ou digite next para prosseguir a pesquisa com thepiratebay.org: ')
    		if asp == 'next':
    			main(call='tpb')
    		else:
    			choice = int(asp) - 1
    			print '\n' + k_titles[choice]
    			retrieve_magnet(url='https://kickasstorrents.to/' + k_links[choice])
    		asp = raw_input('[*] Deseja abrir aplicativo torrent ? [S/n]: ')
    		if asp == 'n':
    			exit()
    		else:
    			os.system('start bittorrent {}'.format(t_magnets[choice]))

    else:
    	table = PrettyTable(['N', 'Nome', 'Tam'])
    	table.align['N'], = 'l'
    	table.align['Nome'] = 'l'
    	table.align['Tam'] = 'l'
    	print '[*] Procurando em http://thepiratebay.org por: ' + sys.argv[1]
    	tpb(sys.argv[1])
    	if len(t_titles) == 0:
    		print '[*] Nenhum resultado encontrado, tentando novamente...'
    		time.sleep(1)
    		main(repeat=True)
    	else:
    		print '[*] Resultados de http://thepiratebay.org para: ' + sys.argv[1]
    		for a, b in zip(t_titles,t_sizes):
    			x += 1
    			table.add_row([x, a[:50], b])
    		print table
    		print '[*] {} resultados encontrados'.format(len(t_titles))
    		asp = raw_input('[*] Selecione um numero da lista: ')
    		choice = int(asp) - 1
    		print '\n' + t_titles[choice] + '\n'
    		print t_magnets[choice]
    		asp = raw_input('[*] Deseja abrir aplicativo torrent ? [S/n]: ')
    		if asp == 'n':
    			exit()
    		else:
    			os.system('start bittorrent {}'.format(t_magnets[choice]))


if len(sys.argv) < 2:
	exit('\nUso: python btsearch.py "{SEARCH}"')  
main()