import cv2
# pip install opencv-python
# pip2 install opencv-python
import platform
import datetime
class CameraControllerOpencv:

	def __init__(self,base_dir):
		self._filename = ""
		self._path = ""
		self.base_dir =base_dir
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
		self.path = self.base_dir + self.filename

		cv2.imwrite(self.path, camera_capture)
		print("image saved locally as " + self.path)

		del(camera)

	def get_image(self,camera):
		retval, im = camera.read()
		return im

	def clean_filename(self,text):
		return "".join(x for x in text if (x.isalnum() or x in "_-"))
