import os
import ctypes
import requests
import platform
import argparse
from clint.textui import progress

class Utils:
	def __init__(self):
		#Windows 10 apps
		self.app_list = ['3dbuilder', 'windowsalarms', 'windowscommunicationsapps', 'windowscamera'
        		, 'bingnews', 'nonenote', 'people', 'windowsphone', 'windowsstore', 'bingsports', 'soundrecorder'
        		, 'officehub', 'skypeapp', 'zunemusic', 'windowsmaps', 'solitairecollection', 'bingfinance', 'zunevideo']

		self.services = ['SysMain', 'TrustedInstaller', 'wuauserv', 'msiserver']

	def services(self):		
        	print "[*] Desativando servico SysMain para otimizacao de disc_usage..."
        	sysmain_cmd = os.system('sc config sysmain start= disabled > NUL')
        	time.sleep(1.7)
        	if sysmain_cmd != 0:
                	print "[*] Nao foi possivel desativar o servico SysMain (superfetch)"
        	else:
                	print "[*] Servico SysMain (superfetch) desabilitado "
        	time.sleep(1.7)
        	print "[*] Desativando TrustedInstaller ( Instalador de Modulos )..."
        	trus_cmd = os.system('sc config TrustedInstaller start= demand > NUL')
        	if trus_cmd != 0:
                	print "[*] Nao foi possivel desativar o service TrustedInstaller (Instalador de modulos)"
        	else:
                	print "[*] Servico TrustedInstaller (Instalador de modulos) desabilitado"
        	time.sleep(1.7)
        	wua_serv = os.system('sc config wuauserv start= demand > NUL')
        	if wua_serv != 0:
                	print "[*] Nao foi possivel desativar o servico wuauserv (Windows Update)"
        	else:
                	print "[*] Servico wuauserv (Windows Update) desativado"
        	time.sleep(1.7)
        	msi_serv = os.system('sc config msiserver start= demand > NUL')
        	if msi_serv != 0:
                	print "[*] Nao foi possivel desativar o servico msiserver (Windows Installer)"
        	else:
                	print "[*] Servico msiserver (Windows Installer) desativado"
        	time.sleep(1.7)

	def apps(self):
		for app in self.app_list:
			try:
				apps_command = os.system('powershell "Get-AppxPackage *{}* | Remove-AppxPackage"'.format(app))
				if apps_command == 1:
					print "[*] Nao foi possivel desinstalar {}".format(app)
				else:
					print "[*] Removendo {}".format(app)
			except KeyboardInterrupt:
				time.sleep(2.9)
				exit()

	def windows_defender(self, func='disable'):
		if func == 'enable':
			print '[*] Habilitando Windows Defender...'
			os.system('start Turn_On_Windows_Defender_Antivirus.reg')
			print '[*] Windows Defender habilitado.'
		elif func == 'disable':
			print '[*] Desabilitando Windows Defender...'
			os.system('start Turn_Off_Windows_Defender_Antivirus.reg')
			print '[*] Windows defender desabilitado.'
		
	def disc_usage(self, dism_=False):
		if dism_:
			os.system('Dism /Online /Cleanup-Image /ScanHealth')
			os.system('Dism /Online /Cleanup-Image /RestoreHealth')
        	print  "[*] 1. Desabilite o arquivo de paginacao em: Avancado > Conf. Desempenho > Avancado > Alterar..."
        	print "[*] 2. Desative as configuracoes remotas do windows na aba Remoto"
		open_ = raw_input('[*] Abrir configuracoes [ENTER]')
		os.system('control sysdm.cpl')
		print '[*] Verificando se foram desabilitados...\n'
		for s in self.services:
			os.system('sc query {} | findstr  /i NOME_DO'.format(s))
			os.system('sc query {} | findstr  /i ESTADO'.format(s))
		print '\nFLAGS = STOPPED, RUNNING'
		print '\n[*] Caso haja algum servico em RUNNING, recomenda-se reiniciar o procedimento.'



