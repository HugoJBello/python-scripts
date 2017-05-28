# requieres mutagen: pip install mutagen
# see http://code.activestate.com/recipes/577138-embed-lyrics-into-mp3-files-using-mutagen-uslt-tag/
# see http://stackoverflow.com/questions/4040605/does-anyone-have-good-examples-of-using-mutagen-to-write-files

import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2

def clean_filename(filename):
	keepcharacters = (' ','.','-','_')
	return "".join(c for c in filename if c.isalnum() or c in keepcharacters).rstrip()


def rename_cleaning_filename(filename):
	os.rename(filename, clean_filename(filename))

def extension(filename):
	return '.' + filename.split('.')[len(filename.split('.'))-1]
	
def remove_extension(filename):
	return filename.split(extension(filename))[0]

for filename in os.listdir('.'):
		rename_cleaning_filename(filename)

music_folder = os.path.dirname(os.path.realpath(__file__))

for root, subdirs, files in os.walk(music_folder):
	for file in files:
		filename = os.path.join(root, file)
		if (extension(file) != '.py'):
			tags = ID3(filename)
			print('Changing title of ' + filename + ' to ' + remove_extension(file))
			tags["TIT2"] = TIT2(encoding=3, text = remove_extension(file))
			tags.save(filename)