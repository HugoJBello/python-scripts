import cv2
# pip install opencv-python

import datetime

class CameraControllerOpencv:
	
	def __init__(self):
		self._filename = ""
		self._path = ""
	
	initial_path = "C:/users/hugo/Documents/"
	
	def take_a_shot(self):
		camera_port = 0
		ramp_frames = 30
		camera = cv2.VideoCapture(camera_port)
		
		retval, im = camera.read()
		for i in range(ramp_frames):
			temp = self.get_image(camera)
		print("Taking image...")
		
		camera_capture = self.get_image(camera)
		date=str(datetime.datetime.now())
		
		self.filename = self.clean_filename(date)+ ".png"
		self.path = "C:/users/hugo/Documents/"+ self.filename
		cv2.imwrite(self.path, camera_capture)
		del(camera)

	def get_image(self,camera):
		# read is the easiest way to get a full image out of a VideoCapture object.
		retval, im = camera.read()
		return im
		
	def clean_filename(self,text):
		return "".join(x for x in text if (x.isalnum() or x in "._- "))