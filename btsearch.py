#coding: utf-8

import urllib2, sys, os, ssl, time, datetime
from urllib import *
from urlparse import *
from prettytable import PrettyTable

try:
        import lxml.html
except ImportError:
        print '[*] Pacote nao instalado: lxml'
        os.system('pip install lxml')

timing = 0 # String to repeat requests if search output is empty

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

class SearchResultParser:
	def __init__(self, html):
		self.doc = lxml.html.parse(html).getroot()
	
	def parse(self):
		row_data = []
		try:
			table = self.doc.xpath('//*[@id="searchResult"]')[0]
			rows = [row for row in table.iterchildren() if row.tag == 'tr']
			for row in rows:
				columns = row.getchildren()[1:]
				row_data.append(self.parse_row_columns(columns))
		except:
			pass
		return row_data
	
	def parse_row_columns(self, columns):
		"""Parse the columns of a table row.
		
		*Returns*
			a dictionary with parsed data.
		"""
		data = {}
		data["user_type"] = "standard"
		for ele in columns[0].iterchildren():
			if ele.tag == 'div' and ele.get('class') == 'detName':
				a = ele.find('a')
				data["torrent_info_url"] = urljoin(ele.base, a.get('href'))
				data["name"] = a.text_content()
			elif ele.tag == 'a':
				if ele.get('title') == "Download this torrent":
					data["torrent_url"] = ele.get("href")
				elif ele.get('title') == "Download this torrent using magnet":
					data["magnet_url"] = ele.get("href")
				elif ele[0].tag == 'img':
					if ele[0].get('title') == "VIP":
						data["user_type"] = "VIP"
					elif ele[0].get('title') == "Trusted":
						data["user_type"] = "trusted"
					
			elif ele.tag == 'font':
				a = ele.find('a')
				if a is None:
					data['user'] = "Anonymous"
				else:
					data['user'] = urljoin(ele.base, a.get('href'))
				data["uploaded_at"], data["size_of"] = self.process_datetime_string(ele.text_content())
		data['seeders'] = int(columns[1].text_content().strip())
		data['leechers'] = int(columns[2].text_content().strip())
		
		return data

	def process_datetime_string(self, string):
		"""Process the datetime string from a torrent upload.
	
		*Returns*
			Tuple with (datetime, (size, unit))
		"""
		def process_datetime(part):
			if part.startswith("Today"):
				h, m = part.split()[1].split(':')
				return datetime.datetime.now().replace(
					hour=int(h), minute=int(m))
			elif part.startswith("Y-day"):
				h, m = part.split()[1].split(':')
				d = datetime.datetime.now()
				return d.replace(
					hour=int(h), minute=int(m),
					day=d.day-1
				)
			elif part.endswith("ago"):
				amount, unit = part.split()[:2]
				d = datetime.datetime.now()
				if unit == "mins":
					d = d.replace(minute=d.minute - int(amount))
				return d
			else:
				d = datetime.datetime.now()
				if ':' in part:
					current_date, current_time = part.split()
					h, m = current_time.split(':')
					month, day = current_date.split('-')
					d = d.replace(hour=int(h), minute=int(m), month=int(month), day=int(day))
				else:
					current_date, year = part.split()
					month, day = current_date.split('-')
					d = d.replace(year=int(year), month=int(month), day=int(day))
				return d
		def process_size(part):
			units = {'MiB':1048576, 'GiB': 1073741824}
			size, unit = part.split()[1:]
			size = float(size) * units[unit]
			return int(size)
		string = string.replace(u"\xa0", " ")
		results = [x.strip() for x in string.split(',')]
		date = process_datetime(' '.join(results[0].split()[1:]))
		size = process_size(results[1])
		return (date, size)
		

