![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=HCI_entertainment&fontSize=90)  
<img src="https://img.shields.io/badge/Python-02569B?style=for-the-badge&logo=Python&logoColor=white">

# **🌱** Getting Started

## **⚙️** 설치

- 해당 프로젝트를 Local 환경에 clone 받아야 합니다.

```python
$ git clone https://github.com/YeJi222/HCI_entertainment.git
```

- 다운 받은 프로젝트의 generate&totalCode디렉토리에 있는 marker_3624.png 이미지를 그대로 사용하셔도 되고,   
새로운 aruco marker를 다운받아도 됩니다.
(aruco marker 생성 방법)   
```
$ cd generate&totalCode
$ python3 ar_markers_generate.py
```

## **🎶** 코드 실행  

- 통합 코드 실행(left, right, back, front 기능)    
```
$ python3 ar_markers_scan.py -c [camera id] -f
$ python3 ar_markers_scan.py -c 1 -f
```

- 엑셀 & 기어 코드 실행(accel_gear.py)    
```
$ python3 accel_gear.py
```

- 핸들 코드 실행(handle.py)    
```
$ python3 handle.py
```

## **👀** Usage  
1. 게임 실행(Real Driver Legend of the City)   
<img width="600" alt="image" src="https://github.com/YeJi222/HCI_entertainment/assets/70511859/e94f2849-7323-42c8-ae3d-e233a8845a3d">

2. accel_gear.py 실행(엑셀, 기어 인식)    
<img width="400" alt="image" src="https://github.com/YeJi222/HCI_entertainment/assets/70511859/3ebb6ad4-58ef-44e6-8675-8c9fcb9306d9">
<img width="400" alt="image" src="https://github.com/YeJi222/HCI_entertainment/assets/70511859/1c46196a-0c72-41be-a646-131722b34ff6">

3. handle.py 실행(핸들 인식)      
<img width="450" alt="image" src="https://github.com/YeJi222/HCI_entertainment/assets/70511859/480500cf-1da4-4aae-9b4e-94323bc4820f">

4. aruco marker를 카메라 3대에 인식시켜 게임을 할 수 있습니다.      
4-1. aruco marker 이미지를 정면 카메라(핸들 - left/right)에 인식시켜 핸들 방향 조절       
4-2. aruco marker 이미지를 발 밑 카메라(엑셀)에 인식시켜 엑셀 밟기       
4-3. aruco marker 이미지를 사이드 카메라(기어 - front/back)에 인식시켜 기어 방향 조절       

🚧 엑셀과 기어를 동시에 인식시켜야 작동됩니다. EX) 엑셀 + front : 앞으로, 엑셀 + back : 뒤로 🚧    

## Reference
[오픈소스 링크]   
https://github.com/MomsFriendlyRobotCompany/ar_markers   
https://github.com/Aviral09/SteeringWheel   

[참고 글]   
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=chandong83&logNo=221291349712
