
# pip install opencv-python
import cv2

# you need the mysql python adapter:
# pip install mysqlclient-1.3.12-cp36-cp36m-win32.whl
#  https://pypi.python.org/pypi/MySQL-python/
import MySQLdb

def new_image_name():

def take_a_shot():
	camera_port = 0
	ramp_frames = 30
	camera = cv2.VideoCapture(camera_port)

	retval, im = camera.read()
	for i in range(ramp_frames):
	 temp = im
	print("Taking image...")

	camera_capture = get_image()
	file = "C:/users/hugo/Documents/test_image.png" # new_image_name()

	cv2.imwrite(file, camera_capture)
	del(camera)

def save_in_database():

def send_ssh():

def main():


if __name__ == '__main__':
  main()
