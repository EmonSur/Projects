int MIDDLEC = 3822;
int NOTED = 3405;
int NOTEE = 3033;
int NOTEF = 2863;
int NOTEG = 2552;
int NOTEA = 2272


int NOTEB = 2025;
int HIGHC = 1911;

#define tonePin 9

void setup() {
  pinMode(tonePin, OUTPUT);
}


void music(int period) {
  int i;
  short waves = 25;
  short hp = period;
    for (i=1; i<waves; i++){
      digitalWrite(tonePin, HIGH);
      delayMicroseconds(hp);
      digitalWrite(tonePin, LOW);
      delayMicroseconds(hp);
    }
}

void loop() {
  music(MIDDLEC);
  music(NOTED);
  music(NOTEE);
  music(NOTEF);
  music(NOTEG);
  music(NOTEA);
  music(NOTEB);
  music(HIGHC);

}
