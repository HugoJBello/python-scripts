
# pip install opencv-python
from camera_controller_opencv import CameraControllerOpencv
from camera_controller_picamera import CameraControllerPicamera

from database_inserter import DatabaseInserter
from ssh_sender import SshSender
import time, threading


# you need the mysql python adapter:
# pip install mysqlclient-1.3.12-cp36-cp36m-win32.whl
#  https://pypi.python.org/pypi/MySQL-python/


def capture_and_send(sftp):
	wait = 40
	try:
		#cameraController = CameraControllerOpencv()
		cameraController = CameraControllerPicamera()
		cameraController.take_a_shot()

		filename = cameraController.filename
		path = cameraController.path
		path_remote = cameraController.path_remote

		try:
			sftp.put(path,path_remote)
			databaseInserter = DatabaseInserter()
			databaseInserter.save(path_remote,filename)
		except:
			print("error")

		print("waiting " + str(wait) + "seconds")
		time.sleep(wait)
	except:
		print("an error ocurred, it will be atempted again")
	threading.Timer(wait, capture_and_send(sftp)).start()

def main():
	sshSender = SshSender()
	sftp = sshSender.obtain_client()
	capture_and_send(sftp)



if __name__ == '__main__':
	main()
