
# # # while 1:
# # r = 4
# # for r in range(20):
# #         r += 1
# #         print(r)
# #         # for y in range(5, 20):
# #             # y = r*2



# # import random
# # LottorNumber = []
# # while len(LottorNumber) < 6 :
# # 	V = random.randint(1,45)
# # 	if V not in LottorNumber:
# # 		LottorNumber.append(V)

# # print(LottorNumber)

# card[1] : [75]
# card[2] : [45]
# card[3] : [43]
# card[4] : [92]
# card[5] : [58]
# card[6] : [66]
# card[7] : [41]
# card[8] : [91]
# card[9] : [87]
# card[10] : [63]
# card[11] : [1]
# card[12] : [89]
# card[13] : [74]
# card[14] : [88]
# card[15] : [65]
# card[16] : [28]
# card[17] : [9]
# card[18] : [48]
# card[19] : [16]
# card[20] : [81]
# card[21] : [8]
# card[22] : [96]
# card[23] : [68]
# card[24] : [13]
# card[25] : [53]
# card[26] : [33]
# card[27] : [70]
# card[28] : [38]
# card[29] : [26]
# card[30] : [98]
# card[31] : [12]
# card[32] : [31]
# card[33] : [78]
# card[34] : [15]
# card[35] : [61]
# card[36] : [32]
# card[37] : [59]
# card[38] : [100]
# card[39] : [5]
# card[40] : [29]
# card[41] : [46]
# card[42] : [30]
# card[43] : [17]
# card[44] : [22]
# card[45] : [50]
# card[46] : [73]
# card[47] : [37]
# card[48] : [6]
# card[49] : [23]
# card[50] : [44]
# card[51] : [47]
# card[52] : [40]
# card[53] : [77]
# card[54] : [84]
# card[55] : [99]
# card[56] : [80]
# card[57] : [93]
# card[58] : [97]
# card[59] : [85]
# card[60] : [24]
# card[61] : [36]
# card[62] : [86]
# card[63] : [52]
# card[64] : [39]
# card[65] : [79]
# card[66] : [67]
# card[67] : [56]
# card[68] : [21]
# card[69] : [55]
# card[70] : [7]
# card[71] : [20]
# card[72] : [49]
# card[73] : [42]
# card[74] : [76]
# card[75] : [82]
# card[76] : [35]
# card[77] : [54]
# card[78] : [57]
# card[79] : [60]
# card[80] : [62]
# card[81] : [69]
# card[82] : [14]
# card[83] : [64]
# card[84] : [90]
# card[85] : [25]
# card[86] : [3]
# card[87] : [11]
# card[88] : [51]
# card[89] : [72]

int BUTTON_PIN = 2;
int PWM_LED_PIN = 3;

int LEDs[] = {13,12,11,10,9};

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
  
  for (int i=0; i<5; i++){
    pinMode(LEDs[i], OUTPUT);
  }
  
  Serial.begin(9600);
}

void loop()
{
  int potentiometerVal = analogRead(POTENTIOMETER_PIN);
   
  analogWrite(PWM_LED_PIN, potentiometerVal / 4);
  
  int buttonState = digitalRead(BUTTON_PIN);
   
  if (buttonState == 1 && lastButtonState == 0) {
    lastMode = mode;
    mode = (mode + 1) % 5;
  }
  lastButtonState = buttonState;
   
  digitalWrite(LEDs[lastMode], LOW);
  digitalWrite(LEDs[mode], HIGH);
   
}