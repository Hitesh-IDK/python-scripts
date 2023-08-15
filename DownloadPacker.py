#Read all files and folders in the downloads folder
#But before that locate the downloads folder
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

def check_folders(download_path):
	#Locating Documents, Media, Zip Folders, Others, Installers directories in the downloads path
	folders = ('Documents', 'Media', 'Zip Folders', 'Installers', 'Others')
	media_folder = ('Photos', 'Videos', 'Audio')

	#Check for folders
	print('Checking if folders already exist...')
	for folder in folders:
		print(f'\tLooking for {folder}...')

		#If folders dont exits, create them
		folder_path = os.path.join(download_path, folder)
		if not os.path.exists(os.path.join(download_path, folder)):
			print(f'\tCreating a new {folder} folder...')
			os.mkdir(folder_path)

			#If media folder doesnt exist, create sub folders in media
			if folder == 'Media':
				for media_type in media_folder:
					media_type_path = os.path.join(folder_path, media_type)
					os.mkdir(media_type_path)

			if folder == 'Others':
				os.mkdir(os.path.join(folder_path, 'Files'))

		#If media exists, check if sub folders in media exist
		elif folder == 'Media':
			print('\tChecking for sub folders in media....')
			for media_type in media_folder:
					media_type_path = os.path.join(folder_path, media_type)
					if not os.path.exists(media_type_path):
						print(f'\t\tCreating a new {media_type} sub folder...')
						os.mkdir(media_type_path)

		#If Others exist, check if Files sub folder exists
		elif folder == 'Others':
			print('\tChecking for Files sub folder in others...')
			other_file_path = os.path.join(folder_path, 'Files')
			print(other_file_path)
			if not os.path.exists(other_file_path):
				print(f'\t\tCreating a new Files sub folder...')
				os.mkdir(other_file_path)

#If folders are ready, start moving the files and folders
def downloads_organizer(download_path):
	#Sort everything except these, sort into these folders
	#Formats
	#Document formats
	doc_formats = ['.DOC', '.DOCX', '.ODT', '.PDF', '.XLS', '.XLSX', '.ODS', '.PPT', '.PPTX','.TXT']
	#Photo formats
	photo_formats = ['.JPEG', '.JPG', '.GIF', '.PNG', '.WEBP', '.HEIF', '.AVIF', '.TIFF', '.TIF', '.BMP']
	#Video formats
	video_formats = ['.MP4', '.MOV', '.WMV', '.AVI', '.AVCHD', '.MKV', '.WEBM', '.MPEG-2']
	#Audio Formats
	audio_formats = ['.PCM', '.WAV', '.AIFF', '.MP3', '.AAC']

	folders = ('Documents', 'Media', 'Zip Folders', 'Installers', 'Others')
	media_folder = ('Photos', 'Videos', 'Audio')

	#Accessing the folder
	download_folder = os.listdir(download_path)

	print(f'Accessing the files at:  {download_path}')
	print('-'*40)
	print('-'*40)

	for file in download_folder:
		print(file)
		#Get file path
		file_path = os.path.join(download_path, file)
		print(f'File: {file_path}')

		#If its our folders
		if file in folders:
			continue

		#If its a file
		elif os.path.isfile(file_path):
			#get the extension first
			file_name, file_extension = os.path.splitext(file)
			print(f'File Extension: {file_extension}')

			#Check for extensions now
			
			#Zip files
			if file_extension == '.zip':
				new_file_path = os.path.join(download_path, 'Zip Folders')
				print(f'Moving to: {new_file_path}')
				shutil.move(file_path, new_file_path)

			#Document files
			elif file_extension.upper() in doc_formats:
				new_file_path = os.path.join(download_path, 'Documents')
				print(f'Moving to: {new_file_path}')
				shutil.move(file_path, new_file_path)

			#Installers
			elif file_extension == '.exe':
				new_file_path = os.path.join(download_path, 'Installers')
				print(f'Moving to: {new_file_path}')
				shutil.move(file_path, new_file_path)

			#Media - Photos
			elif file_extension.upper() in photo_formats:
				new_file_path = os.path.join(download_path, 'Media', 'Photos')
				print(f'Moving to: {new_file_path}')
				shutil.move(file_path, new_file_path)

			#Media - Videos
			elif file_extension.upper() in video_formats:
				new_file_path = os.path.join(download_path, 'Media', 'Videos')
				print(f'Moving to: {new_file_path}')
				shutil.move(file_path, new_file_path)

			#Media - Audios
			elif file_extension.upper() in audio_formats:
				new_file_path = os.path.join(download_path, 'Media', 'Audio')
				print(f'Moving to: {new_file_path}')
				shutil.move(file_path, new_file_path)

			#Others - files
			else:
				new_file_path = os.path.join(download_path, 'Others', 'Files')
				print(f'Moving to: {new_file_path}')
				shutil.move(file_path, new_file_path)

		#Check if directory, if not leave it in downloads
		elif os.path.isdir(file_path):
			new_file_path = os.path.join(download_path, 'Others')
			print(f'Moving to: {new_file_path}')
			shutil.move(file_path, new_file_path)

		print()

#Main function for proper order
def main():

	download_path = get_download_path()
	#If download path was invalid
	if type(download_path) == type(None):
		return;

	#We now have download path
	#Check for folders
	check_folders(download_path)

	#If folders exist, start moving the files
	downloads_organizer(download_path)
	

if __name__ == '__main__':
	# try:
	# 	main()
	# except:
	# 	print('Something went wrong on the way!')
	# else:
	# 	print('\nDownload Packer ran successfully!')
	main()