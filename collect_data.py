import cv2
import os
import sys
#import picamera


#initialize the camera
#picam  = picamera.PiCamera()

camera = cv2.VideoCapture(0)
if not camera.isOpened():
	print ("Cannot open camera")
frame_width  = 480
frame_height = 640
ret = camera.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
ret = camera.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

#create data path
DATA_PATH = 'images'
def createPath(path):
	try:
		os.mkdir(path)
	except FileExistsError:
		pass

createPath(DATA_PATH)
counter = [0, 0, 0, 0, 0, 0]


while True:
	save_path = DATA_PATH
	#read frame from the camera
	ret, frame = camera.read()

	#end if cant read frame from the camera
	if not ret:
		print('Fail to read frame from the camera')
		break

	#flip Horizon
	frame = cv2.flip(frame, 1)

	#create roi
	roi =frame[40:(frame_height - 40), 40:(frame_width - 40)]

	#mark ROI(Region of Interest
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame, "{}x{}".format(frame_width,frame_height),(10,20), font,1,(0,255,0))
	cv2.rectangle(frame, (40,40), (frame_width - 40,frame_height - 40), (0,255,0))

	#display to the monitor
	cv2.imshow("PiCamera", frame)

	#classify data 
	key = cv2.waitKey(10)
	if key == ord('0'):
		counter[0]+=1
		save_path = os.path.join(DATA_PATH, "zero")
		createPath(save_path)
		save_path = os.path.join(save_path, "{}.jpg".format(counter[0]))
	elif key == ord('1'):
		counter[1]+=1
		save_path = os.path.join(DATA_PATH, "one")
		createPath(save_path)
		save_path = os.path.join(save_path, "{}.jpg".format(counter[1]))
	elif key == ord('2'):
		counter[2]+=1
		save_path = os.path.join(DATA_PATH, "two")
		createPath(save_path)
		save_path = os.path.join(save_path, "{}.jpg".format(counter[2]))
	elif key == ord('3'):
		counter[3]+=1
		save_path = os.path.join(DATA_PATH, "three")
		createPath(save_path)
		save_path = os.path.join(save_path, "{}.jpg".format(counter[3]))
	elif key == ord('4'):
		counter[4]+=1
		save_path = os.path.join(DATA_PATH, "four")
		createPath(save_path)
		save_path = os.path.join(save_path, "{}.jpg".format(counter[4]))
	elif key == ord('5'):
		counter[5]+=1
		save_path = os.path.join(DATA_PATH, "five")
		createPath(save_path)
		save_path = os.path.join(save_path, "{}.jpg".format(counter[5]))

	#save image
	if key >= ord('0') and key < ord('6'):
		cv2.imwrite(save_path, roi)
		print("\nimage save in {}".format(save_path))
	#quit
	elif key == ord('q'):
		break

#close process
camera.release()
cv2.destroyAllWindows()
