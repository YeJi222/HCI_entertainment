import tkinter as tk
import cv2 as cv
import threading
from PIL import Image
from PIL import ImageTk


def capture(camera_num, label):
    cap = cv.VideoCapture(camera_num)
    while True:
        ret, frame = cap.read()
        if ret:
            # OpenCV에서 가져온 이미지를 Tkinter Label에 표시하기 위해 적절한 형식으로 변환
            cv_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv_image)
            tk_image = ImageTk.PhotoImage(image=pil_image)

            # Tkinter Label 업데이트
            label.config(image=tk_image)
            label.image = tk_image

        if cv.waitKeyEx(1) == ord('q'):
            break

def capture2(camera_num, label):
    cap = cv.VideoCapture(camera_num)
    while True:
        ret, frame = cap.read()
        if ret:
            # OpenCV에서 가져온 이미지를 Tkinter Label에 표시하기 위해 적절한 형식으로 변환
            cv_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv_image)
            tk_image = ImageTk.PhotoImage(image=pil_image)

            # Tkinter Label 업데이트
            label.config(image=tk_image)
            label.image = tk_image

        if cv.waitKeyEx(1) == ord('q'):
            break

def start_cameras():
    # GUI 생성
    root = tk.Tk()
    root.title("Cameras")
    root.geometry("800x600")

    # 왼쪽 카메라를 위한 Label
    label1 = tk.Label(root)
    label1.pack(side=tk.LEFT, padx=10, pady=10)

    # 오른쪽 카메라를 위한 Label
    label2 = tk.Label(root)
    label2.pack(side=tk.RIGHT, padx=10, pady=10)

    # 각 카메라에 대한 스레드 생성
    thread1 = threading.Thread(target=capture, args=(0, label1))
    thread2 = threading.Thread(target=capture2, args=(1, label2))

    # 스레드 시작
    thread1.start()
    thread2.start()

    # GUI 메인 루프 실행
    root.mainloop()

    # 스레드 종료 대기
    # thread1.join()
    # thread2.join()


if __name__ == '__main__':
    start_cameras()
