int led[5] = {13,12,11,10,9};
int BUTTON = 2;
int val = 0;
int A_LED = A0;
int cnt;
int a;
int buttonInput = digitalRead(BUTTON);
void setup(){
  Serial.begin(9600);
  	pinMode(led[0], OUTPUT);
  	pinMode(led[1], OUTPUT);
  	pinMode(led[2], OUTPUT);
  	pinMode(led[3], OUTPUT);
  	pinMode(led[4], OUTPUT);
  	pinMode(BUTTON, INPUT);
}

void loop(){
	//int buttonInput = digitalRead(BUTTON);
  //if(buttonInput==HIGH);{
  if((a - buttonInput)>0){

   
        cnt = (cnt+1)%5;
    a = buttonInput;
        Serial.println(cnt);
  
  
    digitalWrite(led[cnt],HIGH);
                          delay(500);}
   
digitalWrite(led[cnt],LOW);

  //delay(500);
  //a+3;}}
	//digitalWrite(led[a],LOW);
  
  //if(buttonInput==1){
    //for (int i = 0; i < 5; i ++){
    
    
    //int a = i;
    //if (buttonInput == HIGH);{
   // digitalWrite(led[a],HIGH);
    //if(buttonInput==0)  break;
    //Serial.println(buttonInput);
    //Serial.println(buttonInput==HIGH);
    //Serial.println(buttonInput==LOW);
  	//for (int i = 0; i < 5; i ++)
    //delay(1000);
   // }}
    
    //for(int i = 0; i< 5; i ++){
      //digitalWrite(led[i],HIGH);}
    	//delay(1000);
      //if(buttonInput == LOW){
        //for(int i = 0; i< 5; i ++){
        //digitalWrite(led[i],LOW);
      //  delay(500);}}
    //}}
    
      //for(int i = 0; i< 5; i ++){
      //  digitalWrite(led[i],0);}
  
  
  //val = digitalRead(BUTTON);
  //int i = 0;{
  //{  
   // if (val == 1){
  	 // int i = 0;	 
     // i++;	
    
    
    
    	//digitalWrite(led[i], HIGH);
  //}
  //	else (val == 0) ;{
    //	digitalWrite(led[i], LOW);
    
   // }}}





   analogWrite(A_LED, HIGH);
  
  analogWrite(A_LED, LOW);}
//	bool button = digitalRead(BUTTON);
//if(BUTTON)
//{
 // if(val == 0) {
  //	val = 1;
    //Serial.println("2LED_ON");
    //digitalWrite(led[0], false);
    //digitalWrite(led[1], true);
    //digitalWrite(led[2], false);
    //digitalWrite(led[3], false);
    //digitalWrite(led[4], false);
  //} 
 // else if(val == 1){
  //	val = 2;
  	//Serial.println("3LED_ON");
    //digitalWrite(led[0], false);
    //digitalWrite(led[1], false);
    //digitalWrite(led[2], true);
    //digitalWrite(led[3], false);
    //digitalWrite(led[4], false);
  
  //}
  //else if(val == 2){
  	//val = 3;
  	//Serial.println("3LED_ON");
    //digitalWrite(led[0], false);
    //digitalWrite(led[1], false);
//    digitalWrite(led[2], false);
  //  digitalWrite(led[3], true);
    //digitalWrite(led[4], false);
  
  //}
  //else if(val == 3){
  	//val = 4;
  	//Serial.println("4LED_ON");
    //digitalWrite(led[0], false);
    //digitalWrite(led[1], false);
    //digitalWrite(led[2], false);
    //digitalWrite(led[3], false);
    //digitalWrite(led[4], true);
  
  //}
   
  //else{
    //val = 0;
  	//Serial.println("1LED_ON");
    //digitalWrite(led[0], true);
    //digitalWrite(led[1], false);
//    digitalWrite(led[2], false);
  //  digitalWrite(led[3], false);
    //digitalWrite(led[4], false);
  
  //}
  //}
  //delay(500);
//}
  
  
  
  
  










//const int LED[5] = {13,12,11,10,9};
//const int BUTTON = 7;
//const int GA = 5;
//const int A_LED = 3;

//int val = 0;

//void setup() {
  //Serial.begin(9600);
  //for (int i = 0; i < 5; i ++){
  //int i = 0;
  //if BUTTON == True;
  //{
  	//int i + 1    
  //}
 //   pinMode(LED[i], OUTPUT);
 //   pinMode(BUTTON, INPUT);
//	if (digitalRead(BUTTON)==HIGH)
    //if (val == HIGH)
      //for (int i = 0; i < 5; i ++){
    //if (val == HIGH)
  //  		digitalWrite(LED[i],HIGH);
 //       Serial.println(i);}}
  	//else (val == LOW);{
		//for (int i = 0; i < 5; i ++)     
    		//digitalWrite(LED[i],LOW);
    	//pinMode(LED[i], OUTPUT);
  		//pinMode(BUTTON, INPUT);
     	 //	Serial.println(i);}}
//}
//}
//void loop() {
 // val = digitalRead(BUTTON);

  //if (val == HIGH) {
   	//for (int i = 0; i < 5; i ++)
   //	digitalWrite(LED[i], HIGH);
  
  
  //analogWrite(A_LED, HIGH);
  //if (val == HIGH){
    //for (int i = 0; i < 5; i ++)
    //if (val == HIGH)
      //digitalWrite(LED[i],HIGH);
      //Serial.println("LED[i]");
    
   //else (val == LOW);{
	//	for (int i = 0; i < 5; i ++)     
    	//digitalWrite(LED[i],LOW);
     // digitalWrite(LED[i+1],HIGH);}
   // Serial.println("");
//}
  //else {
   // for (int i = 0; i < 5; i ++)
    	
    //	//if ((LED[i] - LED[i+1]) == 1)
    //		digitalWrite(LED[i], LOW);
      	//	//Serial.print("i");
   // analogWrite(A_LED, LOW);}
