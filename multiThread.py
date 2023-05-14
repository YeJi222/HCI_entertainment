from __future__ import print_function
import sys, getopt
import time
import numpy as np
import imutils
import keyboard
import threading

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

def camera_first():
    print("camera 1")
    print("cam_id : " + str(cam_id))
    for i in range(5):
        print(str(i) + " first")
        time.sleep(0.5)
    print("First Camera")
    
    
def camera_second():
    print("camera 2")
    print("cam_id : " + str(cam_id))
    for i in range(5):
        print(str(i) + " second")
        time.sleep(1)
    print("First Camera")
    
def camera_third():
    print("camera 3")
    print("cam_id : " + str(cam_id))
    for i in range(5):
        print(str(i)+ " third")
        time.sleep(1.5)
    print("Third Camera")

if __name__ == '__main__':
	cam_id = 0 #default 0
	argv = sys.argv
 
	print("main function start")
 
	

 
	# camera_first()
	# camera_second()
	# camera_third()
	
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
	cam_id2 = cam_id + 1;
	cam_id3 = cam_id + 2;
 
	thread_1 = threading.Thread(target = camera_first)
	thread_2 = threading.Thread(target = camera_second)
	thread_3 = threading.Thread(target = camera_third)
 
	thread_1.start()
	thread_2.start()
	thread_3.start()
 
	thread_1.join()
	thread_2.join()
	thread_3.join()
 
	capture = cv2.VideoCapture(cam_id)
	capture2 = cv2.VideoCapture(cam_id2)
	# capture3 = cv2.VideoCapture(cam_id3)
 
	while True:
		frame_captured, frame = capture.read();
		frame_captured2, frame2 = capture2.read()
  
		if frame_captured:
			markers = detect_markers(frame)
			centerX = 0
			centerY = 0
	
			for marker in markers:
				
				marker.highlite_marker(frame)
				centerX = marker.center[0]
				centerY = marker.center[1]
    
				print("camera1", centerX, centerY)
				
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
   
			cv2.imshow('Camera1', frame)
      
		if frame_captured2:
			markers = detect_markers(frame2)
			centerX2 = 0
			centerY2 = 0
	
			for marker in markers:
				
				marker.highlite_marker(frame2)
				centerX2 = marker.center[0];
				centerY2 = marker.center[1];
				
				if centerX2 < 356 and centerY2 < 460: # left
					keyboard.press('a')
					print("Left")
				else:
					keyboard.release('a')
				
				if centerX2 > 496 and centerY2 < 460: # right
					keyboard.press('d')
					print("Right")
				else:
					keyboard.release('d')
	
				# print(centerX, centerY);
			#cv2.imshow('Test Frame', frame2)
	
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
			frame_captured2, frame2 = capture2.read()
			frame2 = np.flip(frame2, axis=1)
			frame2 = imutils.resize(frame2, width=650)
			frame2 = imutils.resize(frame2, height=480)
		
			height = frame2.shape[0]
			width = frame2.shape[1]
		
			frame2 = cv2.rectangle(frame2,(0,0),(width//2- 50, height),(255,255,255),3)
			cv2.putText(frame2,'LEFT',(160,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)
		
			frame2 = cv2.rectangle(frame2,(width//2 + 50,0),(width-2, height),(255,255,255),3)
			cv2.putText(frame2,'RIGHT',(width - width//4- 20,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)
			cv2.imshow("Camera 2", frame2)
   
		if cv2.waitKey(1) == ord('q'):
			break;
 
	"""
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
      
      """
        
	# if capture2.isOpened():  # try to get the first frame
	# 	frame_captured2, frame2 = capture2.read()
	# else:
	# 	frame_captured2 = False
	# while frame_captured2:
	# 	markers = detect_markers(frame2)
	# 	centerX = 0
	# 	centerY = 0
  
	# 	for marker in markers:
			
	# 		marker.highlite_marker(frame2)
	# 		centerX = marker.center[0];
	# 		centerY = marker.center[1];
			
	# 		if centerX < 356 and centerY < 460: # left
	# 			keyboard.press('a')
	# 			print("Left")
	# 		else:
	# 			keyboard.release('a')
			
	# 		if centerX > 496 and centerY < 460: # right
	# 			keyboard.press('d')
	# 			print("Right")
	# 		else:
	# 			keyboard.release('d')
   
	# 		# print(centerX, centerY);
	# 	cv2.imshow('Test Frame', frame2)
  
	# 	if cv2.waitKey(1) & 0xFF == ord('q'):
	# 		break
	# 	frame_captured2, frame2 = capture2.read()
	# 	frame2 = np.flip(frame2, axis=1)
	# 	frame2 = imutils.resize(frame2, width=650)
	# 	frame2 = imutils.resize(frame2, height=480)
    
	# 	height = frame2.shape[0]
	# 	width = frame2.shape[1]
    
	# 	frame2 = cv2.rectangle(frame2,(0,0),(width//2- 50, height),(255,255,255),3)
	# 	cv2.putText(frame2,'LEFT',(160,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)
    
	# 	frame2 = cv2.rectangle(frame2,(width//2 + 50,0),(width-2, height),(255,255,255),3)
	# 	cv2.putText(frame2,'RIGHT',(width - width//4- 20,30),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255), 2)
        
	# When everything done, release the capture
	capture.release()
	capture2.release()
	cv2.destroyAllWindows()