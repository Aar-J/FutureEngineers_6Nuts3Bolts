//Ultrasonic Sensor with Serial Moniter
int trigger=9;
int echo=10;
float distance=0;
float count=0;

void setup() 
{
  pinMode(trigger,OUTPUT);
  pinMode(echo,INPUT);
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(trigger,LOW);
  delayMicroseconds(10);
  digitalWrite(trigger,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger,LOW);
  delayMicroseconds(10);
  count = pulseIn (echo, HIGH);
  distance=count*0.01715;
  Serial.println(distance);
  delay(500);
}
