import paramiko
#pip install pysftp
#pip3 install pysftp

class SshSender:

	def __init__(self):
		self.dir="/home/pi/Documents"


	def obtain_client(self):
		sftp = None
		host = ''
		port = 22
		username = ''
		keyfile_path = None
		password = ''
		transport = None

		try:
			transport = paramiko.Transport((host, port))
			transport.connect(None, username, password, None)
			sftp = paramiko.SFTPClient.from_transport(transport)
			return sftp
		except:
			print("error")
			if sftp is not None:
				sftp.close()
			if transport is not None:
				transport.close()
			pass