class MainApp:
	def __init__(self):
		# If you want to add some apps here just do: self.app_path = '_directory_from_app_'
		#self.db_path = 'C:\Program Files (x86)\IObit\Driver Booster'
		#self.chrome_path = 'C:\Program Files (x86)\Google\Chrome'
		#self.winrar_path  = 'C:\Program Files\WinRAR'
		#self.vlc_path = 'C:\Program Files\VideoLAN\VLC'
		self.app_path = ['C:\Program Files (x86)\IObit\Driver Booster', 'C:\Program Files (x86)\Google\Chrome', 'C:\Program Files\WinRAR', 'C:\Program Files\VideoLAN\VLC']
		self.app_range = len(self.app_path)
		self.app_list = ['Driver Booster', 'Chrome', 'WINRAR', 'VLC']
		self.missing = []
		self.install_apps = []
		# Links for apps
		self.links = ['http://update.iobit.com/dl/driver_booster_setup.exe', 'http://redirector.gvt1.com/edgedl/release2/chrome/AM4yMAx_dXd__69.0.3497.100/69.0.3497.100_chrome_installer.exe',
         		'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-561.exe']
		#Headers
		self.hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		'Accept-Encoding': 'none',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive'}
				
	def download_pkg(self, name, link):
        	file_name = name + '.exe'
        	r = requests.get(link, stream=True, headers=self.hdr)
        	with open(file_name, 'wb') as f:
                	total_length = int(r.headers.get('content-length'))
                	for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                        	if chunk:
                                	f.write(chunk)
                                	f.flush()

	def check_packages(self):
		for i in range(self.app_range): # I am foda
			if os.path.isdir(self.app_path[i]):
				print '{} ENCONTRADO.'.format(self.app_list[i])
			else:
				print '{} NAO ENCONTRADO.'.format(self.app_list[i])
		'''
		if os.path.isdir(self.db_path):
        		print '[*] Driver booster instalado.'
		else:
        		print '[*] Driver booster nao instalado'
			self.missing.append('db.exe')      
		if os.path.isdir(self.chrome_path):
        		print '[*] Chrome instalado'
		else:
        		print '[*] Chrome nao instalado.'
        		self.missing.append('chrome-installer.exe')
		if os.path.isdir(self.winrar_path):
        		print '[*] Winrar instalado'
		else:
        		print '[*] WinRAR nao instalado.'
        		self.missing.append('winrar.exe')
'''

	def install_packages(self, post_execute=False):
		if len(self.missing) == 0:
			pass
		else:
			for i in self.missing:
				if 'db.exe' in i:
					print '[*] Baixando db.exe de: {}'.format(self.links[0])
					try:
						self.download_pkg('db', self.links[0])
					except KeyboardInterrupt:
						pass
					self.install_apps.append('db.exe')
					print '[*] {} salvo em {}'.format(i, os.getcwd() + '/' + i)
				if 'chrome-installer.exe' in i:
					print '[*] Baixando chrome-installer.exe de: {}'.format(self.links[1])
					try:
						self.download_pkg('chrome-installer', self.links[1])
					except KeyboardInterrupt:
						pass
					self.install_apps.append('chrome-installer.exe')
					print '[*] {} salvo em {}'.format(i, os.getcwd() + '/' + i)
				if 'winrar.exe' in i:
					print '[*] Baixando winrar.exe de: {}'.format(self.links[2])
					try:
						self.download_pkg('winrar', self.links[2])
					except KeyboardInterrupt:
						pass
					self.install_apps.append('winrar.exe')
					print '[*] {} salvo em {}'.format(i, os.getcwd() + '/' + i)
			for i in self.missing:
				if post_execute is True:
					print '[*] Executando {}'.format(i)
					os.system('{}'.format(i))
					ask_continue = raw_input('[*] Abrir o proximo instalador [ENTER]')
				
		

				

#is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0 # Check if the user is Admin
#if is_admin is False:
#	exit('\n[*] Voce precisa iniciar este script como admin !')	
#b = MainApps()
#b.check_packages()
#b.install_packages()

w_utils = Utils()
w_packages = MainApp()

def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('--download-apps', help='Somente baixa os aplicativos necessarios.', action='store_true', dest='download_apps', default=False)
	parser.add_argument('--install-apps', help='Baixa e instala os aplicativos necessarios.', action='store_true', dest='install_apps', default=False)
	parser.add_argument('--check-apps', help='Verifica se os aplicativos necessarios estao instalados.', action='store_true', dest='check_apps', default=False)
	parser.add_argument('--list-apps', help='Lista os aplicativos definidos como necessarios', action='store_true', dest='list_apps', default=False)
        args = parser.parse_args()
	just_download = args.download_apps
	download_and_install = args.install_apps
	check_apps = args.check_apps
	list_apps = args.list_apps
	if list_apps is True:
		for i in w_packages.all_apps:
			print i
	if check_apps is True:
		w_packages.check_packages()
	if just_download is True:
		w_packages.check_packages()
		w_packages.install_packages()
	if download_and_install is True:
		w_packages.check_packages()
		w_packages.install_packages(post_execute=True)

		

main()
	
		
		
		
		
		

	
