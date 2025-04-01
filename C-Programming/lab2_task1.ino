#define SENSORPIN A3
#define L1 9
#define value int

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(SENSORPIN, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  static int sensor_value;
  sensor_value = analogRead(SENSORPIN);
  Serial.println(sensor_value);
  sensor_value = map(sensor_value, 20, 450, 0, 10);
  if (sensor_value <= 5){
    digitalWrite(L1, HIGH);
  }else{
    digitalWrite(L1, LOW);
  }
  delay(100);
}
