const int BUZZER = 10;
const int ACTIVE_BUZZER = 11;
const int buttonPin = 2;

void setup() {
    pinMode(buttonPin, INPUT);
    pinMode(ACTIVE_BUZZER, OUTPUT);

    digitalWrite(ACTIVE_BUZZER, HIGH);
    
    tone(BUZZER, 262);

    delay(3000);
    digitalWrite(ACTIVE_BUZZER, LOW);
    noTone(BUZZER);
}

void loop(){
    int buttonInput = digitalRead(buttonPin);
    digitalWrite(ACTIVE_BUZZER, buttonInput);
    delay(1000);
    tone(BUZZER, buttonInput);
}