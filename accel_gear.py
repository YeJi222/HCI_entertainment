'''
    Accel & Gear Code using MultiThread
    
    Accel Camera - #0
    Gear Camera - #1
'''

from __future__ import print_function
import sys
import time
import numpy as np
import imutils
import keyboard
import threading
import queue

try:
	import cv2
	from ar_markers import detect_markers
except ImportError:
	raise Exception('Error: OpenCv is not installed')

prevTime = time.time()

def on_key_event(event):
    print(f"Key {event.name} was {event.event_type}")

def camera_first(capture, q, accelQ, accelFlag):
    frame_captured, frame = capture.read();
    
    if frame_captured:
        markers = detect_markers(frame)
        centerX = 0
        centerY = 0
        
        for marker in markers:
            marker.highlite_marker(frame)
            centerX = marker.center[0]
            centerY = marker.center[1]
            # print("camera1 coordinate", centerX, centerY)
            
            if 650 < centerX < 1220 and 60 < centerY < 745: # accel
                accelFlag = 1
            else:
                accelFlag = 0
		
        # print("accel Flag in camera_first", accelFlag)
        accelQ.put(accelFlag)
		
        frame_captured, frame = capture.read()
        frame = np.flip(frame, axis=1)
        frame = imutils.resize(frame, width=650)
        frame = imutils.resize(frame, height=480)
	
        height = frame.shape[0]
        width = frame.shape[1]
	
        frame = cv2.rectangle(frame,(width//3,0),(width//3 + 300 ,height//3+ 200),(255,255,255),3)
        cv2.putText(frame,'Accel',(400,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)

        q.put(frame)
    
def camera_second(capture2, q2, accelFlag):
    frame_captured, frame = capture2.read();
    
    if frame_captured:
        markers = detect_markers(frame)
        centerX = 0
        # centerY = 0
        
        for marker in markers:
            marker.highlite_marker(frame)
            centerX = marker.center[0]
            # centerY = marker.center[1]
            # print("camera2 coordinate", centerX)
            
            if centerX > 1025 and accelFlag == 1: # front
                keyboard.press('w')
                print("Front")
            else:
                keyboard.release('w')
            if centerX < 890 and accelFlag == 1: # back
                keyboard.release('w')
                keyboard.press('s')
                print("Back")
            else:
                keyboard.release('s')
		
        frame_captured, frame = capture2.read()
        frame = np.flip(frame, axis=1)
        frame = imutils.resize(frame, width=650)
        frame = imutils.resize(frame, height=480)
	
        height = frame.shape[0]
        width = frame.shape[1]
        
        frame = cv2.rectangle(frame,(0,0),(width//2- 10,height),(255,255,255),3)
        cv2.putText(frame,'FRONT',(160,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)
        
        frame = cv2.rectangle(frame,(width//2 + 10,0),(width-2,height),(255,255,255),3)
        cv2.putText(frame,'BACK',(width - width//4- 20,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)
		
        q2.put(frame)

if __name__ == '__main__':
	cam_id = 0
	argv = sys.argv

	cam_id = int(argv[2]) # cam_id 0 => camera1 - Accel
	cam_id2 = cam_id + 1; # cam_id 1 => camera2 - Gear
 
	capture = cv2.VideoCapture(cam_id)
	capture2 = cv2.VideoCapture(cam_id2)
 
	accelFlag = 0
	q = queue.Queue()
	q2 = queue.Queue()
	accelQ = queue.Queue()
	accelQ.put(0)
    
	while 1:
		accelFlag = accelQ.get()
		# print("accel", accelFlag)
        
		thread_1 = threading.Thread(target = camera_first, args=(capture, q, accelQ, 0))
		thread_2 = threading.Thread(target = camera_second, args=(capture2, q2, accelFlag))
	
		thread_1.start()
		thread_2.start()
  
		frame = q.get()
		frame2 = q2.get()
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

		cv2.imshow('Camera1 - Accel', frame)
		cv2.imshow('Camera2 - Gear', frame2)
  
		thread_1.join()
		thread_2.join()
		
	# When everything done, release the capture
	capture.release()
	capture2.release()
	cv2.destroyAllWindows()