import MySQLdb
#pip install mysqlclient

class DatabaseInserter:

	def connect_db(self):
		return MySQLdb.connect(host="localhost",   # your host, usually localhost
							user="root",                 # your username
							passwd="",           # your password
							db="picam_app")                # name of the data base

	def save(self,path,filename):
		print("inserting in database the file " + filename)
		db=self.connect_db()
		x = db.cursor()
		sql = 'insert into image (date_taken,path,filename) values (sysdate(),"' + path + '","' + filename + '");'
		try:
			x.execute(sql)
			row = x.fetchall()
			db.commit()
		except:
			db.rollback()
		db.close()
