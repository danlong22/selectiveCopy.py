#selectiveCopy.py - walks through a folder tree and searches for files with a certain file extension 
#(such as .pdf or .jpg) and Copies these files from whatever location they are in to a new folder.
#usage:
	#move this program into the file that you wish to find all the .docx files from
	#all docx files will be copied to a folder called 'docx'

import os, shutil


print('Please be patient, human. I am working as fast as I can.')

#make the 'docx' folder if it doesn't already exist
try:
	os.mkdir('docx')
except:
	pass

#walk the folder tree
for folderName, subfolders, filenames in os.walk('./'):
	for filename in filenames:
		#find the .docx files
		if filename.endswith('.docx'):
			filename = os.path.abspath(os.path.join(folderName, filename))

			#deal with the files that are in the main folder rather than one of the subfolders
			try:
				shutil.copy(filename, 'docx')
			
			except shutil.SameFileError:
				pass
		
