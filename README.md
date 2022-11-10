## 221104

	- self._likes = self._ydl_info.get('like_count',0)
	- self._dislikes = self._ydl_info.get('dislike_count')
	- pafy/backend_youtube_dl.py 54번째줄 수정

# 221107

	- 213 ~ 215
	- 301 ~ 302 
	- singleton
	- README.md 
	- 생성 및 업데이트

# 221108

	- 301 ~ 308 : 도형출력
	- 308까지 생성
	- polylines 는 int 형을 지원한다.

# 221109

	- 우분투 밀고 40Gb 로 잡아서 다시 설치
	- 설치 후 여분의 용량이 확보되어 자잘한 오류 제거됨
	- 수 번의 삽질과 반복끝에 정상작동 확인
	- 401~406 까지 진도 나감
	- 407 작성

# 221110

	- 412까지 작성

## OpenCv
	- opencv 패키지 설치
	- 파이썬 3.10 설치
	- matplotlib 설치
	- 0201~0212.py 생성
	- 빌드 
	- 실행

# MEMO

## 221107
	- () 확인 잘하기
	- 경로 확인 잘하기
	- 한글 경로는 피하기

## 221109

	- pip install --upgrade pip
	- pip install opencv-contrib-python
	- 실행이 안되면 업그레이드를 하고 실행해보자

## 221110

	- droidcam 설치
	- SUBSYSTEM=="usb",ATTR{idVendor}=="04e8",MODE="0666",GROUP="plugdev"