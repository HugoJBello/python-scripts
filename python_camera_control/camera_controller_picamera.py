import platform
import datetime
import time
import os

class CameraControllerPicamera:

	def __init__(self,base_dir):
		self._filename = ""
		self._path = ""
		self.base_dir =base_dir
		self.initial_path ="/home/pi/Documents/"


	def take_a_shot(self):


		date=str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

		self.filename = self.clean_filename(date)+ ".png"
		self.path = self.base_dir + self.filename

		print("trying to take a shoot")

		#os.system("raspistill -o " + self.path)
		#os.system("raspistill -w 640 -h 480 -q 75 -o " + self.path)
		os.system("raspistill -w 640 -h 480 -q 50 -o " + self.path)
		print("image saved locally as " + self.path)

	def clean_filename(self,text):
		return "".join(x for x in text if (x.isalnum() or x in "_- "))
