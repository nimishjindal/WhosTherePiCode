#include <Servo.h>
Servo myserv;
void setup() {
  // put your setup code here, to run once:
  myserv.attach(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  myserv.write(0);
  delay(800);
  myserv.write(90);
  delay(800);
  myserv.write(180);
  delay(800);
  myserv.write(90);
  delay(800);
  

  
}
