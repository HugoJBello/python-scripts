
# pip install opencv-python
from camera_controller_opencv import CameraControllerOpencv
#from camera_controller_picamera import CameraControllerPicamera
from rest_sender import RestSender

import time, threading
import os, errno
from pathlib import Path


def capture_and_send(base_dir):
	wait = 40
	try:
		cameraController = CameraControllerOpencv(base_dir)
		#cameraController = CameraControllerPicamera(base_dir)
		cameraController.take_a_shot()

		filename = cameraController.filename
		full_path = cameraController.path

		try:
			restSender = RestSender()
			restSender.send_shot(filename,full_path)
			os.remove(full_path)			
		except:
			print("error")
			
		print("waiting " + str(wait) + "seconds")
		time.sleep(wait)
	except:
		print("an error ocurred, it will be atempted again")
		raise
	threading.Timer(wait, capture_and_send(base_dir)).start()


def create_base_directory(base_dir):
	try:
		os.makedirs(base_dir)
		print("directory " + base_dir + " created")
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise

def main():
	base_dir = str(Path.home())+"/temp_picamera/"
	create_base_directory(base_dir)
	capture_and_send(base_dir)



if __name__ == '__main__':
	main()
