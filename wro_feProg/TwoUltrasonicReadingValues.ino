//Ultrasonic Sensor with Serial Monitor
int trigger1 = 8;//r
int echo1 = 9;
int trigger2 = 10;//l
int echo2 = 11;
int trigger3 = 12;//f
int echo3 = 13;

float distance1 = 0;
float distance2 = 0;
float distance3 = 0;
float count3 = 0;
float count1 = 0;
float count2 = 0;

void setup() 
{
  pinMode(trigger1, OUTPUT);
  pinMode(echo1, INPUT);
  pinMode(trigger2, OUTPUT);
  pinMode(echo2, INPUT);
  pinMode(trigger3,OUTPUT);
  pinMode(echo3,INPUT);
  Serial.begin(9600);
}

void loop()
{
  // Sensor 1 right
  digitalWrite(trigger1, LOW);
  delayMicroseconds(10);
  digitalWrite(trigger1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger1, LOW);
  count1 = pulseIn(echo1, HIGH);
  distance1 = count1 * 0.01715;

  // Sensor 2 left
  digitalWrite(trigger2, LOW);
  delayMicroseconds(10);
  digitalWrite(trigger2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger2, LOW);
  count2 = pulseIn(echo2, HIGH);
  distance2 = count2 * 0.01715;

  //sensor 3 center
  digitalWrite(trigger3, LOW);
  delayMicroseconds(10);
  digitalWrite(trigger3, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger3, LOW);
  count3 = pulseIn(echo3, HIGH);
  distance3 = count3 * 0.01715;

  // Send both distances via Serial
  Serial.print(distance1);
  Serial.print(",");
  Serial.print(distance2);
  Serial.print(",");
  Serial.println(distance3);
  
  delay(10);
}
