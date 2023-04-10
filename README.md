![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=HCI_entertainment&fontSize=90)  
<img src="https://img.shields.io/badge/Python-02569B?style=for-the-badge&logo=Python&logoColor=white">

# **🌱** Getting Started

## **⚙️** 설치

- 해당 프로젝트를 Local 환경에 clone 받아야 합니다.

```python
$ git clone https://github.com/YeJi222/HCI_entertainment.git
```

- 다운 받은 프로젝트에 marker_3624.png 이미지를 그대로 사용하셔도 되고, 새로운 aruco marker를 다운받아도 됩니다.
(aruco marker 생성 방법)   
```
$ python ar_markers_generate.py
```

- 실행
```
$ python3 ar_markers_scan.py -c 1 -f
```

## 👀 Usage
<img width="60%" alt="image" src="https://user-images.githubusercontent.com/70511859/230760005-9a600fed-53c5-4f6e-bab6-43984298ea16.png"><br>  
1. 게임과 파이썬 코드를 실행시킨다.
2. aruco marker 이미지를 카메라에 인식시켜 게임을 할 수 있다.
3. left, right, drift, back 기능을 사용할 수 있으며, back을 제외한 키들은 앞으로 가는 키와 동시에 눌린다. 

## Reference
[오픈소스 링크]   
https://github.com/MomsFriendlyRobotCompany/ar_markers   
https://github.com/Aviral09/SteeringWheel   

[참고 글]   
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=chandong83&logNo=221291349712
