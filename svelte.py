# Libraries.
from colorama import *
import os

def main():
	# Dependencies.

	try:
		file = open('/usr/bin/node')
		file.close()

	except FileNotFoundError:
		print('Node is not Installed!')

	try:
		file = open('/usr/bin/npm')
		file.close()

	except FileNotFoundError:
		print('npm is not Installed!')
		exit()

	os.system('clear')

	print(Fore.YELLOW + 'Svelte App Generator (SAG)\n' + Fore.RESET)
	print(Fore.YELLOW + '1.' + Fore.RESET + ' Installation Via Zip\n')
	print(Fore.YELLOW + '2.' + Fore.RESET + ' Online Installation' + Fore.YELLOW + ' [Recomended!]\n')
	print(Fore.YELLOW + '3.' + Fore.RESET + ' Exit\n')

	while True:
		try:
			option = int(input('Choose an option' + Fore.YELLOW + ': ' + Fore.RESET))

			while option < 1 or option > 3:
				print(Fore.RED + '[!]' + Fore.RESET + 'Incorrect Number, please try again...' + Fore.RESET)
				option = int(input('Choose an option' + Fore.YELLOW + ': ' + Fore.RESET))
			break

		except ValueError:
			pass

	if option == 1:
		# Zip Option.
		print(Fore.RED + '[!]' + Fore.RESET + ' Warning: The npm installation is required an internet connection.')
		print(Fore.YELLOW + '[?]' + Fore.RESET + ' Directory Example' + Fore.YELLOW + ': /home/yourusername/folder' + Fore.RESET)

		directory_offline = input('Directory' +  Fore.YELLOW + ': ' + Fore.RESET)
		name_program = input('Name' + Fore.YELLOW + ': ' + Fore.RESET)

		os.system('cd ' + directory_offline + ' && unzip template.zip && mv template-master ' + name_program)
		print(Fore.YELLOW + '[?]' + Fore.RESET + ' Ctrl + c to Stop.')
		os.system('cd ' + name_program + '/ && npm install && npm run dev')

	if option == 2:
		# Online Option.
		print(Fore.YELLOW + '[?]' + Fore.RESET + ' Directory Example' + Fore.YELLOW + ': /home/yourusername/folder' + Fore.RESET)

		directory_online = input('Directory' + Fore.YELLOW + ': ' + Fore.RESET)
		name_program = input('Name' + Fore.YELLOW + ': ' + Fore.RESET)

		os.system('cd ' + directory_online)
		os.system('npx degit sveltejs/template ' + name_program)
		print(Fore.YELLOW + '[?]' + Fore.RESET + ' Ctrl + c to Stop.')
		os.system('cd ' + name_program + '/' + ' && npm install && npm run dev')

main()
