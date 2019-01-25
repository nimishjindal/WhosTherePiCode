//int LEDpinY = 9;
int LEDpinR = 13;

void setup() {
  // put your setup code here, to run once:

  //pinMode(LEDpinY,OUTPUT);
  pinMode(LEDpinR,OUTPUT);

  
}

void loop() {
  // put your main code here, to run repeatedly:
 
 digitalWrite(LEDpinR,HIGH); 
 delay(1000);
 digitalWrite(LEDpinR,LOW); 
 delay(1000);
}