class ThePirateBay:
	"""Api for the Pirate Bay"""

	name = 'The Pirate Bay'
	
	searchUrl = 'http://thepiratebay.org/search/%s/0/7/%d'
	
	def __init__(self):
		pass
			
	def search(self, term, cat=None):
		if not cat:
			cat = 0
		url = self.searchUrl % (quote_plus(term), cat)
		# Added string gcontext ( SSL CERTIFICATE ERROR )
		gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
		req = urllib2.Request(url, headers=hdr)
		try:
                	html = urllib2.urlopen(req, context=gcontext) #context added
                except urllib2.HTTPError:
                        main(repeat=True)
		parser = SearchResultParser(html)
		return parser.parse()


def copy_to_path(): #Func to copy the script to home dir
        script_dir = os.getcwd() + '/' + sys.argv[0]
        home_dir = os.path.expanduser('~/')        
        if os.path.isfile(home_dir + 'btsearch.py'):
                pass
        else:
                import shutil
                shutil.copy(script_dir, home_dir)
                print '[*] Criado link em {}'.format(home_dir + sys.argv[0])
        
def main(repeat=False):
        copy_to_path()
        global timing
        magnet_results_ = []
        title_results_ = []
        seeders_results_ = []
        x = 0
        try:
                search_query = sys.argv[1]
                if "'" in search_query:
                        exit('[*] ALERTA: voce deve utilizar ASPAS DUPLAS durante a pesquisa, ex: python btsearch.py "Avatar".')
		else:
			if repeat == False:
				print('[*] Para conseguir todos resultados possiveis, e necessario utilizar ASPAS DUPLAS durante a pesquisa')
                        
        except IndexError:
                exit('[*] Uso: python btsearch.py "<SEARCH>"')
                
        if search_query == '-h' or search_query == '--help':
                exit('[*] Uso: python btsearch.py  "<SEARCH>"')
                
        def prettySize(size):
                suffixes = [("B",2**10), ("K",2**20), ("M",2**30), ("G",2**40), ("T",2**50)]
                for suf, lim in suffixes:
                        if size > lim:
                                continue
                        else:
                                return round(size/float(lim/2**10),2).__str__()+suf
        t = ThePirateBay()        
        print "[*] Procurando em http://thepiratebay.org por: {}".format(search_query)
        table = PrettyTable(['N', 'Nome', 'Tam',  'Seeders'])  #Datatable main string
        table.align['N'] = 'l'
        table.align['Nome'] = "l"
        table.align['Seeders'] = 'l'
        table.align['Tam'] = 'l'
        
        for t in t.search(str(search_query)):
                x += 1
                #output =  '[{}] '.format(x) + "(" + str(prettySize(t['size_of'])) + ")" + "__________" + t['name'].encode('utf-8') IF YOU WANT TO EDIT THE OUTPUT
                magnet_results_.append(str(t['magnet_url']))
                title_results_.append(str(t['name'].encode('utf-8')))
                seeders_results_.append(str(t['seeders']))
                table.add_row([x, t['name'].encode('utf-8'), str(prettySize(t['size_of'])), t['seeders']]) # Add the retrieved values to the table row
                
        if len(title_results_) == 0:
                timing += 1
                print '[*] Nenhum resultado encontrado, tentando novamente...'
                time.sleep(2)
                if timing == 4:
                        exit('[*] Nao foram encontrados resultados para {} em https://thepiratebay.org'.format(search_query))
                else:
                        main(repeat=True)                
        else:
                print '\n                   Ordem por seeders: DESC | Order by sedeers: DESC                   '
                print table

                
	print ('\n\n[*] Resultados encontrados: {}'.format(len(title_results_)))                
        asp = raw_input('[*] Insira um numero da lista: ')
        choice = int(asp) - 1
        print "\n[*] Magnet link para {}.\n".format(title_results_[choice])
        print magnet_results_[choice]
        asp2 = raw_input('\n[*] Deseja abrir Bittorrent ? [S/n]: ')
        if asp2 == 'n':
                exit()
        else:
                cmd = os.system('start bittorrent "{}"'.format(magnet_results_[choice]))
                
main()
