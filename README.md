### 221104

- self._likes = self._ydl_info.get('like_count',0)
- self._dislikes = self._ydl_info.get('dislike_count')
- pafy/backend_youtube_dl.py 54번째줄 수정

### 221107

- 213 ~ 215
- 301 ~ 302 
- singleton
- README.md 
- 생성 및 업데이트

### 221108

- 301 ~ 308 : 도형출력
- 308까지 생성
- polylines 는 int 형을 지원한다.

### 221109

- 우분투 밀고 40Gb 로 잡아서 다시 설치
- 설치 후 여분의 용량이 확보되어 자잘한 오류 제거됨
- 수 번의 삽질과 반복끝에 정상작동 확인
- 401~406 까지 진도 나감
- 407 작성

### 221110

- 412까지 작성

### 221111

- 4단원 전부작성
- 504 까지 작성
- Threshold

### 221114
	
- 506까지 작성
- 꽃, 닭 예제 풀이

### 221115

- 카드게임

### 221116

- 509까지 작성
- 실행
- 히스토그램, 제로데이, 임계값 등등...

### 221117

- 전체 상담
- 과제 
- cv2.inrange
- 열화상 값 검사 코드예제
- burn_series

### 221118

- 열화상 값 풀이
- star 게임 작성
- return, def, 변수의 위치 등등의 중요성

### 221121

- pulldown 방식으로 스위치를 1개 구성하고, LED를 1개 구성하여, 스위치가 눌려있을 때 LED 불이 켜지고, 스위치가 열려있을 때 LED 불이 꺼지게 한다.
- 이때 스위치와 LED 신호는 독립적이다.
- 결국 스위치는 digitalread, LED 는 digitalwrite 이다.

### 221122

- Arduino Extension 설치
- Tinkercad 이용하여 Arduino 회로 구성
- pullup, pulldown 생성
- 빌드
- 실행

### 221124

- 509 ~ 516 생성
- 빌드
- 실행

### 221125

- 601, 602, 609~612 작성
- 빌드
- 실행

### 221128

- 707까지 작성
- 빌드
- 실행

### 221129

- 711까지 작성
- 빌드
- 실행
- watershed 함수
	- 최저점에 물 흘리기 
- webcam을 이용한 윤곽선 제어
- 700 작성
- 빌드

- 7012-2TT

### 221130

- 714까지 작성
- 빌드
- 실행

### 221201

- 802까지 작성
- HTTP 폴더 생성
- 소켓 통신 클라이언트 및 서버 생성
- 빌드
- 실행

### 221202

- Flask 모듈 설치
	- 가상환경에서 pip install Flask

- applicaltion.py, hello.html 생성
- 빌드
- 실행
	- application.py 를 실행하여 주소를 불러온 후
	- 실행하면 웹페이지에 hello.html에 작성된 내용이 출력된다.
	- html를 잘 이용 못할 경우, atom, notion등을 이용할 수 있다.

- 실행 에러를 잡으려면 추가 설치한 익스텐션을 중지시키거나 삭제하고 다시 해본다. 
- 그래도 에러가 날경우 설치한 모듈을 다시 설치해보고 VSCODE를 재실행해보고 안되면 재부팅도 해본다.
- 그래도 안된다면...다시 설치

### 221205

- H bridge 
	- 트랜지스터 4개로 모터의 회전방향을 조절할 수 있다.
		- 4개의 신호를 통하여 조절
	- 모양이 H 모양이어서 H bridge 이다.
		- (H-bridge_221205.png 참조) 
	- 속도 조절은 PWM을 통해 신호를 주었다 뺐다를 반복하여 조절가능
		-(불을 껐다 켰다를 반복하여 밝기를 조절 하는 느낌)
	+ >>━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━
			S1 ┫┃		      ┃┠ S3
				┣━━━━━━ M ━━━━━┫
			S2 ┫┃		      ┃┠ S4
	- >>━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━
	- S1이 S4랑 짝이다.
	- S2와 S3가 짝이다.

- epoch : 학습 주기, 반복 사이클
- batch size : 현재 가지고 있는 데이터를 그룹단위로 묶은 것

