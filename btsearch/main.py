#coding: utf-8

from prettytable import PrettyTable
from __engine__ import *
from __colors__ import *
from __temp__ import *
import time
import sys
import os


def init(call='kickass', movies=False, verbose=False, PAGE_RANGE=4, repeat=False, x=0):
    if not movies:
        table = PrettyTable(['N', 'Nome', 'Tam', 'Seeders'])
        table.align['N'] = 'l'
        table.align['Nome'] = 'l'
        table.align['Tam'] = 'l'
        table.align['Seeders'] = 'l'
    else:
        table = PrettyTable(['N', 'Nome'])
        table.align['N'] = 'l'
        table.align['Nome'] = 'l'

    if movies:
        if 'bludv' in call:
            if int(PAGE_RANGE) >= 3:
                print '[*] Recomenda-se diminuir o numero de paginas em -r para acelerar a busca.'
            print '[*] Procurando em sites nao oficiais, use --verbose para acompanhar o processo.'
            print GREEN + '[*] Procurando em bludvcomandotorrents.com por: {}'.format(NORMAL + sys.argv[1])
            bludv(sys.argv[1], PAGE_RANGE, verbose=verbose)
            if len(bludv_titles) == 0:
                x += 1
                if x == 3:
                    print RED + '[*] Nenhum resultado encontrado em bludvcomandotorrents.com'
                    init(call='kickass')
                if x == 1:
                    print RED + '[*] 2 tentativas restantes...'
                if x != 3:
                    print RED + '[*] Nenhum resultado encontrado, tentando novamente...' + NORMAL
                    init(call='bludv', x=x)
            else:

                print YELLOW + '[*] Resultados de bludvcomandotorrents.com para: ' + NORMAL + sys.argv[1]
                for a in bludv_titles:
                    x += 1
                    table.add_row([x, a[:50]])
                print table
                print GREEN + '[*] {} resultados encontrados para as {} primeiras paginas.'.format(len(bludv_titles), int(PAGE_RANGE)) + NORMAL
                resp = raw_input('[*] Selecione um numero da lista: ')
                blu_choice = int(resp) - 1
                print '\n' + bludv_titles[blu_choice] + '\n\n' + bludv_magnets[blu_choice]

    if 'kickass' in call:
        print YELLOW + '[*] Procurando em kickasstorrents.to por: {}...'.format(NORMAL + sys.argv[1])
        kickass(sys.argv[1], PAGE_RANGE)
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
                retrieve_magnet(url='https://kickasstorrents.to/' + k_links[choice], call='kickass')
            asp = raw_input('\n[*] Deseja abrir aplicativo torrent ? [S/n]: ')
            if asp == 'n':
                clean_pyc_files()
                exit()
            else:
                os.system('start bittorrent "{}"'.format(k_magnets[0]))
                clean_pyc_files()
                exit()

    elif 'tpb' in call:
        print YELLOW + '[*] Procurando em thepiratebay.org por: {}...'.format(NORMAL + sys.argv[1])
        tpb(sys.argv[1], PAGE_RANGE)
        if len(t_titles) == 0:
            x += 1
            if x == 3:
                print RED + '[*] Nenhum resultado encontrado em thepiratebay.org' + NORMAL
                clean_pyc_files()
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
            asp = raw_input('[*] Selecione um numero da lista ou digite next para prosseguir com 1337x.to: ')
            if asp == 'next':
                init(call='1337x')
            choice = int(asp) - 1
            print '\n' + t_titles[choice] + '\n'
            print t_magnets[choice]
            asp = raw_input('\n[*] Deseja abrir aplicativo torrent ? [S/n]: ')
            if asp == 'n':
                clean_pyc_files()
                exit()
            else:
                os.system('start bittorrent "{}"'.format(t_magnets[choice]))
                clean_pyc_files()
                exit()
    elif '1337x' in call:
        print YELLOW + '[*] Procurando em 1337x.to por: {}...'.format(NORMAL + sys.argv[1])
        x1337(sys.argv[1], PAGE_RANGE)
        if len(x_titles) == 0:
            x += 1
            if x == 3:
                print RED + '[*] Nenhum resultado encontrado em 1337x.to' + NORMAL
                clean_pyc_files()
                exit()
            if x == 1:
                print RED + '[*] 2 tentativas restantes...' + NORMAL
            if x != 3:
                print RED + '[*] Nenhum resultado encontrado, tentando novamente...' + NORMAL
                init(call='1337x', x=x)
        else:
            print '[*] Resultados de 1337x.to para: ' + NORMAL + sys.argv[1]
            for a, b, c in zip(x_titles,x_sizes,x_seeders):
                x += 1
                table.add_row([x, a[:50], b, c])
            print table
            print YELLOW + '[*] {} paginas, {} resultados encontrados'.format(PAGE_RANGE, len(x_titles)) + NORMAL
            if int(x) != int(PAGE_RANGE):
                k = 0
                print RED + '[*] Parece que nao foi possivel reagrupar todos valores da pagina, tentando novamente...' + NORMAL; time.sleep(4)
                for i in x_titles:
                    temp_list.append(x)
                for a, b, c in zip(temp_list,x_sizes,x_seeders):
                    k += 1
                    table.add_row([k, a, b, c])
                if int(x) != int(PAGE_RANGE):
                    print RED + '[*] Nao foi possivel reagrupar todos valores possiveis.' + NORMAL
       
            try:
                asp = raw_input('[*] Selecione um numero da lista: ')
                choice = int(asp) - 1
            except (ValueError, IndexError):
                asp = raw_input('[*] Selecione um numero da lista: ')
            print '\n' + x_titles[choice] + '\n'
            retrieve_magnet(url='https://1337x.to' + x_links[choice], call='1337x')
            asp = raw_input('\n[*] Deseja abrir aplicativo torrent ? [S/n]: ')
            if asp == 'n':
                clean_pyc_files()
                exit()
            else:
                os.system('start bittorrent "{}"'.format(x_magnets[choice]))
                clean_pyc_files()
                exit()            
