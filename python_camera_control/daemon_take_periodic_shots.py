
# pip install opencv-python
from camera_controller_opencv import CameraControllerOpencv
from database_inserter import DatabaseInserter
from ssh_sender import SshSender



# you need the mysql python adapter:
# pip install mysqlclient-1.3.12-cp36-cp36m-win32.whl
#  https://pypi.python.org/pypi/MySQL-python/

filename = ""
path = ""


	
def send_ssh():
	print("W")
	
def main():

	cameraController = CameraControllerOpencv()
	cameraController.take_a_shot()
	filename = cameraController.filename
	path = cameraController.path
	
	databaseInserter = DatabaseInserter()
	databaseInserter.save(path,filename)
	
	sshSender = SshSender()
	sshSender.send(path)
	


if __name__ == '__main__':
 main()
