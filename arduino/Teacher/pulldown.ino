// C++ code
//

// pulldown


int POTENTIOMETER_PIN = A0;
int PWM_LED_PIN = 3;



int BUTTON_PIN = 2;
int LEDs[] = {7,6,5,4};

int lastMode = 0;
int mode = 0;

int lastButtonState = 0;

void setup()
{
  
  //pinMode(LED_BUILTIN, OUTPUT);
  
  pinMode(POTENTIOMETER_PIN, INPUT);
  pinMode(PWM_LED_PIN, OUTPUT);
  
  
  pinMode(BUTTON_PIN, INPUT);
  
  for (int i=0; i<4; i++){
    pinMode(LEDs[i], OUTPUT);
  }
  
  Serial.begin(9600);
}

void loop()
{
  //ADC 10bit ->  2^10 -> 0~1023 (1024)
  int potentiometerVal = analogRead(POTENTIOMETER_PIN);
  //Serial.println(potentiometerVal);
  
  //map(val, min, max, toMin, toMax)
  
  //PWM 8bit 2^8 256 0~255
  analogWrite(PWM_LED_PIN, potentiometerVal / 4);
  
  //256 % 255 = 1
  //analogWrite(PWM_LED_PIN, potentiometerVal);
  
  
  // LOW, HIGH
  int buttonState = digitalRead(BUTTON_PIN);
  //Serial.println(buttonState);
  
  //이전에 버튼이 떼어진 상태에서 처음 누른 상태가 되었을때
  if (buttonState == HIGH && lastButtonState == LOW) {
    
    //현재 켜져있는 led 번호를 기억
    lastMode = mode;
    
    // mode 값이 최대 값을 넘어가면 다시 0으로 초기화
    
    // 나머지 연산 사용
    mode = (mode + 1) % 4;
    
    
    //조건식 사용
    //mode++;
    //if (mode >= 4) {
    //  mode = 0;
    //}
    
    //if (mode >= 4) mode = 0;
    
    //mode = mode >= 4 ? 0 : mode;
      
  }
  
  lastButtonState = buttonState;
  
  //Serial.println(mode);
  
  
  //모든 led를 끈다
  //for (int i=0; i<4; i++) {
  //  digitalWrite(LEDs[i], LOW);
  //}
  
  //이전에 켜있던 led를 끈다
  digitalWrite(LEDs[lastMode], LOW);
  
  //현재 켜야할 led를 켠다
  digitalWrite(LEDs[mode], HIGH);
  
  //digitalWrite(LED_BUILTIN, mode);
 
  
}