# selectiveCopy.py
Assignment from Automate the Boring Stuff with Python chapter 9
Copies all of the .docx files from the folder and subfolders of the folder it is located into a folder called "docx".

Had to put in try-except statements to deal with SameFileErrors that come up whenever the script tries to copy anything from the main directory as opposed to one of the subfolders. 

Aggregating all the diles makes it easier to decide what to delete so I added the seekAndDestroy.py script to find and delete unwanted files. 
