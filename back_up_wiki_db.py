# you need the mysql python adapter:
# pip install mysqlclient-1.3.12-cp36-cp36m-win32.whl
#  https://pypi.python.org/pypi/MySQL-python/

import MySQLdb
import base64

def connect_db():
	return MySQLdb.connect(host="localhost",     # your host, usually localhost
			    			user="root",         # your username
							passwd="",           # your password
							db="my_wiki")        # name of the data base

def extract_pages(db):
	cur_pages = db.cursor()
	cur_pages.execute('select CONVERT(p.page_title USING utf8), CONVERT(t.old_text USING utf8) FROM text t, revision r, page p WHERE  p.page_latest = r.rev_id AND t.old_id =r.rev_text_id')
	return cur_pages.fetchall()
	
def clean_filename(text):
	return "".join(x for x in text if (x.isalnum() or x in "._- "))

class WikiPage:
	title=''
	text=''
	date=''

def save_file(wiki_page):
	file_name = str(wiki_page.title) + '.txt'
	file_name = clean_filename(file_name)
	text_file = open(file_name, 'w')
	text_file.write(str(wiki_page.text))
	
def main():
	db=connect_db()

	for row in extract_pages(db):
		wiki_page = WikiPage()
		wiki_page.title = row[0]
		wiki_page.text=row[1]	
		save_file(wiki_page)
	db.close()

if __name__ == '__main__':
  main()

