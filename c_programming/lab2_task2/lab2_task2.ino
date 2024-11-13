short int IN_PIN = A0;
short int count1 = 0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  count1 = map(analogRead(IN_PIN), 0, 1023, 0, 10);
  Serial.println(count1);
}