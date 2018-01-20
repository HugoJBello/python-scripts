
# pip install opencv-python
from camera_controller_opencv import CameraControllerOpencv
#from camera_controller_picamera import CameraControllerPicamera
from rest_sender import RestSender

# from database_inserter import DatabaseInserter
# from ssh_sender import SshSender
import time, threading


# you need the mysql python adapter:
# pip install mysqlclient-1.3.12-cp36-cp36m-win32.whl
#  https://pypi.python.org/pypi/MySQL-python/


def capture_and_send():
	wait = 40
	try:
		cameraController = CameraControllerOpencv()
		#cameraController = CameraControllerPicamera()
		cameraController.take_a_shot()

		filename = cameraController.filename
		full_path = cameraController.path

		try:
			restSender = RestSender()
			restSender.send_shot(filename,full_path)			
		except:
			print("error")

		print("waiting " + str(wait) + "seconds")
		time.sleep(wait)
	except:
		print("an error ocurred, it will be atempted again")
	threading.Timer(wait, capture_and_send()).start()

def main():
	capture_and_send()



if __name__ == '__main__':
	main()
