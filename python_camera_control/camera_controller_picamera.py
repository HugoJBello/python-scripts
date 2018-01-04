import platform
import datetime
import time
import os

class CameraControllerPicamera:

	def __init__(self):
		self._filename = ""
		self._path = ""
		self.path_remote ="/media/pi/PINCHO/"
		self.initial_path_windows = "C:/users/hugo/Documents/"
		self.initial_path ="/media/pi/7589-EFC6/"

	def take_a_shot(self):


		date=str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

		self.filename = self.clean_filename(date)+ ".png"
		if (platform.system()=='Windows'):
			self.path = self.initial_path_windows + self.filename
		else:
			self.path = self.initial_path + self.filename

		print("trying to take a shoot")

		#os.system("raspistill -o " + self.path)
		#os.system("raspistill -w 640 -h 480 -q 75 -o " + self.path)
		os.system("raspistill -w 640 -h 480 -q 50 -o " + self.path)
		print("image saved locally as " + self.path)

		self.path_remote = self.path_remote + self.filename

	def clean_filename(self,text):
		return "".join(x for x in text if (x.isalnum() or x in "_- "))
