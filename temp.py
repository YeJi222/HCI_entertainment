from __future__ import print_function
import sys, getopt
import time
import numpy as np
import imutils
import keyboard
import threading
import pygame

try:
	import cv2
	from ar_markers import detect_markers
except ImportError:
	raise Exception('Error: OpenCv is not installed')

prevTime = time.time()

def on_key_event(event):
    print(f"Key {event.unicode} was {event.type}")
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            keyboard.press('a')
        elif event.key == pygame.K_d:
            keyboard.press('d')
        elif event.key == pygame.K_w:
            keyboard.press('w')
        elif event.key == pygame.K_s:
            keyboard.press('s')
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            keyboard.release('a')
        elif event.key == pygame.K_d:
            keyboard.release('d')
        elif event.key == pygame.K_w:
            keyboard.release('w')
        elif event.key == pygame.K_s:
            keyboard.release('s')

def putFps(img): # fps 표시 
	global prevTime
	curTime = time.time()
	sec = curTime - prevTime
	prevTime = curTime
	fps_val = 1/(sec)
	fps_txt = "%01.f" % fps_val
	cv2.putText(img, fps_txt, (0, 25), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0))
 

def process_frames(capture, frame):
    while True:
        frame_captured, frame[:] = capture.read()
        if not frame_captured:
            break
        markers = detect_markers(frame)
        centerX = 0
        centerY = 0
        for marker in markers:
            marker.highlite_marker(frame)
            centerX = marker.center[0];
            centerY = marker.center[1];
            if centerX < 355 and centerY < 220: # left
                print("Left")
            else:
                print("Release Left")
            if centerX > 497 and centerY < 220: # right
                print("Right")
            else:
                print("Release Right")
            if centerX > 389 and centerX < 600 and centerY > 374: # Back
                print("Back")
            else:
                print("Release Back")
            if centerX > 642 and centerY > 374: # Front
                print("Front")
            else:
                print("Release Front")
        putFps(frame)
        frame = np.flip(frame, axis=1)
        frame = imutils.resize(frame, width=650)
        frame = imutils.resize(frame, height=480)
        height = frame.shape[0]
        width = frame.shape[1]
        frame = cv2.rectangle(frame,(0,0),(width//2- 