- EX )  1000개의 자료를 100 batchsize로 5 epoch 만큼 학습시면
	-	10개의 그룹이 나오고 5번 반복 사이클이므로  50번 반복한다.


### 221206

- media pipe

### OpenCv
- opencv 패키지 설치
- 파이썬 3.10 설치
- matplotlib 설치
- 0201~0212.py 생성
- 빌드 
- 실행

### 221107
- () 확인 잘하기
- 경로 확인 잘하기
- 한글 경로는 피하기

### 221109

- pip install --upgrade pip
- pip install opencv-contrib-python
- 실행이 안되면 업그레이드를 하고 실행해보자

### 221110

- droidcam 설치
- SUBSYSTEM=="usb",ATTR{idVendor}=="04e8",MODE="0666",GROUP="plugdev"

### 221116

- 전수조사

	- 모든 항목을 전부 검사하는것
	- 예를 들어 3가지 항목이 있을 시(최대값이 5일 때)
	- 1 1 1 > 1 1 2 > 1 1 3 .....1 1 5 > 1 2 1 > 1 2 2 ...
	- 1 2 5 > 1 3 1 ...... 2 1 1 > 2 1 2 .... 4 5 5 > 5 1 1 
	- ..... 5 5 4 > 5 5 5 까지 검사하는 것 

- 재귀함수

	- 자기 자신을 호출하는 함수
	- 추적이 어렵고 해석이 어렵다
	- 사용하면 이점은 있으나 사용을 자제하는 편이 좋다고 한다


### 221121

- pull - up 방식 : 스위치가 눌리지 않았을때 전류가 통하는 것   ==   1
- pull -down 방식 : 스위치가 눌리지 않았을때 전류가 안통하는 것   ==  0


### 221128

- 평균필터 : 실시간으로 샘플값을 수집하고 그 값의 평균을 구하는 것으로, 노이즈를 제거하여
			실제에 가까운 값을 알아내는 방법, 측정치에 떨림이 있다. (예측치 이기때문)
- 칼만필터 -> 로켓의 연료 온도 외부측정, GPS로 터널을 지나는 자동차의 
			위치값을 산출

- 이동 평균필터 : 평균을 낼 샘플의 갯수를 지정된 수로 유지 (유지된 원소는 가장 최신 샘플)

- ex)  [1,2,3,4,5,6,7,8,9,10,] ->[2,3,4,5,6,7,8,9,10,11]
	-> [3,4,5,6,7,8,9,10,11,12]...이런식으로 최신화 (10개가 최대일 때)
	- 파이썬에서 pop 이용 

- 미분은 변화량을 파악한다.
- 미분필터 : 변화량이 급격하게 변화하는 지점을 파악 
	- 사각형을 파악할때 0 --> 1 되었을 지점이 경계면
	- 221128_미분관련.png 참조

### 230131

- openCv 클론한뒤에 자식 브렌치 만들기
	- git checkout -b [사용할 브렌치 네임]
	- (git chegit checkout -b openCv_sb)

### 230201

- 뷰티파이 질문하기

### 230202

- 0001.py f 스트링 방식으로 수정
- git fetch origin
	- git 패치하기 : 변동사항 있는지 확인
- git pull origin 'branch name'
	- 브랜치명의 내용 가져오기 
- git stash
	- 임시저장
- git stash pop
	- 임시저장 가져오기
- git stash save "name"
	- 이름 붙여서 임시저장
- git stash list
	- 임시저장 목록확인
- git stash apply stash@{0}
	- 이름붙인 임시저장 가져오기
	* window는 git stash apply 'stash@{0}'

* git conflict 발생시
	- git checkout main
		- main 브렌치로 이동
	- git pull main
		- main의 최신화
	- git checkout '충돌브렌치이름'
		- 충돌 브렌치로 이동
	- git merge main
		- main 과 merge하기
		- 충돌한 부분을 알려준다
	- 충돌한 파일 수정
	- git add, commit, push, pull request 진행
	- main, master 가 변경되면 다시 충돌이 일어날수 있다.

### 230203

- GAN 공부
	- mnist

### 230206

- deeplearning 관련 서적 주문
- python 관련서적 주문
- 포트폴리오 수정및 보완

### 230207

