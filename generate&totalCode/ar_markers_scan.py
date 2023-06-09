from __future__ import print_function
import sys, getopt
import time
import numpy as np
import imutils
import keyboard

try:
	import cv2
	from ar_markers import detect_markers
except ImportError:
	raise Exception('Error: OpenCv is not installed')

prevTime = time.time()

def on_key_event(event):
    print(f"Key {event.name} was {event.event_type}")

def putFps(img): # fps 표시 
	global prevTime
	curTime = time.time()
	sec = curTime - prevTime
	prevTime = curTime
	fps_val = 1/(sec)
	fps_txt = "%01.f" % fps_val
	cv2.putText(img, fps_txt, (0, 25), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0))

if __name__ == '__main__':
	cam_id = 0 #default 0
	argv = sys.argv
	# print(argv)
	
	# try:
	# 	opts, args = getopt.getopt(argv,"hc:f",["camera_id="])
	# except:
	# 	print('default setting : cam id = 0, fps indication = disabled')
    
	# for opt, arg in opts:
	# 	if opt == '-h':
	# 		print('test.py -c <camera_id> -f')
	# 		sys.exit()
	# 	elif opt in ("-c", "--camera"):
	# 		cam_id = int(arg)
            
	print('Press "q" to quit')
	print('cam_id : ', argv[2])
	cam_id = int(argv[2])
	capture = cv2.VideoCapture(cam_id)
 
	if capture.isOpened():  # try to get the first frame
		frame_captured, frame = capture.read()
	else:
		frame_captured = False
	while frame_captured:
		markers = detect_markers(frame)
		centerX = 0
		centerY = 0
  
		for marker in markers:
			
			marker.highlite_marker(frame)
			centerX = marker.center[0];
			centerY = marker.center[1];
			
			if centerX < 355 and centerY < 220: # left
				keyboard.press('a')
				print("Left")
			else:
				keyboard.release('a')
			
			if centerX > 497 and centerY < 220: # right
				keyboard.press('d')
				print("Right")
			else:
				keyboard.release('d')
    
			if centerX > 389 and centerX < 600 and centerY > 374: # Back
				keyboard.release('w')
				keyboard.press('s')
				print("Back")
			else:
				keyboard.release('s')
    
			if centerX > 642 and centerY > 374: # Front
				keyboard.press('w')
				print("Front")
			else:
				keyboard.release('w')
   
			# print(centerX, centerY);
			# print("detect!")
		cv2.imshow('Test Frame', frame)
  
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		frame_captured, frame = capture.read()
		frame = np.flip(frame, axis=1)
		frame = imutils.resize(frame, width=650)
		frame = imutils.resize(frame, height=480)
    
		height = frame.shape[0]
		width = frame.shape[1]
    
		frame = cv2.rectangle(frame,(0,0),(width//2- 50,height//2 ),(255,255,255),3)
		cv2.putText(frame,'LEFT',(160,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)
    
		frame = cv2.rectangle(frame,(width//2 + 50,0),(width-2,height//2 ),(255,255,255),3)
		cv2.putText(frame,'RIGHT',(width - width//4- 20,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)

		frame = cv2.rectangle(frame,(2*(width//5) + 35,3*(height//4)),(3*width//4 - 25,height),(255,255,255),3)
		cv2.putText(frame,'BACK',(2*(width//5) + 120,height-10),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),2)
  
		frame = cv2.rectangle(frame,(width//2+ 200, 3*(height//4)),(width,height),(255,255,255),3)
		cv2.putText(frame,'FRONT',(width - width//6 - 15,height-10),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),2)
        
	# When everything done, release the capture
	capture.release()
	cv2.destroyAllWindows()