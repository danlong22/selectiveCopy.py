#seekAndDestroy.py - deletes files in a specified folder, and elsewhere in the directory
#usage:
	#create a folder called 'hitlist' in the directory this script is located in
	#move files you want deleted into the 'trash' folder. This script will delete the 
	#files from the 'hitlist' folder, and from the current working directory and it's subfolders

import os, shutil, send2trash

print('*beep* *boop* ready to seek and destory unwanted files, human.')
#find files in 'hitlist'
os.chdir('hitlist')
filesToDelete = []
for filename in os.listdir():
	filesToDelete.append(filename)
os.chdir('../')

#find and delete from cwd and subdirectories

#walk the folder tree
for fileToDelete in filesToDelete:
	for folderName, subfolders, filenames in os.walk('./'):
		for filename in filenames:
			#find the .docx files
			if filename == fileToDelete:
				filename = os.path.abspath(os.path.join(folderName, filename))
				try:
					shutil.move(filename, 'trash')
					#send2trash.send2trash(filename)
					print(filename+ ' has been terminated')
				except: 
					print('I was unable to terminate ' + filename)
					pass

				
		
