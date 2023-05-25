'''
    Handle Code
    
    Handle Camera - #2
'''

from __future__ import print_function
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
	print('Handle Code')
 
	cam_id = 2 # handle camera - #2
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
			
			if centerX < 338 and centerY < 460: # left
				keyboard.press('a')
				keyboard.press('w')
				print("Left")
			else:
				# keyboard.press('w')
				keyboard.release('a')
			
			if centerX > 514 and centerY < 460: # right
				keyboard.press('d')
				keyboard.press('w')
				print("Right")
			else:
				# keyboard.press('w')
				keyboard.release('d')
   
			# print(centerX, centerY);
		cv2.imshow('Camera3 - Handle', frame)
  
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		frame_captured, frame = capture.read()
		frame = np.flip(frame, axis=1)
		frame = imutils.resize(frame, width=650)
		frame = imutils.resize(frame, height=480)
    
		height = frame.shape[0]
		width = frame.shape[1]
    
		frame = cv2.rectangle(frame,(0,0),(width//2 - 70, height),(255,255,255),3)
		cv2.putText(frame,'LEFT',(160,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)
    
		frame = cv2.rectangle(frame,(width//2 + 70,0),(width-2, height),(255,255,255),3)
		cv2.putText(frame,'RIGHT',(width - width//4- 20,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)
        
	# When everything done, release the capture
	capture.release()
	cv2.destroyAllWindows()