#coding: utf-8

from prettytable import PrettyTable
from __engine__ import *
from __colors__ import *
import time
import sys
import os


def init(call='kickass', repeat=False, x=0):
    if 'kickass' in call:
        table = PrettyTable(['N', 'Nome', 'Tam', 'Seeders'])
        table.align['N'], = 'l'
        table.align['Nome'] = 'l'
        table.align['Tam'] = 'l'
        table.align['Seeders'] = 'l'
        print YELLOW + '[*] Procurando em kickasstorrents.to por: {}...'.format(NORMAL + sys.argv[1])
        kickass(sys.argv[1])
        if len(k_titles) == 0:
            x += 1
            if x == 3:
                print RED + '[*] Nenhum resultado encontrado em kickasstorrents.to'
                print YELLOW + '[*] Alternando para thepiratebay.org...' + NORMAL
                init(call='tpb')
            if x == 1:
                print RED + '[*] 2 tentativas restantes...'
            if x != 3:
                print RED + '[*] Nenhum resultado encontrado, tentando novamente...' + NORMAL
                init(x=x)

        else:
            print YELLOW + '[*] Resultados de kickasstorrents.to para: ' + NORMAL + sys.argv[1] 
            for a, b, c in zip(k_titles, k_sizes, k_seeders):
                x += 1
                table.add_row([x, a[:40], b, c])
            print table
            print YELLOW + '[*] {} resultados encontrados'.format(len(k_titles)) + NORMAL
            asp = raw_input('[*] Selecione um numero da lista ou digite next para prosseguir a pesquisa com thepiratebay.org: ')
            if asp == 'next':
                init(call='tpb')
            else:
                choice = int(asp) - 1
                print '\n' + k_titles[choice]
                retrieve_magnet(url='https://kickasstorrents.to/' + k_links[choice])
            asp = raw_input('\n[*] Deseja abrir aplicativo torrent ? [S/n]: ')
            if asp == 'n':
                exit()
            else:
                os.system('start bittorrent "{}"'.format(t_magnets[choice]))
                exit()

    else:
        table = PrettyTable(['N', 'Nome', 'Tam', 'Seeders'])
        table.align['N'], = 'l'
        table.align['Nome'] = 'l'
        table.align['Tam'] = 'l'
        table.align['Seeders'] = 'l'
        print YELLOW + '[*] Procurando em thepiratebay.org por: {}...'.format(sys.argv[1]) + NORMAL
        tpb(sys.argv[1])
        if len(t_titles) == 0:
            x += 1
            if x == 3:
                print RED + '[*] Nenhum resultado encontrado em thepiratebay.org' + NORMAL
                exit()
            if x == 1:
                print RED + '[*] 2 tentativas restantes...' + NORMAL
            if x != 3:
                print RED + '[*] Nenhum resultado encontrado, tentando novamente...' + NORMAL
                init(call='tpb', x=x)


        else:
            print '[*] Resultados de thepiratebay.org para: ' + NORMAL + sys.argv[1]
            for a, b, c in zip(t_titles,t_sizes,t_seeders):
                x += 1
                table.add_row([x, a[:50], b, c])
            print table
            print YELLOW + '[*] {} resultados encontrados'.format(len(t_titles)) + NORMAL
            asp = raw_input('[*] Selecione um numero da lista: ')
            choice = int(asp) - 1
            print '\n' + t_titles[choice] + '\n'
            print t_magnets[choice]
            asp = raw_input('\n[*] Deseja abrir aplicativo torrent ? [S/n]: ')
            if asp == 'n':
                exit()
            else:
                os.system('start bittorrent "{}"'.format(t_magnets[choice]))
                exit()

