// C++ code
//

// pullup

int BUTTON_PIN = 2;
int PWM_LED_PIN = 3;

int LEDs[] = {7,6,5,4};

int POTENTIOMETER_PIN = A0;

int lastMode = 0;
int mode = 0;

int lastButtonState = 0;

void setup()
{
  
  pinMode(LED_BUILTIN, OUTPUT);
  
  pinMode(PWM_LED_PIN, OUTPUT);
  
  pinMode(BUTTON_PIN, INPUT);
  pinMode(POTENTIOMETER_PIN, INPUT);
  
  for (int i=0; i<4; i++){
    pinMode(LEDs[i], OUTPUT);
  }
  
  Serial.begin(9600);
}

void loop()
{
  
  int potentiometerVal = analogRead(POTENTIOMETER_PIN);
  //Serial.println(potentiometerVal);
  
  analogWrite(PWM_LED_PIN, potentiometerVal / 4);
  
  int buttonState = digitalRead(BUTTON_PIN);
  //Serial.println(buttonState);
  
  if (buttonState == 0 && lastButtonState == 1) {
    lastMode = mode;
    mode = (mode + 1) % 4;
  }
  lastButtonState = buttonState;
  
  //Serial.println(mode);
  
  digitalWrite(LEDs[lastMode], LOW);
  digitalWrite(LEDs[mode], HIGH);
  
  //digitalWrite(LED_BUILTIN, mode);
 
  
}