- 뷰티파이
	- 영역 지정한 후 ctrl + shift + b
	* 간격등이 보기 좋게 바뀐다
	* 단! 파이썬에 사용시 주의 해야 한다
- git reset --soft HEAD^    (최근 커밋 하기전으로 돌림)
- git reset --hard HEAD^    (최근 커밋과 스테이징 파일변경 등을 수정하기전으로 돌림(변경이 불가하다))
- git reset HEAD~1          (커밋 실행 취소 (수량~1,2,3...))
- git log                   (log 보기)
- git log --oneline         (log 한줄로 간략히 보기)
- github 에서 글씨중간에 줄이 그어져 있는경우 code임을 명시해 줘야 한다.
	- 수정을 통해 변경
	
- conflicts 해결과 cherry-pick 연습
    - main_light.ino 수정
    - conflict 는 먼저 알맞는 부모 브렌치를 풀 하고 작업을 시작하면 안생기나, 혹여 발생시 틀린 부분을 알맞게 수정하주고 다시 커밋한다
    * cherry-pick은 풀해온 브렌치에 여러개의 커밋이 있을떄 특정 부분의 커밋만 가져올 경우 사용한다
        - git cherry-pick [커밋해시]
            - 커밋 뒤에 해시부분을 복사해서 넣으면 된다.
            - ex) [git cherry-pick c886c1054eb2c32b02cc64a6bda26821af685f39]

### 230209
- revert

### 230210

- stash 할때 git stash 했을 경우 git stash pop을 하게되면 임시저장을 가져옴과 동시에 stash 가 사라져 버리니 필요한 경우 stash 에 라벨을 붙여준다

- unreal을 사용할 경우 3080 정도는 써야 버겁게 돌아가지 않는다고함, 2080을 사용하는 경우 최초 부팅하는 로딩에 10분 가량 걸린다고 한다

### 230213

- IOT 관련 서적 열람 및 학습

- Lidar 통관완료


### 230214

- 드론 일방적인 취소
- 아두이노 나노 배송완료
- 실드 배송완료

### 230215

- Lidar 2ea 수령
- Lidar 관련 자료 검색
	- https://www.youtube.com/watch?v=4sQCz75BfrM
	- 라이다 시연영상
	
	- https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=chandong83&logNo=221254131929
	- 라이다 아두이노 연결
	- https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=chandong83&logNo=221293021042
	- 라이다 간단 연결

	- https://remnant24c.tistory.com/218
	- 라이다 관련 자료

	- https://www.youtube.com/watch?v=VhbFbxyOI1k
	- 드론봇 워크샾 영상

	- https://www.youtube.com/watch?v=6S_fffMb8C8
	- 라이다 맵핑

	- https://www.boannews.com/media/view.asp?idx=92797&kind=
	- Lidar와 IOT의 위험성

	- https://kocoafab.cc/make/view/751
	- 모빌리티 코드 참조

### 230216

- Lidar 코드
	- https://www.cygbot.com/downloads
	- 타업체 코드

### 230217

- 대여도서 반납
	- IOT로 하는 사물인터넷 : 2017년 발간으로 전용 아두이노 키트가 필요함, 그 외에 JAVA를 이용한 게임 만들기 밑 스크래치를 이용한 코딩 등이 기재되어있음

	- 딥러닝과 머신러닝 : 2017년 발간 도서로 다양한 내용이 수록되어 있음
	  openCV를 이용한 딥러닝 keras, tensorflow, 
	  mnist 등 다양한 내용이 전부 들어 있어 종합적인 지식을 얻기에는 좋다

### 230220

- Deep learning study

### 230222

- LIDAR sensor test 

- https://blog.naver.com/roboholic84/221740028135
	- 라이다 아두이노 코드

### 230223

- LiDAR 관련 자료조사

### 230224

- 로보락 LiDAR 센서 관련 자료수집
- 아두이노 프로젝트 구상 및 스케치

### 230227

- buzzer_230227.ino 생성

### 230228

- 아두이노 buzzer remind 및 연구
- LiDAR 센서 모터 동작확인
- git_test 리포지토리로 이동시켜 실습
- 광센서 연구
	- light_sensor.ino, light_sensor_led.ino