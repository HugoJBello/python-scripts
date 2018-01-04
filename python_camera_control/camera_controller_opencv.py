import cv2
# pip install opencv-python
# pip2 install opencv-python
import platform
import datetime

class CameraControllerOpencv:

	def __init__(self):
		self._filename = ""
		self._path = ""
		self.path_remote ="/media/pi/PINCHO/"
		self.initial_path_windows = "C:/users/hugo/Documents/"
		self.initial_path ="/home/pi/Documents/"

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
		if (platform.system()=='Windows'):
			self.path = self.initial_path_windows + self.filename
		else:
			self.path = self.initial_path + self.filename
		print("image saved locally as " + self.path)

		self.path_remote = self.path_remote + self.filename
		cv2.imwrite(self.path, camera_capture)
		del(camera)

	def get_image(self,camera):
		# read is the easiest way to get a full image out of a VideoCapture object.
		retval, im = camera.read()
		return im

	def clean_filename(self,text):
		return "".join(x for x in text if (x.isalnum() or x in "_-"))
