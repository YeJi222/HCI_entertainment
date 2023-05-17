from __future__ import print_function
import sys, getopt
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

def putFps(img): # fps 표시 
	global prevTime
	curTime = time.time()
	sec = curTime - prevTime
	prevTime = curTime
	fps_val = 1/(sec)
	fps_txt = "%01.f" % fps_val
	cv2.putText(img, fps_txt, (0, 25), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0))

def camera_first(cam_id, capture, q):
    # print("camera 1")
    # print("cam_id : " + str(cam_id))
    
    # capture = cv2.VideoCapture(cam_id)
    frame_captured, frame = capture.read();
    
    # print(frame_captured)
    
    if frame_captured:
        markers = detect_markers(frame)
        centerX = 0
        centerY = 0
        
        # print(centerX, centerY)
        
        for marker in markers:
            marker.highlite_marker(frame)
            centerX = marker.center[0]
            centerY = marker.center[1]
            
            # print("camera1 coordinate", centerX, centerY)
            
            if 650 < centerX < 1245 and 30 < centerY < 780: # accel
                # keyboard.press('a')
                # print(centerX, centerY)
                print("Excel")
            else:
                print()
                # keyboard.release('a')

			# print(centerX, centerY);
			# print("detect!")
		
		
        frame_captured, frame = capture.read()
        frame = np.flip(frame, axis=1)
        frame = imutils.resize(frame, width=650)
        frame = imutils.resize(frame, height=480)
	
        height = frame.shape[0]
        width = frame.shape[1]
	
        frame = cv2.rectangle(frame,(width//3,0),(width//3 + 300 ,height//3+ 200),(255,255,255),3)
		# cv2.putText(frame,'LEFT',(160,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)

        # cv2.imshow('Camera1', frame)
        q.put(frame)
    
    return frame;
    
    
def camera_second(cam_id, capture, q2):
    # print("camera 2")
    # print("cam_id : " + str(cam_id))
    frame_captured, frame = capture.read();
    
    # print(frame_captured)
    
    if frame_captured:
        markers = detect_markers(frame)
        centerX = 0
        centerY = 0
        
        # print(centerX, centerY)
        
        for marker in markers:
            marker.highlite_marker(frame)
            centerX = marker.center[0]
            centerY = marker.center[1]
            
            print("camera2 coordinate", centerX, centerY)
            
            if centerX < 356 and centerY < 460: # left
                keyboard.press('a')
                print("Left")
            else:
                keyboard.release('a')
                
            if centerX > 496 and centerY < 460: # right
                keyboard.press('d')
                print("Right")
            else:
                keyboard.release('d')

			# print(centerX, centerY);
			# print("detect!")
		
		
        frame_captured, frame = capture.read()
        frame = np.flip(frame, axis=1)
        frame = imutils.resize(frame, width=650)
        frame = imutils.resize(frame, height=480)
	
        height = frame.shape[0]
        width = frame.shape[1]
		
        frame = cv2.rectangle(frame,(0,0),(width//2- 50, height),(255,255,255),3)
        cv2.putText(frame,'LEFT',(160,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)
		
        frame = cv2.rectangle(frame,(width//2 + 50,0),(width-2, height),(255,255,255),3)
        cv2.putText(frame,'RIGHT',(width - width//4- 20,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)
 
        q2.put(frame)
        
    # print("Second Camera")

if __name__ == '__main__':
	cam_id = 0 #default 0
	argv = sys.argv

	print('Press "q" to quit')
	print('cam_id : ', argv[2])
	cam_id = int(argv[2])
	cam_id2 = cam_id + 1;
	cam_id3 = cam_id + 2;
 
	capture = cv2.VideoCapture(cam_id)
	capture2 = cv2.VideoCapture(cam_id2)
	# capture3 = cv2.VideoCapture(cam_id3)
 
	frame_captured, frame = capture.read();
	
	q = queue.Queue()
	q2 = queue.Queue()
 
	while frame_captured:
		thread_1 = threading.Thread(target = camera_first, args=(cam_id, capture, q))
		thread_2 = threading.Thread(target = camera_second, args=(cam_id, capture, q2))
		# thread_3 = threading.Thread(target = camera_third)
	
		thread_1.start()
		thread_2.start()
		# thread_3.start()
	
		
  
		frame = q.get()
		frame2 = q2.get()
		# print(type(frame))
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

		cv2.imshow('Camera1', frame)
		cv2.imshow('Camera2', frame2)
  
		# 'q' 키를 누르면 종료
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
  
		thread_1.join()
		thread_2.join()
		# thread_3.join()
     
     
		# frame_captured, frame = capture.read();
		#frame_captured2, frame2 = capture2.read()
  
      
		
	# When everything done, release the capture
	capture.release()
	# capture2.release()
	cv2.destroyAllWindows()