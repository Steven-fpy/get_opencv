// C++ code
//

// mode change

// pin number
int POTENTIOMETER_PIN = A0;
int BUTTON_PIN1 = 2; //mode변경
int BUTTON_PIN2 = 4; //on,off 리셋

// const
int LEDs[] = {11,10,9,6,5};
int MAX_LED = 5;
int MAX_MODE = 4;

// variable
int preButtonState1 = 0; //mode변경
int preButtonState2 = 0; //on,off 리셋

int button1PushedTime = 0;
bool changedButton1State = false;
int ledOn = 1;

int mode = 0;
//int mode = 1;

int nextOnLed = 0;
int ledState = 0;



void setup()
{
  
  //pinMode(LED_BUILTIN, OUTPUT);
  
  pinMode(POTENTIOMETER_PIN, INPUT);  
  pinMode(BUTTON_PIN1, INPUT);
  pinMode(BUTTON_PIN2, INPUT);
  
  for (int i=0; i<MAX_LED; i++){
    pinMode(LEDs[i], OUTPUT);
  }
  
  Serial.begin(9600);
}

void loop()
{
  bool reset = false;
  
  
  //------- Reset/On/Off
  
  //Reset
  int buttonState1 = digitalRead(BUTTON_PIN2);
  
  if (buttonState1 == HIGH) {
    //0->1 라이징
    if (preButtonState1 == LOW) {
      button1PushedTime = millis();
      
      //off 상태일때 눌림으로만 on
      if (!ledOn) {
        ledOn = 1;
        changedButton1State = true;
      }
    }
    
    //누르고 있는 상태
    int pushDeltaTime = millis() - button1PushedTime;
    //Serial.println(pushDeltaTime);
    
    if (changedButton1State == false && ledOn && pushDeltaTime >= 3000) {
      reset = true;
      changedButton1State = true;
      button1PushedTime = millis();
      modeReset();
    }
  }
  
  //On/Off
  //1->0 폴링
  //if (buttonState1 - preButtonState1 < 0) {
  if (buttonState1 == LOW && preButtonState1 == HIGH) {
    
    if (changedButton1State == true) {
      changedButton1State = false;
    }else{
      ledOn = 1 - ledOn;
    }
  }
  
  preButtonState1 = buttonState1;
  
  
  if (!ledOn) {
    ledAllOff(true);
    return;
  }
  
  
  //------ 모드변경
  int buttonState2 = digitalRead(BUTTON_PIN1);
  
  //Serial.println(buttonState);
  
  //0->1 라이징
  //if (buttonState2 - preButtonState2 > 0) {
  if (buttonState2 == HIGH && preButtonState2 == LOW) {
    mode = (mode + 1) % MAX_MODE;
    
    nextOnLed = 0;
    ledState = 0;
  }
  preButtonState2 = buttonState2;
  
  //Serial.print("mode: ");
  //Serial.println(mode);
  
  //Serial.print("ledOn: ");
  //Serial.println(ledOn);
  
  int potentiometerVal = analogRead(POTENTIOMETER_PIN);
  //Serial.println(potentiometerVal);
  
  switch(mode) {
    case 0:
    	
    	//mode1(potentiometerVal / 4);
    	mode1(map(potentiometerVal, 0,1023, 0,255));
    	break;
    case 1:{
    	int sensor = map(potentiometerVal, 0,1023, 100,2000);
    	//int sensor2 = mapping(potentiometerVal, 0,1023, 100,2000);
    	
    	mode2(sensor);
    	break;
    }
    case 2:
    	mode3(map(potentiometerVal, 0,1023, 100,1000));
    	break;
    case 3:
    	mode4(map(potentiometerVal, 0,1023, 100,500));
    	break;
    default:
    	break;
  }
}


long mapping(long val, long iMin, long iMax, long oMin, long oMax) {
  return (val - iMin) * (oMax - oMin) / (iMax - iMin) + oMin;
}

void ledAllOff(bool reset) {
  
  for (int i=0; i<MAX_LED; i++){
    digitalWrite(LEDs[i], LOW);
  }
  
  if (reset) {
    nextOnLed = 0;
   	ledState = 0;
  }
}

void modeReset() {
  Serial.println("modeReset()");
  
  nextOnLed = 0;
  ledState = 0;
  
  mode = 0;
}


//5개 LED 모두 켜진 상태로 디이얼로 밝기 조절
void mode1(int light) {
  //Serial.println("mode1()");
  
  /*
  if (ledState == light) {
    return;
  }
  
  ledState = light;
  Serial.println(light);
  */
  
  for (int i=0; i<MAX_LED; i++){
    analogWrite(LEDs[i], light);
  }
  delay(50);
}


//(1,3,5)->(2,4) ... 순서대로 점멸, 다이얼로 점멸 속도 조절
void mode2(int delayMS) {
  //Serial.println("mode2()");
  
  ledAllOff(false);
  
  for (int i = 0+nextOnLed; i<MAX_LED; i+=2) {
    digitalWrite(LEDs[i], HIGH);
  }
  
  //(1,3,5)->(2,4)
  nextOnLed = 1 - nextOnLed;
  
  /*
  if (ledState >= 1) {
    //(1,3,5)->(2,4)
  	nextOnLed = 1 - nextOnLed;
  }

  ledState = 1 - ledState;
  */

  delay(delayMS);
  
}

//1->2->3->4->5->1 ... 순서대로 이동, 다이얼로 이동속도 조절
void mode3(int delayMS) {
  //Serial.println("mode3()");
  
  ledAllOff(false);
  
  digitalWrite(LEDs[nextOnLed], HIGH);
  //1->2->3->4->5->1
  nextOnLed = (nextOnLed + 1) % MAX_LED;
  
  /*
  digitalWrite(LEDs[nextOnLed], ledState);
  
  if (ledState) {
    //1->2->3->4->5->1
  	nextOnLed = (nextOnLed + 1) % MAX_LED;
  }
  
  ledState = 1 - ledState;
  */
  
  delay(delayMS);
  
}

//1->3->5->2->4->1 ...
void mode4(int delayMS) {
  
  ledAllOff(false);
  
  digitalWrite(LEDs[nextOnLed], HIGH);
  //1->3->5->2->4->1 ...
  nextOnLed = (nextOnLed + 2) % MAX_LED;
  
  /*
  digitalWrite(LEDs[nextOnLed], ledState);

  if (ledState) {
    //1->3->5->2->4->1 ...
  	nextOnLed = (nextOnLed + 2) % MAX_LED;
  }
  ledState = 1 - ledState;
  */
  
  delay(delayMS);
 
}
