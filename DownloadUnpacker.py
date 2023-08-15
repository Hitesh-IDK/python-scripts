import os
import shutil

def get_download_path():

	if os.path.exists(os.path.join(os.path.expanduser('~'), 'downloads')):
		return os.path.join(os.path.expanduser('~'), 'downloads')
	elif os.path.exists(os.path.join('D:\\', 'downloads')):
		return os.path.join('D:\\', 'downloads')
	else:
		tries = 3
		while tries > 0:
			print('Unable to locate your downloads folder...')
			print('Please locate your downloads folder and copy paste the file path here')
			print('Tip: Right click on your downloads folder and click copy path and paste it here')

			input_path = input('File Path: ')
			if os.path.exists(input_path):
				return input_path
			elif tries == 1:
				print('Too many attempts!')
				print('Rerun the script after you confirm your downloads path')
				tries -= 1
			else:
				print('File path is invalid!')
				tries -= 1

def unpacker(download_path):
	#Sub folders and folders
	folders = ('Documents', 'Media', 'Zip Folders', 'Installers', 'Others')
	media_folder = ('Photos', 'Videos', 'Audio')

	folders = os.listdir(download_path)

	print(f'Starting unpacking at: {download_path}')
	for folder in folders:
		folder_path = os.path.join(download_path, folder)

		if os.path.isdir(folder_path):
			if folder in folders:
				print(f'\tUnpacking {folder}....')

				if folder == 'Media':
					for media_type in media_folder:
						media_path = os.path.join(folder_path, media_type)

						if os.path.exists(media_path):
							media_files = os.listdir(media_path)

							for media_file in media_files:
								media_file_path = os.path.join(media_path, media_file)
								shutil.move(media_file_path, download_path)

				elif folder == 'Others':
					other_files_path = os.path.join(folder_path, 'Files')

					if os.path.exists(other_files_path):
						other_files = os.listdir(other_files_path)

						for other_file in other_files:
							other_file_path = os.path.join(other_files_path, other_file)
							shutil.move(other_file_path, download_path)

					other_directories = os.listdir(folder_path)

					for directory in other_directories:
						if directory != 'Files':
							directory_path = os.path.join(folder_path, directory)
							shutil.move(directory_path, download_path)

				else:
					files = os.listdir(folder_path)

					for file in files:
						file_path = os.path.join(folder_path, file)
						shutil.move(file_path, download_path)

def main():

	#Download path
	download_path = get_download_path()

	#Start unpacking
	unpacker(download_path)

if __name__ == '__main__':
	try:
		main()
	except:
		print('Something went wrong!')
		print('Exiting the program!!')
	else:
		print('Unpacking successful!')
