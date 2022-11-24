

//1. 징비 3개가 각각 구현되어서 동작확인
//2. 서보모터 동작확인
//3. mode 값에 따른 지정된 장비가 동작하는지 확인
//4. 버튼을 눌렀을때 mode 값이 변경되는지 확인
//5. 잘 섞어서 구현

const int MAX_MODE_NUM = 3;
const int BUTTON_PIN = 2;
int mode = -1;
int increase = 1; // 1, -1

void act1() {
  //초음파

  //구현
  //거리를 구하고, 출력
}

void act2() {
  //부저

  //소리를 발생
  //켜고 끄고
}

void act3() {

  //led

  //빛을 내고 끄고
}

void servoAct(int angle) {

  //해당 각도로 서보 모터가 동작

  servo.write(angle);
}

void buttonPressed() {
    
  //TODO 모드 변경
  //mode++;
//  if(mode == MAX_MODE_NUM-1) {
//    increase = -1;
//  }else if (mode == 0) {
//    increase = 1;
//  }
  
  mode = (mode + increase) % MAX_MODE_NUM;
  // 시작 mode -1;
  // mode = (-1 + 1) % 3; // 0
  
  // mode = (0 + 1) % 3; // 1
  // mode = (1 + 1) % 3; // 2
  // mode = (2 + 1) % 3; // 0 초기화
  
}

void setup() {
  //TODO 장비 1,2,3 설정
  

  //버튼 인터럽트 설정
  attachInterrupt(digitalPinToInterrupt(BUTTON_PIN), buttonPressed, RISING);

}

void loop() {

//  if (digitalRead(BUTTON_PIN) == 1) {
//    //모드 변경
//    mode = (mode + increase) % MAX_MODE_NUM;
//    delay(500);
//  }

  //현재 mode 값을 참고로 지정된 동작을 실행 (장비 구동 및 서보모터 각도 변경)
  switch(mode) {
    case 0:
      act1();
      servoAct(0);
//      servo.write(0);
      break;

    case 1:
      act2();
      servoAct(90);
      break;

    case 2:
      act3();
      servoAct(180);
      break;

    default:
      break;
  }

}
