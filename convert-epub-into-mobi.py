# requires calibre to be instaled.
# usage: paste the .py file inside the folder that contains the .epub files, then just run
# python ----.py and it will rename the .epub files to obtain clean names nad then it will
# convert them to .mobi files using the command ebook-convert.


def is_epub (filename):
	aux = filename.split(".")
	return aux[len(aux)-1] == "epub"


def remove_extension (filename):
	aux = filename.split(".")
	new_filename=""
	for i in range(0, len(aux)-1): new_filename = new_filename + aux[i]
	return new_filename


import re
import os


def clean_filename (filename):
	  return "".join([c for c in filename if re.match(r'(\w|\_|\.)', c)])




def rename_cleaning_filename (filename):
	os.rename(filename,clean_filename(filename))


	
for filename in os.listdir("."):
	if is_epub(filename):
		rename_cleaning_filename(filename)
		os.system("ebook-convert " + filename + " " + remove_extension(filename) + ".mobi")