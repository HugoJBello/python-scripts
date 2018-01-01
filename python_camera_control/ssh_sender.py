import pysftp
#pip install pysftp

class SshSender:

	dir="/home/pi/Documents"
	
	def send(self,path):
		srv = pysftp.Connection("", username="", password="")
		srv.cd(dir)            # temporarily chdir to public
		srv.put(path)  # upload file to public/ on remote
			
		