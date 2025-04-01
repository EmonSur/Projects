#define B00000000 0x0
#define Bxx111111 0x3F
#define Bxx000010 0x2
#define Bxx000001 0x1
#define LED_PIN 9
#define LED_PIN 8

int i = 0;

void setup() {
    Serial.begin(9600);
    DDRD = B00000000;
    DDRB = Bxx111111;
}

void lights() {
    char c = PIND;
}

void loop() {
    for (char c[i]; i < 8; i++) {
        if (c[i] == c[i + 1]) {
            if (c[i] == 0) {
                PINB |= Bxx000010;
            } else {
                PINB |= Bxx000001;
            }
        }
    }
}
