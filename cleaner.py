import os
import sys
import threading
import emoji
import asyncio
import time
import getpass
import admin

from colorama import Fore, init

os.system('cls') if os.name == "nt" else os.system('clear')

import win32com.shell.shell as shell
ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)


init(autoreset = True)
c = Fore.LIGHTWHITE_EX
w = Fore.LIGHTGREEN_EX
banner = f"""
		 		 {c}█████{w}╗ {c}██{w}╗  {c}████████{w}╗
				{c}██{w}╔══{c}██{w}╗{c}██{w}║  ╚══{c}██{w}╔══╝
				{c}███████{w}║{c}██{w}║     {c}██{w}║   
				{c}██{w}╔══{c}██{w}║{c}██{w}║     {c}██{w}║   
				{c}██{w}║  {c}██{w}║{c}███████{w}╗{c}██{w}║   
				{w}╚═╝  ╚═╝╚══════╝╚═╝  
   			{w}>>>>>>> {c}Avast Cleaner copy{w} <<<<<<<
"""
print(banner)


text1 = "Фулл очистка"
text2 = "Очистка логов"
text3 = "Под ваше усмотрение"





print(f"			{w}[{Fore.RESET}1{w}] {text1}")
print(f"			{w}[{Fore.RESET}2{w}] {text2}")
print(f"			{w}[{Fore.RESET}3{w}] {text3}")
print()
print()
while True:
	choose = int(input(Fore.LIGHTRED_EX))
	if choose == 1:

		global_mb = 0
		print()

		
		os.chdir(rf"C:/Users/{getpass.getuser()}/Downloads")
		print()
		print(f"{w}[{Fore.RESET}!{w}] {os.getcwd()}")
		for file in os.listdir():
			try:
				size = os.path.getsize(file)
				os.remove(file)

				global_mb += int(size)
				print(f"{w}[{Fore.RESET}+{w}] {file} {size} кб ")
			except Exception:
				print(f"{w}[{Fore.RESET}-{w}] {file} {size} кб")
		os.chdir(fr"C:\Windows\SoftwareDistribution\DataStore\Logs")
		print()
		print(f"{w}[{Fore.RESET}!{w}] {os.getcwd()}")
		for file in os.listdir():
			try:
				size = os.path.getsize(file)
				os.remove(file)

				global_mb += int(size)
				print(f"{w}[{Fore.RESET}+{w}] {file} {size} кб ")
			except Exception:
				print(f"{w}[{Fore.RESET}-{w}] {file} {size} кб")
		os.chdir(r"C:\Windows\Temp")

		print()
		print(f"{w}[{Fore.RESET}!{w}] {os.getcwd()}")
		for file in os.listdir():
			try:
				size = os.path.getsize(file)
				os.remove(file)

				global_mb += int(size)
				print(f"{w}[{Fore.RESET}+{w}] {file} {size} кб ")
			except Exception:
				print(f"{w}[{Fore.RESET}-{w}] {file} {size } кб")
		os.chdir(r'C:\Windows\Logs\WindowsUpdate')
		print()
		print(f"{w}[{Fore.RESET}!{w}] {os.getcwd()}")
		for file in os.listdir():
			try:
				size = os.path.getsize(file)
				os.remove(file)

				global_mb += int(size)
				print(f"{w}[{Fore.RESET}+{w}] {file} {size} кб ")
			except Exception:
				print(f"{w}[{Fore.RESET}-{w}] {file} {size} кб")

		os.chdir(fr"C:/ProgramData/USOShared/Logs/System")
		print()
		print(f"{w}[{Fore.RESET}!{w}] {os.getcwd()}")
		for file in os.listdir():
			try:
				size = os.path.getsize(file)
				os.remove(file)

				global_mb += int(size)
				print(f"{w}[{Fore.RESET}+{w}] {file} {size} кб ")
			except Exception:
				print(f"{w}[{Fore.RESET}-{w}] {file} {size} кб")
		os.chdir(fr"{os.getenv('temp')}")
		print()
		print(f"{w}[{Fore.RESET}!{w}] {os.getcwd()}")
		for file in os.listdir():
			try:
				size = os.path.getsize(file)
				os.remove(file)

				global_mb += int(size)
				print(f"{w}[{Fore.RESET}+{w}] {file} {size} кб ")
			except Exception:
				print(f"{w}[{Fore.RESET}-{w}] {file} {size} кб")
		print(f"Очищенно: {global_mb}мб")

	elif choose == 2:
		xl = 0
		def delete(path):
			os.chdir(path)
			print(f"{w}[{Fore.RESET}!{w}] {os.getcwd()}")
			for file in os.listdir():
				try:
					size = os.path.getsize(file)
					os.remove(file)

					xl += int(size)
					print(f"{w}[{Fore.RESET}+{w}] {file} {size} кб ")
				except Exception:
					print(f"{w}[{Fore.RESET}-{w}] {file} {size} кб")
		delete('C:\Windows\Logs\WindowsUpdate')
		delete(f'C:/ProgramData/USOShared/Logs/System')
		delete(f'C:\Windows\SoftwareDistribution\DataStore\Logs')
	else:
		global_mb = 0

		def delall():
			inp = input('Чистить? y - да, n - нет: ')
			if inp == "y":
				for i in os.listdir():
					try:
						os.remove(i)
						global_mb += 1
					except:
						pass
			else:
				pass


		
		os.chdir(rf"C:/Users/{getpass.getuser()}/Downloads")
		print()
		print(f"{w}[{Fore.RESET}!{w}] {os.getcwd()}")
		delall()
		os.chdir(fr"C:\Windows\SoftwareDistribution\DataStore\Logs")
		print()
		print(f"{w}[{Fore.RESET}!{w}] {os.getcwd()}")
		delall()
		os.chdir(r"C:\Windows\Temp")
		delall()
		print()
		print(f"{w}[{Fore.RESET}!{w}] {os.getcwd()}")
		delall()
		os.chdir(r'C:\Windows\Logs\WindowsUpdate')
		print()
		print(f"{w}[{Fore.RESET}!{w}] {os.getcwd()}")
		delall()

		os.chdir(fr"C:/ProgramData/USOShared/Logs/System")
		print()
		print(f"{w}[{Fore.RESET}!{w}] {os.getcwd()}")
		delall()
		os.chdir(fr"{os.getenv('temp')}")
		print()
		print(f"{w}[{Fore.RESET}!{w}] {os.getcwd()}")
		delall()
		print(f"Очищенно: {global_mb} файлов")



